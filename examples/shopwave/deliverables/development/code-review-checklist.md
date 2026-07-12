# ShopWave - Code Review Checklist

## Metadata
- **Version**: 1.0
- **Author**: Morgan Lee (Tech Lead)
- **Date**: 2026-01-15
- **Project**: ShopWave
- **Status**: Approved

## Purpose

This checklist ensures code reviews are thorough and consistent for ShopWave.

## Review Process

1. Understand the context: Read PR description and related issues
2. Run the code: Test the changes locally if possible
3. Review systematically: Go through this checklist
4. Provide feedback: Leave constructive comments
5. Approve or request changes: Make a decision

## Code Quality

### Code Style
- [ ] Code follows project style guidelines
- [ ] No linting errors
- [ ] Consistent formatting
- [ ] No commented-out code
- [ ] No console.log statements
- [ ] No hardcoded values

### Code Structure
- [ ] Functions are small and focused (< 50 lines)
- [ ] Single responsibility principle followed
- [ ] No duplicate code (DRY)
- [ ] No deep nesting (> 3 levels)

### Naming
- [ ] Variables have descriptive names
- [ ] Functions have verb-noun names
- [ ] Classes have noun names
- [ ] Consistent casing conventions

## Functionality

### Correctness
- [ ] Code does what it's supposed to do
- [ ] Logic is correct
- [ ] Edge cases are handled
- [ ] Error cases are handled

### Requirements
- [ ] Implements the requirements
- [ ] Meets acceptance criteria
- [ ] No missing functionality

## Testing

### Test Coverage
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] E2E tests added/updated (if applicable)
- [ ] Test coverage meets threshold (80%)
- [ ] All tests pass

## Security

### Input Validation
- [ ] All user input is validated
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] File uploads validated (if applicable)

### Authentication & Authorization
- [ ] Authentication is implemented correctly
- [ ] Authorization checks are in place
- [ ] Passwords are hashed (bcrypt)
- [ ] JWT tokens are properly validated

### Data Protection
- [ ] No sensitive data in logs
- [ ] No secrets in code
- [ ] Environment variables used for configuration

## Performance

### Efficiency
- [ ] No unnecessary API calls
- [ ] No N+1 query problems
- [ ] Database queries are optimized
- [ ] Proper use of caching
- [ ] No unnecessary re-renders (frontend)

## Error Handling

### Error Management
- [ ] Errors are caught and handled
- [ ] Error messages are meaningful
- [ ] Errors are logged with context
- [ ] No silent failures

## Documentation

### Code Comments
- [ ] Complex logic is explained
- [ ] Public APIs are documented (JSDoc)
- [ ] No unnecessary comments

### Documentation Updates
- [ ] README updated (if needed)
- [ ] API documentation updated

## Approval Criteria

Code is ready to merge when:
- [ ] All critical issues are addressed
- [ ] All important issues are addressed or discussed
- [ ] Tests pass (unit, integration, E2E)
- [ ] CI checks pass (lint, build, test)
- [ ] At least one reviewer approves
- [ ] No unresolved discussions

## Approval

- [ ] Morgan Lee (Tech Lead)
- [ ] All Reviewers
