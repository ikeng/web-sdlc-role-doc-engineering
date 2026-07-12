# Audit Procedures

## Purpose
Create an auditable trail for role and document engineering work.

## Audit artifacts
- `examples/<project>/audit/validation-report.md` — validation results by role/file
- `examples/<project>/audit/agent-role-audit.md` — summary of enhancements and decisions

## Procedure
1. After enhancing role files, run structure and content validation.
2. Record any issues and resolutions in `validation-report.md`.
3. Summarize:
   - Files modified/created
   - Enhancement rationale
   - Validation results
   - Recommendations
4. Store both artifacts under `examples/<project>/audit/`.

## Usage
- Reference these artifacts during project reviews.
- Use as evidence that role definitions and deliverables were systematically reviewed.
