from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


FRONTMATTER_END = "---"
AGENT_SUFFIX = ".agent.md"
INLINE_LIST_PATTERN = re.compile(r"^[A-Za-z0-9_-]+(?:\s*,\s*[A-Za-z0-9_-]+)*$")
FRONTMATTER_KEY_PATTERN = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):(?:[ \t]*(.*))?$")
INLINE_REFERENCE_PATTERN = re.compile(r"`([^`]+)`")
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
VALID_NAME_PATTERN = re.compile(r"^[a-z][a-z0-9-]*$")
SKILL_BOOLEAN_FIELDS = frozenset({"disable-model-invocation", "user-invocable"})


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    message: str

    def __str__(self) -> str:
        return f"{self.path}:{self.line}: {self.message}"


def _parse_scalar(value: str) -> str | None:
    value = value.strip()
    if not value:
        return None

    if re.fullmatch(r"(?i:null|true|false|~|[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[-+]?\d+)?)", value):
        return None
    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return None
        return parsed if isinstance(parsed, str) else None

    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            return None
        return value[1:-1].replace("''", "'")

    if value.startswith("[") or value.endswith("]"):
        return None
    return value


def _parse_list(value: str) -> list[str] | None:
    value = value.strip()
    if value == "[]":
        return []
    if not (value.startswith("[") and value.endswith("]")):
        return None

    contents = value[1:-1].strip()
    if not contents:
        return []
    if not INLINE_LIST_PATTERN.fullmatch(contents):
        return None
    return [item.strip() for item in contents.split(",")]


def parse_frontmatter(text: str, display_path: str) -> tuple[dict[str, object], list[Finding]]:
    lines = text.splitlines()
    findings: list[Finding] = []
    if not lines or lines[0].strip() != FRONTMATTER_END:
        return {}, [Finding(display_path, 1, "Missing YAML frontmatter opening delimiter '---'.")]

    end_index = next(
        (index for index in range(1, len(lines)) if lines[index].strip() == FRONTMATTER_END),
        None,
    )
    if end_index is None:
        return {}, [Finding(display_path, len(lines), "Missing YAML frontmatter closing delimiter '---'.")]

    metadata: dict[str, object] = {}
    active_list_key: str | None = None

    for index in range(1, end_index):
        line_number = index + 1
        line = lines[index]
        if not line.strip():
            continue

        if line.startswith("  - "):
            if active_list_key is None:
                findings.append(
                    Finding(display_path, line_number, "List item is not attached to a frontmatter field.")
                )
                continue
            item = _parse_scalar(line[4:])
            if item is None:
                findings.append(Finding(display_path, line_number, "Invalid frontmatter list item."))
                continue
            value = metadata[active_list_key]
            if isinstance(value, list):
                value.append(item)
            continue

        active_list_key = None
        match = FRONTMATTER_KEY_PATTERN.fullmatch(line)
        if not match:
            findings.append(Finding(display_path, line_number, "Invalid frontmatter field syntax."))
            continue

        key, raw_value = match.groups()
        if key in metadata:
            findings.append(Finding(display_path, line_number, f"Duplicate frontmatter field '{key}'."))
            continue

        if raw_value is None or raw_value == "":
            metadata[key] = []
            active_list_key = key
        elif raw_value.strip().startswith("["):
            parsed_list = _parse_list(raw_value)
            if parsed_list is None:
                findings.append(Finding(display_path, line_number, f"Invalid list value for '{key}'."))
            else:
                metadata[key] = parsed_list
        elif key in SKILL_BOOLEAN_FIELDS and raw_value.strip() in {"true", "false"}:
            metadata[key] = raw_value.strip() == "true"
        else:
            parsed_value = _parse_scalar(raw_value)
            if parsed_value is None:
                findings.append(Finding(display_path, line_number, f"Invalid scalar value for '{key}'."))
            else:
                metadata[key] = parsed_value

    return metadata, findings


def _read_text(path: Path, root: Path, findings: list[Finding]) -> str | None:
    try:
        return path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as error:
        findings.append(
            Finding(path.relative_to(root).as_posix(), 1, f"Cannot read file: {error}")
        )
        return None


def _validate_apply_to(pattern: str, path: str, line: int) -> list[Finding]:
    findings: list[Finding] = []
    if not pattern.strip():
        return [Finding(path, line, "'applyTo' must not be empty.")]
    if "\\" in pattern:
        findings.append(Finding(path, line, "'applyTo' must use forward slashes."))
    if pattern.startswith("/") or ".." in pattern.split("/"):
        findings.append(Finding(path, line, "'applyTo' must be a relative glob without parent segments."))

    opening_index: int | None = None
    for index, character in enumerate(pattern):
        if character == "{":
            if opening_index is not None:
                findings.append(Finding(path, line, "Nested braces are not supported in 'applyTo' globs."))
            else:
                opening_index = index
        elif character == "}":
            if opening_index is None:
                findings.append(Finding(path, line, "Unmatched '}' in 'applyTo' glob."))
            else:
                alternatives = pattern[opening_index + 1 : index].split(",")
                if len(alternatives) < 2 or any(not item.strip() for item in alternatives):
                    findings.append(
                        Finding(path, line, "Brace alternatives in 'applyTo' must be non-empty and comma-separated.")
                    )
                opening_index = None
    if opening_index is not None:
        findings.append(Finding(path, line, "Unclosed '{' in 'applyTo' glob."))
    return findings


