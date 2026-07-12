# Validation Checklist

## Document-level checks
- [ ] Each role file includes the 8 standard sections from the enhancement template
- [ ] Role outputs reference existing deliverable files in the project structure
- [ ] Interaction patterns are consistent with Agile/Scrum flow
- [ ] Review cycles are realistic for the role

## Content checks
- [ ] Business context is project-specific, not generic
- [ ] Technical scope matches the documented tech stack
- [ ] Skill/tool mappings are relevant and complete
- [ ] Function list uses the inputs/outputs/trigger format
- [ ] Quality standards include measurable metrics
- [ ] Validation checklist covers logic, technical, business, and tooling

## Cross-role checks
- [ ] No overlapping or conflicting responsibilities
- [ ] Handoffs between roles are clearly documented
- [ ] Approval chains are consistent

## Downstream-impact checks (feature-details)
- [ ] Normal flow is sequential and complete
- [ ] Edge cases cover boundary conditions
- [ ] Exception paths cover failures and recovery
- [ ] Tech Implementation, QA, Security, UX, and DevOps impacts are all present
- [ ] API endpoints and components align with architecture

## Automation
- Run `python scripts/validate_docs.py <project_root>` for structure validation.
