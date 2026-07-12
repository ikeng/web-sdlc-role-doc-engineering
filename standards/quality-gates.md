# Quality Gates

## Purpose

This document defines quality gates - checkpoints that must be passed before moving to the next phase of the SDLC. Quality gates ensure artifacts meet required standards and prevent issues from propagating.

## Quality Gate Overview

```
Research → Ideate → Plan → Execute → Optimize → Review
    ↓         ↓        ↓        ↓         ↓          ↓
  Gate 1   Gate 2   Gate 3   Gate 4   Gate 5    Gate 6
```

## Gate 1: Research Phase Exit

### Criteria
- [ ] Requirements are documented
- [ ] Completeness score ≥ 7/10
- [ ] Key objectives identified
- [ ] Success criteria defined
- [ ] Constraints identified
- [ ] Stakeholders identified

### Review Process
- Author: [Role]
- Reviewer: [Role]
- Approval: [Role]

### Exit Conditions
All criteria must be met before proceeding to Ideate phase.

---

## Gate 2: Ideate Phase Exit

### Criteria
- [ ] At least 2 solutions proposed
- [ ] Pros/cons evaluated for each
- [ ] Recommendation provided
- [ ] Trade-offs documented
- [ ] Solution aligns with requirements

### Review Process
- Author: [Role]
- Reviewer: [Role]
- Approval: [Role]

### Exit Conditions
All criteria must be met before proceeding to Plan phase.

---

## Gate 3: Plan Phase Exit

### Criteria
- [ ] Solution broken into atomic steps
- [ ] File structure defined
- [ ] Functions/classes identified
- [ ] Expected results defined
- [ ] Timeline estimated
- [ ] Risks identified
- [ ] User approval obtained

### Review Process
- Author: [Role]
- Reviewer: [Role]
- Approval: [Role]

### Exit Conditions
All criteria must be met and user must approve plan before proceeding to Execute phase.

---

## Gate 4: Execute Phase Exit

### Criteria
- [ ] All planned steps completed
- [ ] Code compiles/builds successfully
- [ ] Tests pass (unit, integration)
- [ ] No critical bugs
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] Quality standards met

### Review Process
- Author: [Role]
- Reviewer: [Role]
- Approval: [Role]

### Exit Conditions
All criteria must be met before proceeding to Optimize phase.

---

## Gate 5: Optimize Phase Exit

### Criteria
- [ ] Code review completed
- [ ] Redundant code identified and removed
- [ ] Performance issues addressed
- [ ] Security issues addressed
- [ ] Code quality improved
- [ ] No new bugs introduced

### Review Process
- Author: [Role]
- Reviewer: [Role]
- Approval: [Role]

### Exit Conditions
All criteria must be met before proceeding to Review phase.

---

## Gate 6: Review Phase Exit

### Criteria
- [ ] All deliverables completed
- [ ] All quality gates passed
- [ ] Requirements met
- [ ] User acceptance obtained
- [ ] Documentation complete
- [ ] Lessons learned documented

### Review Process
- Author: [Role]
- Reviewer: [Role]
- Approval: [Role]

### Exit Conditions
All criteria must be met before project completion.

---

## Artifact Quality Gates

### Requirements Document

**Quality Gates**:
- [ ] All requirements are numbered and traceable
- [ ] Functional and non-functional requirements are separated
- [ ] Requirements are testable and unambiguous
- [ ] Stakeholders have reviewed and approved
- [ ] Change control process is defined

**Owner**: Business Analyst
**Reviewer**: Product Owner, Tech Lead

---

### Architecture Document

**Quality Gates**:
- [ ] Architecture meets all requirements
- [ ] Scalability and performance are addressed
- [ ] Security considerations are documented
- [ ] ADRs are documented for major decisions
- [ ] Stakeholders have reviewed and approved

**Owner**: Solution Architect
**Reviewer**: Tech Lead, Security Engineer, DevOps Engineer

---

### User Stories

**Quality Gates**:
- [ ] All stories follow user story format
- [ ] Acceptance criteria are testable
- [ ] Stories are independently deliverable
- [ ] PO has reviewed and approved
- [ ] Estimates are provided

**Owner**: Product Owner
**Reviewer**: Tech Lead, QA Engineer

---

### Test Plan

**Quality Gates**:
- [ ] All testing types are covered
- [ ] Test environment is defined
- [ ] Automation strategy is clear
- [ ] Entry/exit criteria are measurable
- [ ] Team has reviewed and approved

**Owner**: QA Engineer
**Reviewer**: Tech Lead, Product Owner

---

### Code

**Quality Gates**:
- [ ] Code passes linting
- [ ] All tests pass
- [ ] Code coverage meets threshold (80%)
- [ ] No security vulnerabilities
- [ ] Code reviewed and approved
- [ ] Documentation complete

**Owner**: Developer
**Reviewer**: Tech Lead

---

## Phase Transition Criteria

### Product → Analysis
- [ ] Product vision is approved
- [ ] Product backlog is prioritized
- [ ] User stories are defined
- [ ] Acceptance criteria are documented

### Analysis → Design
- [ ] Requirements spec is approved
- [ ] Use cases are documented
- [ ] Business rules are defined
- [ ] Traceability matrix is complete

### Design → Architecture
- [ ] Wireframes are approved
- [ ] UI spec is complete
- [ ] Design system is defined
- [ ] Accessibility requirements are documented

### Architecture → Development
- [ ] Architecture document is approved
- [ ] Tech stack is selected
- [ ] API design is documented
- [ ] Security requirements are defined

### Development → Quality
- [ ] Code standards are defined
- [ ] Code is implemented and reviewed
- [ ] Unit tests pass
- [ ] Integration tests pass

### Quality → Deployment
- [ ] Test plan is approved
- [ ] Test cases are executed
- [ ] Quality metrics meet targets
- [ ] All critical bugs are fixed

### Deployment → Project
- [ ] Deployment plan is approved
- [ ] CI/CD pipeline is configured
- [ ] Runbook is complete
- [ ] Monitoring is set up

### All Phases → Security
- [ ] Security requirements are documented
- [ ] Threat model is complete
- [ ] Security checklist is approved
- [ ] Security testing is passed

## Quality Metrics

### Tracking Metrics
- Requirements coverage: % of requirements implemented
- Test coverage: % of code covered by tests
- Defect density: Bugs per KLOC
- Defect escape rate: Bugs found after release
- Review coverage: % of code reviewed
- Documentation coverage: % of artifacts documented

### Quality Targets
- Test coverage: ≥ 80%
- Code review coverage: 100%
- Documentation coverage: 100%
- Critical bugs: 0 at release
- High bugs: < 5 at release

## Escalation

### When to Escalate
- Quality gate cannot be passed
- Critical issues discovered
- Timeline/budget constraints prevent meeting criteria
- Stakeholder disagreement

### Escalation Path
1. Discuss with team lead
2. Escalate to project manager
3. Escalate to product owner
4. Final decision by steering committee

## Approval

- [ ] Tech Lead
- [ ] QA Engineer
- [ ] Project Manager
- [ ] Product Owner