def _frontmatter_field_line(text: str, field: str) -> int:
    for line_number, line in enumerate(text.splitlines()[1:], start=2):
        if line.strip() == FRONTMATTER_END:
            break
        match = FRONTMATTER_KEY_PATTERN.fullmatch(line)
        if match and match.group(1) == field:
            return line_number
    return 2


def _validate_ui_metadata(path: Path, root: Path, findings: list[Finding]) -> None:
    display_path = path.relative_to(root).as_posix()
    text = _read_text(path, root, findings)
    if text is None:
        return

    values: dict[str, str] = {}
    interface_seen = False
    supported_fields = {"display_name", "short_description"}
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line == "interface:":
            if interface_seen:
                findings.append(Finding(display_path, line_number, "Duplicate 'interface' mapping."))
            interface_seen = True
            continue

        match = re.fullmatch(r"  ([A-Za-z][A-Za-z0-9_-]*):[ \t]*(.*)", line)
        if not match or not interface_seen:
            findings.append(Finding(display_path, line_number, "Unsupported or invalid YAML structure."))
            continue

        key, raw_value = match.groups()
        if key not in supported_fields:
            findings.append(Finding(display_path, line_number, f"Unsupported UI metadata field '{key}'."))
            continue
        if key in values:
            findings.append(Finding(display_path, line_number, f"Duplicate UI metadata field '{key}'."))
            continue
        value = _parse_scalar(raw_value)
        if value is None:
            findings.append(Finding(display_path, line_number, f"Invalid value for UI metadata field '{key}'."))
            continue
        values[key] = value

    if not interface_seen:
        findings.append(Finding(display_path, 1, "Missing 'interface' mapping."))
    for key in sorted(supported_fields - values.keys()):
        findings.append(Finding(display_path, 1, f"Missing UI metadata field '{key}'."))


def _validate_local_references(root: Path, markdown_files: list[Path], findings: list[Finding]) -> None:
    root_resolved = root.resolve()
    for markdown_path in markdown_files:
        text = _read_text(markdown_path, root, findings)
        if text is None:
            continue
        display_path = markdown_path.relative_to(root).as_posix()

        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in INLINE_REFERENCE_PATTERN.finditer(line):
                reference = match.group(1)
                if reference.startswith(".github/"):
                    candidate = root.joinpath(*PurePosixPath(reference.rstrip("/")).parts)
                elif reference.startswith("references/") and markdown_path.name == "SKILL.md":
                    candidate = markdown_path.parent.joinpath(*PurePosixPath(reference).parts)
                else:
                    continue
                resolved = candidate.resolve()
                try:
                    resolved.relative_to(root_resolved)
                except ValueError:
                    findings.append(Finding(display_path, line_number, f"Reference escapes workspace: '{reference}'."))
                    continue
                if not resolved.exists():
                    findings.append(Finding(display_path, line_number, f"Referenced path does not exist: '{reference}'."))

            for match in MARKDOWN_LINK_PATTERN.finditer(line):
                target = match.group(1).strip()
                if target.startswith("<") and ">" in target:
                    target = target[1 : target.index(">")]
                else:
                    target = target.split()[0]
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                link_path = unquote(parsed.path)
                candidate = root / link_path.lstrip("/") if link_path.startswith("/") else markdown_path.parent / link_path
                resolved = candidate.resolve()
                try:
                    resolved.relative_to(root_resolved)
                except ValueError:
                    findings.append(Finding(display_path, line_number, f"Markdown link escapes workspace: '{target}'."))
                    continue
                if not resolved.exists():
                    findings.append(Finding(display_path, line_number, f"Markdown link target does not exist: '{target}'."))


