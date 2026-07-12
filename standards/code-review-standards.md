# Code Review Standards

## Purpose

This document defines code review standards and the review process to ensure code quality, maintainability, and consistency.

## Review Process

### 1. Author Preparation

Before requesting a review:
- [ ] Self-review the code
- [ ] Run linter and fix issues
- [ ] Run tests and ensure they pass
- [ ] Write/update tests for new functionality
- [ ] Update documentation if needed
- [ ] Write clear PR description

### 2. Review Request

- Request review from at least one team member
- For complex changes, request multiple reviewers
- Tag relevant team members (Tech Lead for architecture, QA for test coverage)

### 3. Reviewer Review

- Review within 24 hours
- Use the code review checklist
- Provide constructive feedback
- Approve or request changes

### 4. Author Response

- Address all review comments
- Push updates to the same branch
- Re-request review if significant changes

### 5. Approval & Merge

- At least one approval required
- All CI checks must pass
- Squash and merge to main

## Review Criteria

### Code Quality
- Code is readable and maintainable
- Functions are small and focused
- No code duplication
- Proper error handling
- No commented-out code

### Functionality
- Code does what it's supposed to do
- Edge cases are handled
- Error cases are handled
- Requirements are met

### Testing
- Tests are written for new functionality
- Tests cover edge cases
- Tests are clear and maintainable
- All tests pass

### Security
- No security vulnerabilities
- Input validation implemented
- No hardcoded secrets
- Proper authentication/authorization

### Performance
- No performance issues
- Efficient algorithms used
- No unnecessary API calls
- Database queries optimized

### Documentation
- Code is self-documenting
- Complex logic is commented
- Public APIs are documented
- README updated if needed

## Feedback Guidelines

### Providing Feedback

**Good Feedback**:
- ✅ "Consider using `Array.map()` here for better readability"
- ✅ "This could be optimized by caching the result"
- ✅ "Add error handling for the case when the API returns 404"
- ✅ "Great job handling the edge case!"

**Bad Feedback**:
- ❌ "This is wrong"
- ❌ "Rewrite this"
- ❌ "I don't like this"
- ❌ "Why did you do it this way?"

### Feedback Categories

**Critical (Must Fix)**:
- Security vulnerabilities
- Bugs that break functionality
- Performance issues
- Missing error handling

**Important (Should Fix)**:
- Code quality issues
- Missing tests
- Documentation gaps
- Best practice violations

**Nice-to-have (Could Fix)**:
- Code style suggestions
- Minor optimizations
- Alternative approaches

## Approval Criteria

Code is ready to merge when:
- [ ] All critical issues are addressed
- [ ] All important issues are addressed or discussed
- [ ] Tests pass (unit, integration, E2E)
- [ ] CI checks pass (lint, build, test)
- [ ] At least one reviewer approves
- [ ] No unresolved discussions

## Review Timeframe

- **Initial review**: Within 24 hours
- **Re-review**: Within 12 hours
- **Urgent fixes**: Within 4 hours

## Escalation

If review is blocked:
1. Discuss with reviewer directly
2. Escalate to Tech Lead if unresolved after 24 hours
3. Product Owner makes final decision if needed

## Metrics

Track these metrics:
- Review turnaround time
- Number of review cycles
- Comments per PR
- Approval rate

## Approval

- [ ] Tech Lead
- [ ] All Reviewers
