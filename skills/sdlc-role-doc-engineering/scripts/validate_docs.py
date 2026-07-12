#!/usr/bin/env python3
"""Validate SDLC role doc engineering artifacts."""

import sys
from pathlib import Path


def check_role_files(project_root: Path) -> list:
    issues = []
    roles_dir = project_root / "examples" / "shopwave" / "roles"
    if not roles_dir.exists():
        issues.append(f"Missing roles directory: {roles_dir}")
        return issues

    expected_sections = [
        "Role Overview",
        "Business Context",
        "Technical Scope",
        "Skill / Tool Mapping",
        "Function List",
        "Quality Standards",
        "Validation Checklist",
        "Approval",
    ]

    for md in roles_dir.glob("*.md"):
        text = md.read_text()
        missing = [s for s in expected_sections if s not in text]
        if missing:
            issues.append(f"{md.name}: missing sections {missing}")
    return issues


def check_feature_details(project_root: Path) -> list:
    issues = []
    doc = project_root / "examples" / "shopwave" / "deliverables" / "product" / "feature-details.md"
    if not doc.exists():
        issues.append(f"Missing feature details: {doc}")
        return issues

    text = doc.read_text()
    required = ["Normal Flow", "Edge Cases", "Exception Paths", "Downstream Impacts"]
    for section in required:
        if section not in text:
            issues.append(f"feature-details.md: missing section '{section}'")
    return issues


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_docs.py <project_root>")
        return 2
    project_root = Path(sys.argv[1])
    issues = []
    issues.extend(check_role_files(project_root))
    issues.extend(check_feature_details(project_root))

    if issues:
        print("Validation issues:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
