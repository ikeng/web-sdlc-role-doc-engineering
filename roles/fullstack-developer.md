# Full-stack Developer

## Role Overview

The Full-stack Developer implements features across the entire technology stack, from frontend to backend, ensuring quality and performance.

## Responsibilities

- Implement features according to specifications
- Write clean, maintainable, and tested code
- Participate in code reviews
- Fix bugs and address technical debt
- Write unit and integration tests
- Optimize performance and scalability
- Collaborate with designers and QA
- Participate in sprint planning and estimation

## Output Files

| File | Phase | Description |
|------|-------|-------------|
| Implementation code | Development | Feature and bug fix implementations |
| Unit tests | Development | Unit test suites |
| Integration tests | Development | Integration test suites |
| Code review feedback | Development | Review comments and suggestions |

## File Dimensions

### Implementation Code

**Purpose**: Deliver working, tested, and documented code.

**Required Standards**:
- Follows code standards and guidelines
- Includes inline documentation
- Handles errors gracefully
- Logs appropriately
- Includes input validation
- Follows security best practices
- Is performant and efficient
- Is maintainable and readable

**Quality Gates**:
- [ ] Code passes linting and formatting
- [ ] All tests pass
- [ ] Code coverage meets threshold
- [ ] No security vulnerabilities
- [ ] Performance meets requirements
- [ ] Documentation is complete
- [ ] Code review approved

### Unit Tests

**Purpose**: Ensure individual components work correctly.

**Required Sections**:
- Test file naming convention
- Test structure (describe/it blocks)
- Test cases covering:
  - Happy path
  - Edge cases
  - Error cases
  - Boundary conditions
- Mocking and stubbing
- Test data setup and teardown
- Assertions and expectations
- Test coverage requirements

**Quality Gates**:
- [ ] All public methods are tested
- [ ] Edge cases are covered
- [ ] Error cases are tested
- [ ] Coverage meets threshold (e.g., 80%)
- [ ] Tests are fast and independent
- [ ] Tests are maintainable

### Integration Tests

**Purpose**: Verify components work together correctly.

**Required Sections**:
- Integration test setup
- Test environment configuration
- Test data management
- API contract testing
- Database integration testing
- Third-party service mocking
- End-to-end workflow testing
- Test cleanup and teardown

**Quality Gates**:
- [ ] Key user flows are tested
- [ ] External dependencies are mocked
- [ ] Tests are reliable and repeatable
- [ ] Tests run in CI/CD
- [ ] Failures are actionable

### Code Review Feedback

**Purpose**: Provide constructive feedback on code quality.

**Required Standards**:
- Feedback is constructive and actionable
- References code standards and guidelines
- Explains the "why" behind suggestions
- Prioritizes issues (critical, important, nice-to-have)
- Includes positive feedback
- Suggests improvements with examples

**Quality Gates**:
- [ ] All review items are addressed
- [ ] Feedback is clear and actionable
- [ ] Discussion is respectful
- [ ] Approval criteria are met

## Interaction Patterns

**Inputs From**:
- Tech Lead (guidance and standards)
- UX Designer (design specifications)
- QA Engineer (bug reports)

**Outputs To**:
- Tech Lead (code for review)
- QA Engineer (testable builds)
- DevOps Engineer (deployment artifacts)

**Review Cycle**:
- Daily: Code reviews and pair programming
- Sprint: Implementation and testing
- Release: Bug fixes and hotfixes

## Tools & Templates

- IDEs and code editors
- Testing frameworks (Jest, pytest, etc.)
- Debugging tools
- Version control (Git)
