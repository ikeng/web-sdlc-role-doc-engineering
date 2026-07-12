# ShopWave - Tech Lead Role

## Role Overview

**Name**: Morgan Lee
**Email**: morgan@shopwave.com
**Responsibilities**: Lead technical implementation, ensure code quality, mentor developers for ShopWave.

## Key Focus Areas

1. **Code Quality**: Enforce standards, conduct reviews
2. **Performance**: Optimize queries, implement caching
3. **Security**: Review code for vulnerabilities
4. **Team Growth**: Mentor developers, share knowledge

## Business Context

- **Industry/Domain**: Independent e-commerce storefront for handcrafted home goods
- **Project Example**: ShopWave MVP delivery and early growth
- **Business Goals Supported**: Fast delivery, low defect rate, maintainable codebase
- **Stakeholder Value**: Keeps development predictable and protects long-term ownership cost

## Technical Scope

- **Primary Tech Stack Interactions**: React, Express, Prisma, PostgreSQL, Redis, Stripe
- **Key Systems/Services**: GitHub, CI/CD, Lighthouse, monitoring tools
- **Data Domains**: Code quality metrics, review history, defects
- **Compliance/Security Boundaries**: Secure coding standards, secret handling

## Skill / Tool Mapping

- **MCP Skills**:
  - `code-review` — for review workflow and quality enforcement
  - `verification-before-completion` — for gating merges on evidence
  - `testing-patterns` — for testability guidance
- **CLI/Runtime Tools**: Linters, formatters, review tools, coverage tools
- **When to Use Each**: PR review, standards enforcement, and release gating

## Function List

| Function | Inputs | Outputs | Trigger/Cadence |
|----------|--------|---------|-----------------|
| Set coding standards | Team needs, architecture | `code-standards.md` | Project start and updates |
| Define dev workflow | Process goals | `dev-guidelines.md` | Project setup |
| Run code reviews | PRs, code changes | Review approval or changes | Per PR |
| Mentor developers | Reviews, pairing | Improved implementation quality | Ongoing |
| Track technical debt | Codebase issues | Debt backlog, fixes | Sprint cadence |

## Quality Standards

- **Definition of Done**:
  - Code passes linting, tests, and review checklist
  - Documentation is updated
  - Performance and security considerations are addressed
- **Review Criteria**:
  - Readability, test coverage, error handling, security hygiene
- **Metrics/Targets**:
  - Review turnaround time
  - Defect escape rate
  - Code coverage / quality gate pass rate

## Validation Checklist

- **Logic Consistency**:
  - [ ] Standards align with chosen stack
  - [ ] Review checklist covers required concerns
- **Technical Accuracy**:
  - [ ] Workflow matches repository and CI setup
  - [ ] Tooling choices are compatible
- **Business Alignment**:
  - [ ] Standards do not block delivery goals
  - [ ] Review process balances quality and velocity
- **Tooling/Skill Coverage**:
  - [ ] Review and verification skills are mapped
  - [ ] No missing quality-gate workflow

## Output Files for ShopWave

### Code Standards
**File**: `deliverables/development/code-standards.md`

**Key Standards**:
- TypeScript strict mode
- ESLint + Prettier
- Conventional commits
- 80% test coverage minimum
- All PRs require review

### Development Guidelines
**File**: `deliverables/development/dev-guidelines.md`

**Key Guidelines**:
- GitHub Flow branching
- Feature branches: `feature/US-XXX-description`
- Commit format: `type(scope): description`
- All code reviewed before merge
- Tests run in CI/CD

### Code Review Checklist
**File**: `deliverables/development/code-review-checklist.md`

**Review Criteria**:
- Code follows standards
- Tests cover new functionality
- Error handling implemented
- No security vulnerabilities
- Performance considered
- Documentation updated

## Current Focus

**Sprint 1**: Set up CI/CD, code standards, and development workflow
**Sprint 2**: Review checkout implementation, add integration tests
**Sprint 3**: Performance optimization, caching strategy

## Approval

- [ ] Morgan Lee (Tech Lead)
- [ ] Jordan Smith (Solution Architect)
