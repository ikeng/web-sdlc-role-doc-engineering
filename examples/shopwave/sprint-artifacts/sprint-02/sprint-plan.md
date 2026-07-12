# ShopWave - Sprint 2 Plan

## Metadata
- **Version**: 1.0
- **Author**: Sam Patel (Project Manager)
- **Date**: 2026-01-15
- **Sprint**: Sprint 2
- **Duration**: Feb 17 - Feb 28, 2026 (2 weeks)
- **Status**: Approved

## Sprint Goal

**Sprint Goal**: Implement shopping cart, checkout with Stripe, and order creation

**Business Value**: Enable customers to complete purchases and generate revenue

## Sprint Backlog

### User Stories

| ID | Title | Priority | Story Points | Assignee | Status |
|----|-------|----------|--------------|----------|--------|
| US-006 | Shopping cart | High | 8 | Riley Chen | ☐ To Do |
| US-007 | Checkout flow | High | 13 | Riley Chen | ☐ To Do |
| US-008 | Order confirmation | High | 3 | Riley Chen | ☐ To Do |
| US-009 | Order tracking | High | 5 | Riley Chen | ☐ To Do |

**Total Story Points**: 29
**Team Velocity**: 25 points/sprint (estimated)

### Tasks

#### US-006: Shopping Cart (8 points)

| Task ID | Description | Assignee | Hours | Status |
|---------|-------------|----------|-------|--------|
| T-022 | Implement cart service (backend) | Riley Chen | 4 | ☐ |
| T-023 | Create cart drawer UI (frontend) | Riley Chen | 4 | ☐ |
| T-024 | Add to cart functionality | Riley Chen | 3 | ☐ |
| T-025 | Update quantity functionality | Riley Chen | 2 | ☐ |
| T-026 | Remove item functionality | Riley Chen | 2 | ☐ |
| T-027 | Write unit tests | Riley Chen | 2 | ☐ |
| T-028 | Write integration tests | Riley Chen | 3 | ☐ |

#### US-007: Checkout Flow (13 points)

| Task ID | Description | Assignee | Hours | Status |
|---------|-------------|----------|-------|--------|
| T-029 | Create checkout page (frontend) | Riley Chen | 4 | ☐ |
| T-030 | Implement shipping address form | Riley Chen | 3 | ☐ |
| T-031 | Integrate Stripe payment | Riley Chen | 5 | ☐ |
| T-032 | Implement order creation (backend) | Riley Chen | 5 | ☐ |
| T-033 | Add order confirmation page | Riley Chen | 2 | ☐ |
| T-034 | Send confirmation email | Riley Chen | 2 | ☐ |
| T-035 | Write unit tests | Riley Chen | 3 | ☐ |
| T-036 | Write integration tests | Riley Chen | 4 | ☐ |

#### US-008: Order Confirmation (3 points)

| Task ID | Description | Assignee | Hours | Status |
|---------|-------------|----------|-------|--------|
| T-037 | Create confirmation page | Riley Chen | 2 | ☐ |
| T-038 | Send confirmation email | Riley Chen | 2 | ☐ |
| T-039 | Write tests | Riley Chen | 1 | ☐ |

#### US-009: Order Tracking (5 points)

| Task ID | Description | Assignee | Hours | Status |
|---------|-------------|----------|-------|--------|
| T-040 | Create order history page | Riley Chen | 3 | ☐ |
| T-041 | Implement order tracking API | Riley Chen | 3 | ☐ |
| T-042 | Add tracking number display | Riley Chen | 2 | ☐ |
| T-043 | Write tests | Riley Chen | 2 | ☐ |

## Team Capacity

### Team Members

| Name | Role | Availability | Effective Capacity |
|------|------|--------------|-------------------|
| Riley Chen | Developer | 100% | 40 hours |
| Quinn Brooks | QA | 100% | 40 hours |
| Taylor Kim | Designer | 50% (other project) | 20 hours |

### Capacity Calculation

**Total Team Capacity**: 100 hours
**Meetings**: 16 hours
**Available Hours**: 84 hours

**Buffer**: 20%
**Effective Capacity**: 67 hours

## Sprint Timeline

### Week 1

| Day | Date | Activities | Milestones |
|-----|------|------------|------------|
| Mon | 2026-02-17 | Sprint planning | Sprint starts |
| Tue | 2026-02-18 | Development | - |
| Wed | 2026-02-19 | Development | Mid-sprint check |
| Thu | 2026-02-20 | Development | - |
| Fri | 2026-02-21 | Development | - |

### Week 2

| Day | Date | Activities | Milestones |
|-----|------|------------|------------|
| Mon | 2026-02-24 | Development | Feature freeze |
| Tue | 2026-02-25 | Testing | QA begins |
| Wed | 2026-02-26 | Bug fixes | - |
| Thu | 2026-02-27 | Bug fixes | Code freeze |
| Fri | 2026-02-28 | Sprint review | Sprint ends |

## Dependencies

### Internal Dependencies
- [Dependency 1: "Sprint 1 features complete"]
  - **Owner**: Riley Chen
  - **Target Date**: 2026-02-14
  - **Status**: ☐ In Progress / ☐ Completed

### External Dependencies
- [Dependency 1: "Stripe test account"]
  - **Owner**: Alex Rivera
  - **Target Date**: 2026-02-16
  - **Status**: ☐ In Progress / ☐ Completed

## Risks

### Sprint Risks

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| Stripe integration issues | Medium | High | Early integration, test mode | Riley Chen |
| Checkout flow complexity | Medium | Medium | Break into smaller tasks | Sam Patel |

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
- **Date**: 2026-02-17 (Monday)
- **Duration**: 2 hours
- **Attendees**: Full team

### Daily Standup
- **Time**: 9:00 AM daily
- **Duration**: 15 minutes

### Sprint Review
- **Date**: 2026-02-28 (Friday)
- **Duration**: 1 hour
- **Attendees**: Team, stakeholders

### Sprint Retrospective
- **Date**: 2026-02-28 (Friday)
- **Duration**: 1 hour
- **Attendees**: Team only

## Metrics

### Sprint Metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Story Points Committed | 29 | - | 🟢 |
| Story Points Completed | 29 | - | 🟢 |
| Velocity | 25 | - | 🟢 |
| Bug Count | < 5 | - | 🟢 |

## Impediments

### Current Impediments
- None

## Approval

- [ ] Sam Patel (Project Manager)
- [ ] Alex Rivera (Product Owner)
- [ ] Morgan Lee (Tech Lead)
- [ ] Riley Chen (Developer)
