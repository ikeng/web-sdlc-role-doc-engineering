# Tech Lead

## Role Overview

The Tech Lead leads the technical implementation, ensures code quality, and mentors developers on best practices and architectural patterns.

## Responsibilities

- Lead technical implementation of features
- Review code for quality and standards compliance
- Mentor and coach developers
- Make technical decisions and trade-offs
- Identify and mitigate technical risks
- Ensure code quality and maintainability
- Coordinate with Solution Architect on implementation
- Participate in sprint planning and estimation

## Output Files

| File | Phase | Description |
|------|-------|-------------|
| `code-standards.md` | Development | Code style and quality standards |
| `dev-guidelines.md` | Development | Development guidelines and best practices |
| `code-review-checklist.md` | Development | Code review criteria and checklist |

## File Dimensions

### code-standards.md

**Purpose**: Define code style, structure, and quality standards for the team.

**Required Sections**:
- Code style guide (language-specific)
- Naming conventions (files, variables, functions, classes)
- Code organization and structure
- Commenting and documentation standards
- Error handling patterns
- Logging standards
- Testing requirements (coverage, types)
- Performance guidelines
- Security best practices
- Version control conventions

**Quality Gates**:
- [ ] Standards are documented and accessible
- [ ] All team members have reviewed
- [ ] Linting/formatting tools are configured
- [ ] Standards are enforced in CI/CD

### dev-guidelines.md

**Purpose**: Provide development guidelines and best practices.

**Required Sections**:
- Development workflow (branching, commits)
- Pull request process
- Code review expectations
- Testing requirements and types
- Debugging and troubleshooting
- Performance optimization
- Security guidelines
- Accessibility guidelines
- Internationalization (i18n) guidelines
- Common patterns and anti-patterns

**Quality Gates**:
- [ ] Guidelines are clear and actionable
- [ ] Examples are provided
- [ ] Team has been trained
- [ ] Guidelines are followed in practice

### code-review-checklist.md

**Purpose**: Standardized checklist for code reviews.

**Required Sections**:
- Code quality and style
- Architecture and design
- Functionality and correctness
- Performance considerations
- Security vulnerabilities
- Test coverage
- Documentation
- Accessibility
- Error handling
- Backward compatibility

**Quality Gates**:
- [ ] All checklist items are addressed
- [ ] Review feedback is constructive
- [ ] At least one reviewer approves
- [ ] CI checks pass

## Interaction Patterns

**Inputs From**:
- Solution Architect (architecture decisions)
- Product Owner (feature requirements)
- QA Engineer (quality feedback)

**Outputs To**:
- Full-stack Developer (guidance and feedback)
- QA Engineer (testable code)
- DevOps Engineer (deployment-ready code)

**Review Cycle**:
- Daily: Code reviews
- Weekly: Technical debt review
- Sprint: Architecture review
- Monthly: Standards update

## Tools & Templates

- Code review tools (GitHub PR, GitLab MR)
- Linting tools (ESLint, Prettier)
- Code quality tools (SonarQube, CodeClimate)
- Review templates
