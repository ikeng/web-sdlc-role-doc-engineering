# Product Owner (PO)

## Role Overview

The Product Owner is responsible for defining the product vision, prioritizing the backlog, and ensuring the development team builds the right product for users.

## Responsibilities

- Define and communicate product vision and strategy
- Create and prioritize product backlog
- Write and refine user stories with acceptance criteria
- Define MVP features and release roadmap
- Collaborate with stakeholders on requirements
- Make final decisions on feature priorities
- Review and approve completed work
- Gather and analyze user feedback

## Output Files

| File | Phase | Description |
|------|-------|-------------|
| `product-vision.md` | Product | High-level product vision and goals |
| `product-backlog.md` | Product | Prioritized list of features and epics |
| `user-stories.md` | Product | Detailed user stories with acceptance criteria |
| `acceptance-criteria.md` | Product | Detailed acceptance criteria for features |

## File Dimensions

### product-vision.md

**Purpose**: Define the strategic direction and goals of the product.

**Required Sections**:
- Product name and tagline
- Vision statement (1-2 sentences)
- Target audience and user personas
- Core value proposition
- Success metrics (KPIs)
- Competitive landscape
- Release roadmap (high-level)
- Constraints and assumptions

**Quality Gates**:
- [ ] Vision is clear, concise, and inspiring
- [ ] Target audience is well-defined
- [ ] Success metrics are measurable
- [ ] Stakeholders have reviewed and approved

### product-backlog.md

**Purpose**: Maintain a prioritized list of all product features, epics, and user stories.

**Required Sections**:
- Epic list with descriptions
- User stories organized by epic
- Priority levels (High/Medium/Low)
- Story points estimates
- Dependencies between stories
- Sprint assignments
- Status tracking (To Do/In Progress/Done)

**Quality Gates**:
- [ ] All stories follow INVEST principles
- [ ] Priorities reflect business value
- [ ] Estimates are consistent and reviewed
- [ ] Dependencies are documented

### user-stories.md

**Purpose**: Detailed user stories with acceptance criteria for development.

**Required Sections**:
- Story ID and title
- User persona
- User story (As a... I want... So that...)
- Acceptance criteria (Given/When/Then format)
- Definition of Done
- Story points
- Priority
- Dependencies
- Notes and assumptions

**Quality Gates**:
- [ ] All stories follow user story format
- [ ] Acceptance criteria are testable
- [ ] Stories are independently deliverable
- [ ] PO has reviewed and approved

### acceptance-criteria.md

**Purpose**: Detailed acceptance criteria for complex features or epics.

**Required Sections**:
- Feature/epic name
- Business context and rationale
- Detailed acceptance scenarios
- Edge cases and error handling
- Non-functional requirements
- Acceptance test cases
- Sign-off criteria

**Quality Gates**:
- [ ] All scenarios are covered
- [ ] Edge cases are identified
- [ ] Non-functional requirements are specified
- [ ] Test cases are documented

## Interaction Patterns

**Inputs From**:
- Stakeholders (requirements, feedback)
- Business Analyst (business requirements)
- UX Designer (user research)

**Outputs To**:
- Business Analyst (prioritized features)
- UX Designer (feature requirements)
- Development Team (sprint backlog)

**Review Cycle**:
- Daily: Backlog refinement
- Weekly: Sprint planning and review
- Monthly: Roadmap review with stakeholders

## Tools & Templates

- Product management tools (Jira, Linear, Asana)
- User story templates
- Roadmap templates
- Prioritization frameworks (RICE, MoSCoW)
