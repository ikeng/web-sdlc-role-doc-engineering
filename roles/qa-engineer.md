# QA Engineer

## Role Overview

The QA Engineer ensures product quality through comprehensive testing strategies, test automation, and quality metrics reporting.

## Responsibilities

- Create and execute test plans
- Write automated test scripts
- Perform manual testing when needed
- Report and track bugs
- Define quality metrics and KPIs
- Conduct regression testing
- Participate in requirement reviews
- Ensure accessibility and usability standards
- Collaborate with developers on testability

## Output Files

| File | Phase | Description |
|------|-------|-------------|
| `test-plan.md` | Quality | Comprehensive test strategy and plan |
| `test-cases.md` | Quality | Detailed test cases and scenarios |
| `quality-metrics.md` | Quality | Quality metrics and reporting |

## File Dimensions

### test-plan.md

**Purpose**: Define the overall testing strategy and approach.

**Required Sections**:
- Document metadata (version, authors, date)
- Testing objectives and scope
- Testing types (unit, integration, E2E, performance, security)
- Test environment setup
- Test data management
- Automation strategy
- Testing tools and frameworks
- Entry and exit criteria
- Risk assessment
- Schedule and milestones

**Quality Gates**:
- [ ] All testing types are covered
- [ ] Test environment is defined
- [ ] Automation strategy is clear
- [ ] Entry/exit criteria are measurable
- [ ] Team has reviewed and approved

### test-cases.md

**Purpose**: Detailed test cases for features and scenarios.

**Required Sections**:
- Test case ID and title
- Test type (functional, integration, E2E)
- Preconditions
- Test steps
- Expected results
- Actual results
- Status (Pass/Fail/Blocked)
- Priority
- Related requirements
- Notes and attachments

**Quality Gates**:
- [ ] All requirements are covered
- [ ] Test cases are clear and repeatable
- [ ] Edge cases are included
- [ ] Test data is defined
- [ ] Test cases are automated where possible

### quality-metrics.md

**Purpose**: Track and report quality metrics for the team.

**Required Sections**:
- Test execution summary
- Pass/fail rates
- Code coverage metrics
- Bug statistics (open, closed, severity)
- Test automation coverage
- Performance metrics
- Accessibility compliance
- Quality trends over time
- Recommendations for improvement

**Quality Gates**:
- [ ] Metrics are accurate and up-to-date
- [ ] Trends are identified
- [ ] Action items are defined
- [ ] Report is shared with stakeholders

## Interaction Patterns

**Inputs From**:
- Business Analyst (requirements)
- Full-stack Developer (builds)
- UX Designer (design specs)

**Outputs To**:
- Full-stack Developer (bug reports)
- Project Manager (quality status)
- Tech Lead (quality metrics)

**Review Cycle**:
- Sprint: Test execution and reporting
- Release: Quality gate review
- Monthly: Quality metrics review

## Tools & Templates

- Test automation frameworks (Cypress, Selenium, Playwright)
- Bug tracking (Jira, Linear)
- Test management tools
- Performance testing tools (JMeter, k6)
