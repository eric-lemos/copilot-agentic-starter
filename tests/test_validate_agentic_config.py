from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from validate_agentic_config import validate_workspace
from validate_discovery import validate_instruction_reviews


class ValidateAgenticConfigTests(unittest.TestCase):
    def test_repository_configuration_is_valid(self) -> None:
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(validate_workspace(root), [])

    def test_reports_unknown_delegation_and_invalid_apply_to(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self._write(
                root,
                ".github/agents/owner.agent.md",
                """---
name: owner
description: Owner agent.
target: false
tools: [read]
agents: [missing]
---
""",
            )
            self._write(
                root,
                ".github/instructions/sample.instructions.md",
                """---
description: Sample instructions.
applyTo: "**/*.{py,}"
---
""",
            )

            findings = validate_workspace(root)
            messages = [finding.message for finding in findings]

            self.assertIn("Delegated agent 'missing' does not exist.", messages)
            self.assertIn("Invalid scalar value for 'target'.", messages)
            self.assertIn(
                "Brace alternatives in 'applyTo' must be non-empty and comma-separated.",
                messages,
            )

    def test_reports_missing_frontmatter_delimiter_and_reference(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self._write(
                root,
                ".github/agents/broken.agent.md",
                """---
name: broken
description: Broken agent.
target: vscode
tools: [read]
agents: []
""",
            )
            self._write(
                root,
                "README.md",
                "See `.github/missing.md` for details.\n",
            )

            findings = validate_workspace(root)
            messages = [finding.message for finding in findings]

            self.assertIn("Missing YAML frontmatter closing delimiter '---'.", messages)
            self.assertIn("Referenced path does not exist: '.github/missing.md'.", messages)

    def test_accepts_github_actions_workflow_yaml(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self._write(
                root,
                ".github/workflows/validate.yml",
                """name: Validate
on:
  push:
jobs:
  validate:
    runs-on: ubuntu-latest
    steps: []
""",
            )

            self.assertEqual(validate_workspace(root), [])

    def test_validates_skill_invocation_flags_as_booleans(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self._write(
                root,
                ".github/skills/sample/SKILL.md",
                """---
name: sample
description: Sample skill.
disable-model-invocation: true
user-invocable: false
---
""",
            )
            self.assertEqual(validate_workspace(root), [])

            self._write(
                root,
                ".github/skills/sample/SKILL.md",
                """---
name: sample
description: Sample skill.
disable-model-invocation: "true"
---
""",
            )
            messages = [finding.message for finding in validate_workspace(root)]
            self.assertIn("'disable-model-invocation' must be a boolean.", messages)

    def test_ignores_dependency_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / ".github").mkdir()
            self._write(
                root,
                "node_modules/example/README.md",
                "See `.github/missing.md` for details.\n",
            )

            self.assertEqual(validate_workspace(root), [])

    @staticmethod
    def _write(root: Path, relative_path: str, content: str) -> None:
        path = root / Path(relative_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


class ValidateDiscoveryInstructionReviewsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        instructions = self.root / ".github" / "instructions"
        instructions.mkdir(parents=True)
        (instructions / "security.instructions.md").write_text(
            "# Security\n\n## Authorization\n", encoding="utf-8"
        )
        (instructions / "testing.instructions.md").write_text(
            "# Testing\n\n## Scenarios\n", encoding="utf-8"
        )
        self.document = {
            "schema_version": "1.3",
            "status": "approved",
            "requirements": [{"id": "RF-01"}],
            "decisions": [],
            "instruction_reviews": [
                {
                    "instruction": ".github/instructions/security.instructions.md",
                    "applicability": "applicable",
                    "reviewed_sections": ["Authorization"],
                    "rationale": "Access control applies.",
                    "related_items": ["RF-01"],
                },
                {
                    "instruction": ".github/instructions/testing.instructions.md",
                    "applicability": "not_applicable",
                    "reviewed_sections": ["Scenarios"],
                    "rationale": "No implementation is in scope.",
                    "related_items": [],
                },
            ],
        }

    def _validate(self, document: dict) -> tuple[list[str], list[str]]:
        return validate_instruction_reviews(
            f"# Discovery\n\n```json\n{json.dumps(document)}\n```\n", self.root
        )

    def test_accepts_complete_reviews(self) -> None:
        self.assertEqual(self._validate(self.document), ([], []))

    def test_accepts_refactoring_metadata(self) -> None:
        self.document.update(
            {
                "schema_version": "1.4",
                "work_type": "refactor",
                "refactoring": {
                    "source_path": "project",
                    "target_path": "project",
                    "current_state": ["Existing API and tests were inspected."],
                    "preserve": ["Existing API behavior."],
                    "validation_strategy": ["Run existing API tests."],
                },
            }
        )
        self.assertEqual(self._validate(self.document), ([], []))

    def test_rejects_missing_or_unsafe_refactoring_metadata(self) -> None:
        self.document.update({"schema_version": "1.4", "work_type": "refactor"})
        errors, _ = self._validate(self.document)
        self.assertTrue(any("refactoring" in error for error in errors))

        self.document["refactoring"] = {
            "source_path": "../outside",
            "target_path": "C:/outside",
            "current_state": [],
            "preserve": ["Existing API behavior."],
            "validation_strategy": ["Run existing tests."],
        }
        errors, _ = self._validate(self.document)
        for field in ("source_path", "target_path", "current_state"):
            self.assertTrue(any(field in error for error in errors))

    def test_rejects_unknown_refactoring_work_type(self) -> None:
        self.document.update({"schema_version": "1.4", "work_type": "unknown"})
        errors, _ = self._validate(self.document)
        self.assertTrue(any("work_type" in error for error in errors))

    def test_rejects_refactoring_marked_as_discovery_version(self) -> None:
        self.document["work_type"] = "refactor"
        errors, _ = self._validate(self.document)
        self.assertTrue(any("requires schema version 1.4" in error for error in errors))

    def test_detects_new_instruction_after_review(self) -> None:
        (self.root / ".github" / "instructions" / "new.instructions.md").write_text(
            "# New\n", encoding="utf-8"
        )
        errors, _ = self._validate(self.document)
        self.assertTrue(any("new.instructions.md" in error for error in errors))

    def test_reports_missing_duplicate_and_unrecognized_instructions(self) -> None:
        reviews = self.document["instruction_reviews"]
        reviews[1] = reviews[0].copy()
        reviews.append({**reviews[0], "instruction": ".github/instructions/unknown.instructions.md"})
        errors, _ = self._validate(self.document)
        self.assertTrue(any("Missing instruction review" in error for error in errors))
        self.assertTrue(any("Duplicate instruction review" in error for error in errors))
        self.assertTrue(any("Unknown instruction" in error for error in errors))

    def test_reports_invalid_sections_references_and_unresolved_review(self) -> None:
        review = self.document["instruction_reviews"][0]
        review["reviewed_sections"] = ["Nonexistent"]
        review["rationale"] = " "
        review["related_items"] = ["missing"]
        review["applicability"] = "pending"
        errors, _ = self._validate(self.document)
        self.assertTrue(any("Unknown section" in error for error in errors))
        self.assertTrue(any("rationale" in error for error in errors))
        self.assertTrue(any("Unknown related item" in error for error in errors))
        self.assertTrue(any("pending" in error for error in errors))

    def test_warns_for_previous_versions_without_reviews(self) -> None:
        for version in ("1.0", "1.1", "1.2"):
            with self.subTest(version=version):
                errors, warnings = self._validate({"schema_version": version})
                self.assertEqual(errors, [])
                self.assertTrue(any("not verifiable" in warning for warning in warnings))

    def test_rejects_malformed_or_ambiguous_json(self) -> None:
        for text in (
            "No JSON block",
            "```json\n{}\n```\n```json\n{}\n```",
            '```json\n{"schema_version": "1.2", "schema_version": "1.3"}\n```',
            '```json\n{"schema_version": "1.3", "value": NaN}\n```',
        ):
            with self.subTest(text=text):
                errors, _ = validate_instruction_reviews(text, self.root)
                self.assertTrue(errors)

    def test_rejects_non_string_version_and_status(self) -> None:
        errors, _ = self._validate({"schema_version": []})
        self.assertTrue(any("Unsupported schema version" in error for error in errors))
        self.document["status"] = []
        errors, _ = self._validate(self.document)
        self.assertTrue(any("Discovery status" in error for error in errors))

    def test_published_example_passes_cli_validation(self) -> None:
        repository = Path(__file__).resolve().parents[1]
        contract = repository / ".github" / "skills" / "agentic-software-delivery" / "references" / "discovery-contract.md"
        content = contract.read_text(encoding="utf-8")
        blocks = re.findall(r"```json\n(.*?)\n```", content, re.DOTALL)
        example = json.loads(blocks[0])
        self.assertEqual(example["schema_version"], "1.3")
        path = self.root / "example.md"
        path.write_text(f"```json\n{blocks[0]}\n```\n", encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(repository / "scripts" / "validate_discovery.py"), str(path)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("structurally valid", result.stdout)

    def test_published_refactoring_example_passes_cli_validation(self) -> None:
        repository = Path(__file__).resolve().parents[1]
        contract = repository / ".github" / "skills" / "agentic-software-delivery" / "references" / "discovery-contract.md"
        blocks = re.findall(r"```json\n(.*?)\n```", contract.read_text(encoding="utf-8"), re.DOTALL)
        document = json.loads(blocks[0])
        refactoring = next(
            item for item in map(json.loads, blocks) if item.get("work_type") == "refactor"
        )
        document.update(refactoring)
        path = self.root / "example.md"
        path.write_text(f"```json\n{json.dumps(document)}\n```\n", encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(repository / "scripts" / "validate_discovery.py"), str(path)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_cli_warns_for_legacy_and_fails_for_incomplete_reviews(self) -> None:
        repository = Path(__file__).resolve().parents[1]
        script = repository / "scripts" / "validate_discovery.py"
        path = self.root / "example.md"
        for document, expected_code, message in (
            ({"schema_version": "1.2"}, 0, "not verifiable"),
            (
                {
                    "schema_version": "1.3",
                    "status": "approved",
                    "requirements": [],
                    "decisions": [],
                    "instruction_reviews": [],
                },
                1,
                "Missing instruction review",
            ),
        ):
            with self.subTest(document=document):
                path.write_text(f"```json\n{json.dumps(document)}\n```\n", encoding="utf-8")
                result = subprocess.run(
                    [sys.executable, str(script), str(path)],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(result.returncode, expected_code)
                self.assertIn(message, result.stderr)


if __name__ == "__main__":
    unittest.main()
