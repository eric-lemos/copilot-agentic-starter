from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from validate_agentic_config import validate_workspace


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

    @staticmethod
    def _write(root: Path, relative_path: str, content: str) -> None:
        path = root / Path(relative_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