def validate_workspace(root: Path) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    github_dir = root / ".github"
    if not github_dir.is_dir():
        return [Finding(".github", 1, "Missing '.github' configuration directory.")]

    agent_files = sorted((github_dir / "agents").glob("*.agent.md"))
    instruction_files = sorted((github_dir / "instructions").glob("*.instructions.md"))
    skill_files = sorted((github_dir / "skills").rglob("SKILL.md"))
    agent_metadata: dict[str, tuple[Path, dict[str, object]]] = {}
    agent_name_paths: dict[str, Path] = {}

    for path in agent_files:
        display_path = path.relative_to(root).as_posix()
        text = _read_text(path, root, findings)
        if text is None:
            continue
        metadata, parse_findings = parse_frontmatter(text, display_path)
        findings.extend(parse_findings)

        name = metadata.get("name")
        if not isinstance(name, str) or not VALID_NAME_PATTERN.fullmatch(name):
            findings.append(Finding(display_path, 2, "'name' must be a lowercase agent identifier."))
            continue
        expected_name = path.name[: -len(AGENT_SUFFIX)]
        if name != expected_name:
            findings.append(
                Finding(display_path, 2, f"Agent name '{name}' does not match filename '{expected_name}'.")
            )
        if name in agent_name_paths:
            findings.append(
                Finding(display_path, 2, f"Duplicate agent name '{name}' also declared in "
                f"'{agent_name_paths[name].relative_to(root).as_posix()}'.")
            )
        else:
            agent_name_paths[name] = path

        for field in ("description", "target"):
            if not isinstance(metadata.get(field), str) or not str(metadata[field]).strip():
                findings.append(Finding(display_path, 2, f"'{field}' must be a non-empty string."))
        for field in ("tools", "agents"):
            value = metadata.get(field)
            if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
                findings.append(Finding(display_path, 2, f"'{field}' must be a list of non-empty strings."))
                continue
            if len(value) != len(set(value)):
                findings.append(Finding(display_path, 2, f"'{field}' must not contain duplicates."))

        agent_metadata[name] = (path, metadata)

    for name, (path, metadata) in agent_metadata.items():
        delegated_agents = metadata.get("agents")
        if not isinstance(delegated_agents, list):
            continue
        display_path = path.relative_to(root).as_posix()
        for delegated_name in delegated_agents:
            if delegated_name == name:
                findings.append(Finding(display_path, 2, "An agent must not delegate to itself."))
            elif delegated_name not in agent_name_paths:
                findings.append(
                    Finding(display_path, 2, f"Delegated agent '{delegated_name}' does not exist.")
                )

    for path in instruction_files:
        display_path = path.relative_to(root).as_posix()
        text = _read_text(path, root, findings)
        if text is None:
            continue
        metadata, parse_findings = parse_frontmatter(text, display_path)
        findings.extend(parse_findings)
        description = metadata.get("description")
        if not isinstance(description, str) or not description.strip():
            findings.append(Finding(display_path, 2, "'description' must be a non-empty string."))
        apply_to = metadata.get("applyTo")
        if apply_to is not None:
            if not isinstance(apply_to, str):
                findings.append(Finding(display_path, _frontmatter_field_line(text, "applyTo"), "'applyTo' must be a string."))
            else:
                findings.extend(
                    _validate_apply_to(
                        apply_to,
                        display_path,
                        _frontmatter_field_line(text, "applyTo"),
                    )
                )

    for path in skill_files:
        display_path = path.relative_to(root).as_posix()
        text = _read_text(path, root, findings)
        if text is None:
            continue
        metadata, parse_findings = parse_frontmatter(text, display_path)
        findings.extend(parse_findings)
        for field in ("name", "description"):
            if not isinstance(metadata.get(field), str) or not str(metadata[field]).strip():
                findings.append(Finding(display_path, 2, f"'{field}' must be a non-empty string."))
        for field in SKILL_BOOLEAN_FIELDS:
            if field in metadata and not isinstance(metadata[field], bool):
                findings.append(
                    Finding(display_path, _frontmatter_field_line(text, field), f"'{field}' must be a boolean.")
                )
        name = metadata.get("name")
        if isinstance(name, str) and name != path.parent.name:
            findings.append(
                Finding(display_path, 2, f"Skill name '{name}' does not match directory '{path.parent.name}'.")
            )

    yaml_files = sorted(path for path in github_dir.rglob("*") if path.suffix.lower() in {".yaml", ".yml"})
    ui_metadata_files = set(github_dir.glob("skills/**/agents/ui_metadata.yaml"))
    workflow_dir = github_dir / "workflows"
    workflow_files = set(workflow_dir.glob("*.yaml")) | set(workflow_dir.glob("*.yml"))
    for path in yaml_files:
        if path not in ui_metadata_files and path not in workflow_files:
            findings.append(
                Finding(path.relative_to(root).as_posix(), 1, "No YAML validator is registered for this file.")
            )
    for path in sorted(ui_metadata_files):
        _validate_ui_metadata(path, root, findings)

    markdown_files = sorted(
        path
        for path in root.rglob("*.md")
        if "node_modules" not in path.relative_to(root).parts
    )
    _validate_local_references(root, markdown_files, findings)
    return sorted(findings, key=lambda finding: (finding.path, finding.line, finding.message))


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    findings = validate_workspace(root)
    if findings:
        for finding in findings:
            print(finding)
        print(f"Agentic configuration validation failed with {len(findings)} finding(s).")
        return 1

    print("Agentic configuration validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
