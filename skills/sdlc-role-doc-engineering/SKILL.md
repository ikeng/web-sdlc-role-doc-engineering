---
name: sdlc-role-doc-engineering
description: Role-first SDLC document engineering skill. Use when (1) defining or enriching SDLC role agents, (2) generating role-specific deliverables from templates, (3) mapping business context, tech stack, skills/tools to roles, (4) validating and auditing generated documents, or (5) standardizing cross-role document quality. NOT for generic document writing without role/template context.
---

# SDLC Role Doc Engineering

## Quick start

Use this skill to turn role definitions into complete, role-specific document sets:
1. Define or enrich role agents with business context, scenarios, tech stack, skills/tools, function list, and validation criteria.
2. Map each role to its deliverables using the role matrix and templates.
3. Generate role-specific documents with consistent structure.
4. Run validation and produce an audit trail.

## Core workflow

### 1. Role definition / enrichment
- Load `assets/role-definition-template.md` for baseline structure.
- Load `assets/role-enhancement-template.md` for business/tech/skill enrichment.
- For each role, capture:
  - Business context: industry, project example, goals, stakeholder value
  - Technical scope: stack interactions, key systems, data domains, compliance boundaries
  - Skill/tool mapping: MCP skills, CLI/runtime tools, when to use each
  - Function list: inputs, outputs, trigger/cadence
  - Quality standards: DoD, review criteria, metrics/targets
  - Validation checklist: logic, technical, business, tooling checks
  - Approval sign-off

### 2. Deliverable mapping
- Load `references/role-matrix.md` to map roles to deliverables.
- For each role, identify required outputs and select the appropriate template from `assets/deliverable-templates/`.
- Reuse existing project artifacts when available; do not duplicate.

### 3. Document generation
- Apply the selected template to each role's context.
- Ensure outputs are role-specific, not generic.
- Keep names, responsibilities, and approval sections aligned with the enhanced role definition.

### 4. Validation & audit
- Load `references/validation-checklist.md` for cross-cutting checks.
- Run `scripts/validate_docs.py` against generated documents when possible.
- Record results in `examples/<project>/audit/validation-report.md`.
- Create `examples/<project>/audit/agent-role-audit.md` as the audit trail.

## Role matrix

See [references/role-matrix.md](references/role-matrix.md) for the canonical mapping of roles to deliverables.

## Templates

- [assets/role-definition-template.md](assets/role-definition-template.md)
- [assets/role-enhancement-template.md](assets/role-enhancement-template.md)
- [assets/deliverable-templates/](assets/deliverable-templates/)

## Validation

See [references/validation-checklist.md](references/validation-checklist.md).

Run `python scripts/validate_docs.py <project_root>` to perform automated structure checks.

## Audit

See [references/audit-procedures.md](references/audit-procedures.md).

## Output standards

- Use Markdown with clear section headings.
- Preserve existing role files; do not delete original content without explicit request.
- Keep skill under 500 lines; move detailed guides to `references/`.
