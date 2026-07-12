# Code Review Checklist

## Metadata
- **Version**: 1.0
- **Author**: Tech Lead
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Status**: Approved

## Purpose

This checklist ensures code reviews are thorough and consistent. Reviewers should go through each item and provide feedback.

## Review Process

1. **Understand the context**: Read PR description and related issues
2. **Run the code**: Test the changes locally if possible
3. **Review systematically**: Go through this checklist
4. **Provide feedback**: Leave constructive comments
5. **Approve or request changes**: Make a decision

## Code Quality

### Code Style
- [ ] Code follows project style guidelines
- [ ] No linting errors
- [ ] Consistent formatting
- [ ] No commented-out code
- [ ] No console.log statements (use logger)
- [ ] No hardcoded values (use constants)

### Code Structure
- [ ] Functions are small and focused (< 50 lines)
- [ ] Single responsibility principle followed
- [ ] No duplicate code (DRY)
- [ ] Proper use of design patterns
- [ ] No deep nesting (> 3 levels)

### Naming
- [ ] Variables have descriptive names
- [ ] Functions have verb-noun names (e.g., `getUser()`)
- [ ] Classes have noun names (e.g., `UserService`)
- [ ] No abbreviations unless universally understood
- [ ] Consistent casing conventions

## Functionality

### Correctness
- [ ] Code does what it's supposed to do
- [ ] Logic is correct
- [ ] Edge cases are handled
- [ ] Error cases are handled
- [ ] No off-by-one errors

### Requirements
- [ ] Implements the requirements
- [ ] Meets acceptance criteria
- [ ] No missing functionality
- [ ] No extra functionality (YAGNI)

### Business Logic
- [ ] Business rules are correctly implemented
- [ ] Calculations are accurate
- [ ] Data transformations are correct
- [ ] State management is correct

## Testing

### Test Coverage
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] E2E tests added/updated (if applicable)
- [ ] Test coverage meets threshold (80%+)
- [ ] All tests pass

### Test Quality
- [ ] Tests cover happy path
- [ ] Tests cover edge cases
- [ ] Tests cover error cases
- [ ] Tests are independent
- [ ] Tests are deterministic (no flaky tests)
- [ ] Test names are descriptive

## Security

### Input Validation
- [ ] All user input is validated
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] File uploads are validated
- [ ] API inputs are sanitized

### Authentication & Authorization
- [ ] Authentication is implemented correctly
- [ ] Authorization checks are in place
- [ ] Sensitive operations require authentication
- [ ] Passwords are hashed (bcrypt)
- [ ] JWT tokens are properly validated

### Data Protection
- [ ] No sensitive data in logs
- [ ] No secrets in code
- [ ] Environment variables used for configuration
- [ ] HTTPS enforced in production
- [ ] CORS configured correctly

## Performance

### Efficiency
- [ ] No unnecessary API calls
- [ ] No N+1 query problems
- [ ] Database queries are optimized
- [ ] Proper use of caching
- [ ] No memory leaks
- [ ] No unnecessary re-renders (frontend)

### Scalability
- [ ] Code can handle expected load
- [ ] No blocking operations in hot paths
- [ ] Proper use of async/await
- [ ] Pagination implemented for lists
- [ ] Images/assets are optimized

## Error Handling

### Error Management
- [ ] Errors are caught and handled
- [ ] Error messages are meaningful
- [ ] Errors are logged with context
- [ ] No silent failures
- [ ] User-friendly error messages

### Edge Cases
- [ ] Null/undefined values handled
- [ ] Empty arrays/objects handled
- [ ] Network failures handled
- [ ] Timeouts handled
- [ ] Retry logic implemented where needed

## Documentation

### Code Comments
- [ ] Complex logic is explained
- [ ] Non-obvious decisions are documented
- [ ] Public APIs are documented (JSDoc)
- [ ] No unnecessary comments (code should be self-explanatory)

### Documentation Updates
- [ ] README updated (if needed)
- [ ] API documentation updated
- [ ] Architecture diagrams updated (if needed)
- [ ] Changelog updated

## Dependencies

### New Dependencies
- [ ] New dependencies are necessary
- [ ] Dependencies are well-maintained
- [ ] No duplicate functionality with existing dependencies
- [ ] License is compatible with project
- [ ] Bundle size impact is acceptable

### Dependency Updates
- [ ] Breaking changes are handled
- [ ] Migration guide followed
- [ ] Tests pass after update

## Backward Compatibility

### Breaking Changes
- [ ] Breaking changes are documented
- [ ] Migration path is provided
- [ ] Version bump is appropriate
- [ ] Deprecation warnings added (if applicable)

### API Contracts
- [ ] API responses are consistent
- [ ] API contracts are not broken
- [ ] Versioning strategy followed

## Review Feedback Guidelines

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

## Common Review Findings

### Code Quality
- **Issue**: Function too long
- **Suggestion**: Break into smaller functions

- **Issue**: Deeply nested code
- **Suggestion**: Use early returns, extract to functions

### Security
- **Issue**: SQL injection vulnerability
- **Suggestion**: Use parameterized queries

- **Issue**: Hardcoded credentials
- **Suggestion**: Use environment variables

### Performance
- **Issue**: N+1 query problem
- **Suggestion**: Use eager loading or batch queries

- **Issue**: Unnecessary re-renders
- **Suggestion**: Use React.memo or useMemo

## Approval

- [ ] Tech Lead
- [ ] All Reviewers
