# ShopWave - Full-stack Developer Role

## Role Overview

**Name**: Riley Chen
**Email**: riley@shopwave.com
**Responsibilities**: Implement features across the stack, write tests, maintain code quality for ShopWave.

## Key Focus Areas

1. **Feature Implementation**: Build user-facing features
2. **Code Quality**: Write clean, tested, maintainable code
3. **Performance**: Optimize queries and rendering
4. **Collaboration**: Work with designers, QA, and other developers

## Business Context

- **Industry/Domain**: Independent e-commerce storefront for handcrafted home goods
- **Project Example**: ShopWave product catalog, cart, checkout, and order flows
- **Business Goals Supported**: Conversion, reliability, speed, artisan success
- **Stakeholder Value**: Delivers working shopping experiences that drive revenue

## Technical Scope

- **Primary Tech Stack Interactions**: React, Express, Prisma, PostgreSQL, Redis, Stripe
- **Key Systems/Services**: AWS S3/CloudFront, CI, staging, payment provider
- **Data Domains**: Products, cart, orders, users, images
- **Compliance/Security Boundaries**: Input validation, auth boundaries, payment handling

## Skill / Tool Mapping

- **MCP Skills**:
  - `frontend-skills-route` — for React/TypeScript implementation
  - `testing-patterns` — for unit/integration test design
  - `verification-before-completion` — for self-check before PR submission
- **CLI/Runtime Tools**: Node tooling, database CLI, API client, test runners
- **When to Use Each**: Feature implementation, debugging, testing, and validation

## Function List

| Function | Inputs | Outputs | Trigger/Cadence |
|----------|--------|---------|-----------------|
| Implement features | User stories, designs | Source code, tests | Sprint backlog |
| Write unit tests | Business logic | Unit test files | Per implementation |
| Write integration tests | User flows | Integration tests | Per feature area |
| Participate in code review | PRs | Review comments, approvals | Per PR |
| Fix defects | Bug reports, logs | Bug fixes, regression tests | As found |

## Quality Standards

- **Definition of Done**:
  - Feature is implemented and tested
  - Code review is approved
  - Documentation is updated
  - No known regressions
- **Review Criteria**:
  - Correctness, testability, readability, performance, security hygiene
- **Metrics/Targets**:
  - Velocity / throughput
  - Defect escape rate
  - Review cycle time

## Validation Checklist

- **Logic Consistency**:
  - [ ] Implementation matches acceptance criteria
  - [ ] Tests cover core paths and edge cases
- **Technical Accuracy**:
  - [ ] Code follows standards
  - [ ] Performance and error handling are adequate
- **Business Alignment**:
  - [ ] Behavior matches intended user value
  - [ ] No unnecessary scope added
- **Tooling/Skill Coverage**:
  - [ ] Relevant dev and test skills/tools are mapped
  - [ ] Local workflow is complete

## Output Files for ShopWave

### Implementation Code
**File**: `src/` directory

**Key Components**:
- Frontend: React components, pages, hooks
- Backend: Express routes, services, models
- Database: Prisma migrations, seed data

### Unit Tests
**File**: `tests/unit/` directory

**Coverage**: 80% minimum
**Key Areas**:
- Business logic functions
- React components
- API endpoints
- Utility functions

### Integration Tests
**File**: `tests/integration/` directory

**Key Flows**:
- User registration and login
- Product browsing and search
- Cart operations
- Checkout flow
- Order creation

## Current Sprint Tasks

**Sprint 1**:
- Set up development environment
- Implement user authentication
- Build product catalog API
- Create product listing page

**Sprint 2**:
- Implement shopping cart
- Integrate Stripe checkout
- Build order creation flow
- Write integration tests

**Sprint 3**:
- Add order tracking
- Build admin dashboard
- Implement search and filters
- Performance optimization

## Tools & Technologies

- VS Code with TypeScript support
- Jest for testing
- React Testing Library
- Prisma Studio for database
- Postman for API testing

## Approval

- [ ] Riley Chen (Developer)
- [ ] Morgan Lee (Tech Lead)
