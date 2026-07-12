# ShopWave - Sprint 1 Plan

## Metadata
- **Version**: 1.0
- **Author**: Sam Patel (Project Manager)
- **Date**: 2026-01-15
- **Sprint**: Sprint 1
- **Duration**: Feb 3 - Feb 14, 2026 (2 weeks)
- **Status**: Approved

## Sprint Goal

**Sprint Goal**: Set up development environment, implement user authentication, and build product catalog

**Business Value**: Establish foundation for the platform and enable product discovery

## Sprint Backlog

### User Stories

| ID | Title | Priority | Story Points | Assignee | Status |
|----|-------|----------|--------------|----------|--------|
| US-001 | User registration | High | 5 | Riley Chen | ☐ To Do |
| US-002 | User login | High | 3 | Riley Chen | ☐ To Do |
| US-003 | Product catalog | High | 8 | Riley Chen | ☐ To Do |
| US-004 | Product detail | High | 5 | Riley Chen | ☐ To Do |
| US-005 | Artisan profiles | Medium | 5 | Riley Chen | ☐ To Do |

**Total Story Points**: 26
**Team Velocity**: 25 points/sprint (estimated)

### Tasks

#### US-001: User Registration (5 points)

| Task ID | Description | Assignee | Estimated Hours | Status |
|---------|-------------|----------|-----------------|--------|
| T-001 | Create registration form (frontend) | Riley Chen | 4 | ☐ To Do |
| T-002 | Implement registration endpoint (backend) | Riley Chen | 3 | ☐ To Do |
| T-003 | Add password validation | Riley Chen | 2 | ☐ To Do |
| T-004 | Write unit tests | Riley Chen | 2 | ☐ To Do |
| T-005 | Write integration tests | Riley Chen | 2 | ☐ To Do |

#### US-002: User Login (3 points)

| Task ID | Description | Assignee | Estimated Hours | Status |
|---------|-------------|----------|-----------------|--------|
| T-006 | Create login form (frontend) | Riley Chen | 3 | ☐ To Do |
| T-007 | Implement login endpoint (backend) | Riley Chen | 2 | ☐ To Do |
| T-008 | Implement JWT token generation | Riley Chen | 2 | ☐ To Do |
| T-009 | Write unit tests | Riley Chen | 2 | ☐ To Do |

#### US-003: Product Catalog (8 points)

| Task ID | Description | Assignee | Estimated Hours | Status |
|---------|-------------|----------|-----------------|--------|
| T-010 | Create product listing page (frontend) | Riley Chen | 4 | ☐ To Do |
| T-011 | Implement product API (backend) | Riley Chen | 4 | ☐ To Do |
| T-012 | Add category filtering | Riley Chen | 3 | ☐ To Do |
| T-013 | Add search functionality | Riley Chen | 3 | ☐ To Do |
| T-014 | Add pagination | Riley Chen | 2 | ☐ To Do |
| T-015 | Write unit tests | Riley Chen | 2 | ☐ To Do |
| T-016 | Write integration tests | Riley Chen | 3 | ☐ To Do |

#### US-004: Product Detail (5 points)

| Task ID | Description | Assignee | Estimated Hours | Status |
|---------|-------------|----------|-----------------|--------|
| T-017 | Create product detail page (frontend) | Riley Chen | 4 | ☐ To Do |
| T-018 | Implement product detail API (backend) | Riley Chen | 2 | ☐ To Do |
| T-019 | Add image gallery | Riley Chen | 3 | ☐ To Do |
| T-020 | Add related products | Riley Chen | 2 | ☐ To Do |
| T-021 | Write unit tests | Riley Chen | 2 | ☐ To Do |

## Team Capacity

### Team Members

| Name | Role | Availability | Effective Capacity |
|------|------|--------------|-------------------|
| Riley Chen | Developer | 100% | 40 hours |
| Quinn Brooks | QA | 100% | 40 hours |
| Taylor Kim | Designer | 100% | 40 hours |

### Capacity Calculation

**Total Team Capacity**: 120 hours
**Meetings**: 16 hours (standup, planning, review, retro)
**Available Hours**: 104 hours

**Buffer**: 20% for unplanned work
**Effective Capacity**: 83 hours

## Sprint Timeline

### Week 1

| Day | Date | Activities | Milestones |
|-----|------|------------|------------|
| Mon | 2026-02-03 | Sprint planning | Sprint starts |
| Tue | 2026-02-04 | Development | - |
| Wed | 2026-02-05 | Development | Mid-sprint check |
| Thu | 2026-02-06 | Development | - |
| Fri | 2026-02-07 | Development | - |

### Week 2

| Day | Date | Activities | Milestones |
|-----|------|------------|------------|
| Mon | 2026-02-10 | Development | Feature freeze |
| Tue | 2026-02-11 | Testing | QA begins |
| Wed | 2026-02-12 | Bug fixes | - |
| Thu | 2026-02-13 | Bug fixes | Code freeze |
| Fri | 2026-02-14 | Sprint review | Sprint ends |

## Dependencies

### Internal Dependencies
- [Dependency 1: "Development environment setup"]
  - **Owner**: Morgan Lee
  - **Target Date**: 2026-02-02
  - **Status**: ☐ In Progress / ☐ Completed

### External Dependencies
- [Dependency 1: "Stripe test account"]
  - **Owner**: Alex Rivera
  - **Target Date**: 2026-02-03
  - **Status**: ☐ In Progress / ☐ Completed

## Risks

### Sprint Risks

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| Environment setup delays | Low | Medium | Prepare setup scripts | Morgan Lee |
| Design feedback delays | Medium | Low | Schedule design review early | Taylor Kim |

## Definition of Done

A user story is considered "Done" when:
- [ ] Code is implemented and reviewed
- [ ] Unit tests are written and passing (≥ 80% coverage)
- [ ] Integration tests are written and passing
- [ ] Code is merged to main branch
- [ ] QA testing is complete and passed
- [ ] Documentation is updated
- [ ] Product Owner has approved
- [ ] Feature is deployed to staging

## Sprint Ceremonies

### Sprint Planning
- **Date**: 2026-02-03 (Monday)
- **Duration**: 2 hours
- **Attendees**: Full team
- **Agenda**: Review backlog, select stories, break down tasks

### Daily Standup
- **Time**: 9:00 AM daily
- **Duration**: 15 minutes
- **Format**: What did I do yesterday? What will I do today? Any blockers?

### Sprint Review
- **Date**: 2026-02-14 (Friday)
- **Duration**: 1 hour
- **Attendees**: Team, stakeholders
- **Agenda**: Demo completed work, gather feedback

### Sprint Retrospective
- **Date**: 2026-02-14 (Friday)
- **Duration**: 1 hour
- **Attendees**: Team only
- **Agenda**: What went well? What didn't? What to improve?

## Metrics

### Sprint Metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Story Points Committed | 26 | - | 🟢 |
| Story Points Completed | 26 | - | 🟢 |
| Velocity | 25 | - | 🟢 |
| Burndown Rate | On track | - | 🟢 |
| Bug Count | < 5 | - | 🟢 |

## Impediments

### Current Impediments
- None

## Approval

- [ ] Sam Patel (Project Manager)
- [ ] Alex Rivera (Product Owner)
- [ ] Morgan Lee (Tech Lead)
- [ ] Riley Chen (Developer)
