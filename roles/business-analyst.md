# Business Analyst (BA)

## Role Overview

The Business Analyst bridges the gap between business stakeholders and the development team, ensuring requirements are clearly understood and documented.

## Responsibilities

- Gather and analyze business requirements
- Document functional and non-functional requirements
- Create use cases and user stories
- Facilitate requirements workshops and interviews
- Validate requirements with stakeholders
- Manage requirements changes and traceability
- Create process flow diagrams
- Support acceptance testing

## Output Files

| File | Phase | Description |
|------|-------|-------------|
| `requirements-spec.md` | Analysis | Detailed requirements specification |
| `use-case-diagram.md` | Analysis | Use case documentation and diagrams |
| `business-rules.md` | Analysis | Business rules and validation logic |

## File Dimensions

### requirements-spec.md

**Purpose**: Comprehensive documentation of all product requirements.

**Required Sections**:
- Document metadata (version, authors, date)
- Executive summary
- Scope definition (in-scope/out-of-scope)
- User personas and roles
- Functional requirements (numbered, traceable)
- Non-functional requirements (performance, security, usability)
- Assumptions and constraints
- Dependencies
- Acceptance criteria
- Glossary of terms

**Quality Gates**:
- [ ] All requirements are numbered and traceable
- [ ] Functional and non-functional requirements are separated
- [ ] Requirements are testable and unambiguous
- [ ] Stakeholders have reviewed and approved
- [ ] Change control process is defined

### use-case-diagram.md

**Purpose**: Document user interactions with the system through use cases.

**Required Sections**:
- Use case ID and name
- Actors involved
- Preconditions
- Postconditions
- Basic flow (happy path)
- Alternative flows
- Exception flows
- Business rules
- Related use cases
- Priority and complexity

**Quality Gates**:
- [ ] All actors are identified
- [ ] Flows are complete and unambiguous
- [ ] Edge cases are covered
- [ ] Use cases are testable

### business-rules.md

**Purpose**: Document business logic, constraints, and validation rules.

**Required Sections**:
- Rule ID and name
- Business context
- Rule definition (if-then format)
- Validation logic
- Error messages
- Priority and severity
- Dependencies on other rules
- Examples

**Quality Gates**:
- [ ] Rules are unambiguous and testable
- [ ] All edge cases are covered
- [ ] Rules are prioritized
- [ ] Business stakeholders have approved

## Interaction Patterns

**Inputs From**:
- Product Owner (prioritized features)
- Stakeholders (business needs)
- Users (feedback, pain points)

**Outputs To**:
- Product Owner (requirements clarification)
- UX Designer (user requirements)
- Solution Architect (functional requirements)
- Development Team (detailed specs)

**Review Cycle**:
- Weekly: Requirements review with stakeholders
- Sprint: Requirements refinement
- Release: Requirements sign-off

## Tools & Templates

- Requirements management tools (Confluence, Notion)
- Diagramming tools (Mermaid, Draw.io)
- Requirements traceability matrix
- Use case templates
