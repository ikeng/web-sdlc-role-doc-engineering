# ShopWave - QA Engineer Role

## Role Overview

**Name**: Quinn Brooks
**Email**: quinn@shopwave.com
**Responsibilities**: Ensure product quality through testing, define quality standards, automate testing where possible.

## Key Focus Areas

1. **Test Coverage**: Comprehensive unit, integration, and E2E tests
2. **Quality Metrics**: Track and report quality metrics
3. **Bug Detection**: Find and document bugs early
4. **Automation**: Automate repetitive testing tasks

## Business Context

- **Industry/Domain**: Independent e-commerce storefront for handcrafted home goods
- **Project Example**: ShopWave MVP catalog, cart, checkout, and admin flows
- **Business Goals Supported**: Reliable checkout, low defect rate, fast release confidence
- **Stakeholder Value**: Prevents customer-facing failures and protects conversion

## Technical Scope

- **Primary Tech Stack Interactions**: React frontend, Express backend, PostgreSQL, Stripe
- **Key Systems/Services**: CI, staging, defect tracker, Lighthouse, OWASP ZAP
- **Data Domains**: Test cases, defects, coverage, performance results
- **Compliance/Security Boundaries**: Test data handling, access to staging

## Skill / Tool Mapping

- **MCP Skills**:
  - `testing-patterns` — for test strategy and test design
  - `test-driven-development` — for TDD workflows where applicable
  - `frontend-testing` — for UI and browser-level validation
- **CLI/Runtime Tools**: Jest, Playwright, Lighthouse, GitHub Actions
- **When to Use Each**: Test planning, automation, regression, and release gating

## Function List

| Function | Inputs | Outputs | Trigger/Cadence |
|----------|--------|---------|-----------------|
| Create test plan | Requirements, risks | `test-plan.md` | Per release or epic |
| Write test cases | Requirements, designs | `test-cases.md` | Per feature |
| Execute tests | Build, environments | Test results, defects | Per build/release |
| Report quality metrics | Test data, defects | `quality-metrics.md` | Sprint / release |
| Drive test automation | Manual tests, pain points | Automated suites | Ongoing |

## Quality Standards

- **Definition of Done**:
  - Test plan is approved
  - Critical paths are automated or covered
  - Defects are triaged and tracked
  - Release criteria are met
- **Review Criteria**:
  - Coverage of requirements and edge cases
  - Repeatability and reliability of tests
- **Metrics/Targets**:
  - Test pass rate
  - Defect density
  - Automation coverage
  - Escape rate

## Validation Checklist

- **Logic Consistency**:
  - [ ] Test cases map to requirements and acceptance criteria
  - [ ] Entry/exit criteria are consistent with release needs
- **Technical Accuracy**:
  - [ ] Test environments match target stack
  - [ ] Automation is maintainable
- **Business Alignment**:
  - [ ] Critical user journeys are tested first
  - [ ] Risk-based prioritization is applied
- **Tooling/Skill Coverage**:
  - [ ] Testing and QA skills/tools are mapped
  - [ ] Reporting workflow is clear

## Output Files for ShopWave

### Test Plan
**File**: `deliverables/quality/test-plan.md`

**Testing Strategy**:
- Unit tests: Jest + React Testing Library
- Integration tests: Jest + Supertest
- E2E tests: Playwright
- Performance: Lighthouse CI
- Security: OWASP ZAP

**Test Schedule**:
- Sprint 1: Auth, product catalog tests
- Sprint 2: Cart, checkout tests
- Sprint 3: Order management, admin tests

### Test Cases
**File**: `deliverables/quality/test-cases.md`

**Example Test Cases**:
- TC-001: User registration with valid data
- TC-002: User login with invalid password
- TC-003: Add product to cart
- TC-004: Complete checkout with Stripe
- TC-005: View order history

### Quality Metrics
**File**: `deliverables/quality/quality-metrics.md`

**Targets**:
- Code coverage: ≥ 80%
- Test pass rate: ≥ 95%
- Critical bugs: 0 at release
- Performance: Page load < 2s

## Current Focus

**Sprint 1**: Set up test infrastructure, write auth tests
**Sprint 2**: Write cart and checkout tests
**Sprint 3**: E2E tests, performance testing

## Tools

- Jest for unit/integration tests
- Playwright for E2E tests
- Cypress for component tests
- GitHub Actions for CI/CD
- Lighthouse for performance

## Approval

- [ ] Quinn Brooks (QA Engineer)
- [ ] Morgan Lee (Tech Lead)
