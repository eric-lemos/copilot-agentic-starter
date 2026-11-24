from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath, PureWindowsPath


JSON_BLOCK = re.compile(r"^```json[ \t]*\r?\n(.*?)^```[ \t]*\r?$", re.MULTILINE | re.DOTALL)
HEADING = re.compile(r"^ {0,3}#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$")
LEGACY_VERSIONS = {"1.0", "1.1", "1.2"}


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> object:
    raise ValueError(f"Invalid JSON constant: {value}")


def _validate_refactoring(document: dict[str, object], root: Path) -> list[str]:
    errors: list[str] = []
    if document.get("work_type") != "refactor":
        errors.append("'work_type' must be 'refactor' for schema version 1.4.")
    details = document.get("refactoring")
    if not isinstance(details, dict):
        return errors + ["'refactoring' must be an object."]

    for field in ("source_path", "target_path"):
        value = details.get(field)
        if not isinstance(value, str) or not value.strip() or "\\" in value or "\0" in value:
            errors.append(f"'refactoring.{field}' must be a workspace-relative path using '/'.")
            continue
        path = PurePosixPath(value)
        if path.is_absolute() or PureWindowsPath(value).drive or ".." in path.parts:
            errors.append(f"'refactoring.{field}' must be a workspace-relative path using '/'.")
            continue
        try:
            (root / path).resolve().relative_to(root.resolve())
        except ValueError:
            errors.append(f"'refactoring.{field}' resolves outside the workspace.")
        except (OSError, RuntimeError) as error:
            errors.append(f"'refactoring.{field}' cannot be resolved: {error}")

    for field in ("current_state", "preserve", "validation_strategy"):
        value = details.get(field)
        if not isinstance(value, list) or not value or any(
            not isinstance(item, str) or not item.strip() for item in value
        ):
            errors.append(f"'refactoring.{field}' must be a non-empty array of non-empty strings.")
    return errors


def validate_instruction_reviews(markdown: str, root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    blocks = JSON_BLOCK.findall(markdown)
    if len(blocks) != 1:
        return ["Expected exactly one fenced JSON block."], warnings
    try:
        document = json.loads(blocks[0], object_pairs_hook=_unique_object, parse_constant=_reject_constant)
    except (json.JSONDecodeError, ValueError) as error:
        return [f"Invalid JSON: {error}"], warnings
    if not isinstance(document, dict):
        return ["Discovery JSON must be an object."], warnings

    version = document.get("schema_version")
    if isinstance(version, str) and version in LEGACY_VERSIONS:
        return errors, ["Legacy discovery: instruction review coverage is not verifiable."]
    if version not in ("1.3", "1.4"):
        return [f"Unsupported schema version: {version!r}"], warnings
    if version == "1.4":
        errors.extend(_validate_refactoring(document, root))
    elif document.get("work_type") == "refactor":
        errors.append("Refactoring requires schema version 1.4.")

    status = document.get("status")
    if status not in ("proposed", "approved"):
        errors.append("Discovery status must be 'proposed' or 'approved'.")

    instructions_dir = root / ".github" / "instructions"
    if not instructions_dir.is_dir():
        return errors + ["Instruction directory is missing."], warnings
    expected = {
        path.relative_to(root).as_posix(): path
        for path in instructions_dir.glob("*.instructions.md")
        if path.is_file()
    }
    if not expected:
        return errors + ["No instruction files were found."], warnings

    known_items: set[str] = set()
    for field in ("requirements", "decisions"):
        items = document.get(field)
        if not isinstance(items, list):
            errors.append(f"'{field}' must be an array.")
            continue
        for item in items:
            if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not item["id"].strip():
                errors.append(f"Every item in '{field}' must have a non-empty string id.")
            else:
                known_items.add(item["id"])

    reviews = document.get("instruction_reviews")
    if not isinstance(reviews, list):
        return errors + ["'instruction_reviews' must be an array."], warnings

    seen: set[str] = set()
    for review in reviews:
        if not isinstance(review, dict):
            errors.append("Every instruction review must be an object.")
            continue
        instruction = review.get("instruction")
        if not isinstance(instruction, str) or instruction not in expected:
            errors.append(f"Unknown instruction: {instruction!r}")
            continue
        if instruction in seen:
            errors.append(f"Duplicate instruction review: {instruction}")
        seen.add(instruction)
        applicability = review.get("applicability")
        if applicability not in ("applicable", "not_applicable", "pending"):
            errors.append(f"{instruction}: invalid applicability.")
        if status == "approved" and applicability == "pending":
            errors.append(f"{instruction}: pending applicability is not allowed in an approved baseline.")
        rationale = review.get("rationale")
        if not isinstance(rationale, str) or not rationale.strip():
            errors.append(f"{instruction}: rationale must be a non-empty string.")

        sections = review.get("reviewed_sections")
        if not isinstance(sections, list) or not sections or any(
            not isinstance(section, str) or not section.strip() for section in sections
        ):
            errors.append(f"{instruction}: reviewed_sections must be a non-empty array of strings.")
        else:
            path = expected[instruction]
            try:
                path.resolve().relative_to(root.resolve())
                text = path.read_text(encoding="utf-8-sig")
            except ValueError:
                errors.append(f"{instruction}: instruction path escapes the workspace.")
            except (OSError, UnicodeError) as error:
                errors.append(f"{instruction}: cannot read instruction: {error}")
            else:
                headings = {
                    match.group(1).strip()
                    for line in text.splitlines()
                    if (match := HEADING.fullmatch(line))
                }
                for section in sections:
                    if section not in headings:
                        errors.append(f"{instruction}: Unknown section: {section!r}")

        related = review.get("related_items")
        if not isinstance(related, list) or any(
            not isinstance(item, str) or not item.strip() for item in related
        ):
            errors.append(f"{instruction}: related_items must be an array of non-empty strings.")
        else:
            if applicability == "not_applicable" and related:
                errors.append(f"{instruction}: a not_applicable review cannot have related items.")
            for item in related:
                if item not in known_items:
                    errors.append(f"{instruction}: Unknown related item: {item}")

    for instruction in sorted(expected.keys() - seen):
        errors.append(f"Missing instruction review: {instruction}")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check discovery instruction review coverage.")
    parser.add_argument("discovery", help="Path to a discovery Markdown file.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    path = Path(args.discovery)
    if not path.is_absolute():
        path = root / path
    try:
        markdown = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as error:
        print(f"Cannot read discovery file: {error}", file=sys.stderr)
        return 1
    errors, warnings = validate_instruction_reviews(markdown, root)
    for warning in warnings:
        print(f"Warning: {warning}", file=sys.stderr)
    for error in errors:
        print(f"Error: {error}", file=sys.stderr)
    if errors:
        return 1
    if not warnings:
        print("Discovery instruction review coverage is structurally valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
