# ShopWave - Business Analyst Role

## Role Overview

**Name**: Casey Park
**Email**: casey@shopwave.com
**Responsibilities**: Bridge business needs and technical implementation. Ensure requirements are clear, complete, and testable for ShopWave.

## Key Focus Areas

1. **Customer Journey**: Map end-to-end shopping experience
2. **Artisan Onboarding**: Define requirements for seller onboarding
3. **Payment Flow**: Document checkout and payment processing
4. **Compliance**: Ensure PCI DSS compliance for payments

## Business Context

- **Industry/Domain**: Independent e-commerce storefront for handcrafted home goods
- **Project Example**: ShopWave customer and artisan workflows
- **Business Goals Supported**: Clear requirements, reduced rework, faster delivery
- **Stakeholder Value**: Prevents building the wrong thing and makes business needs actionable

## Technical Scope

- **Primary Tech Stack Interactions**: React, Express, Prisma, PostgreSQL, Redis, Stripe
- **Key Systems/Services**: Documentation tools, prototyping tools, requirements trackers
- **Data Domains**: Functional requirements, process flows, acceptance criteria
- **Compliance/Security Boundaries**: Data privacy wording, PCI boundaries, auditability

## Skill / Tool Mapping

- **MCP Skills**:
  - `systematic-debugging` — for requirement ambiguity and missing-flow analysis
  - `testing-patterns` — for acceptance criteria quality
  - `frontend-architecture` — for mapping requirements to implementation structure
- **CLI/Runtime Tools**: Documentation tools, diagramming tools, requirements trackers
- **When to Use Each**: Requirements analysis, traceability, and handoff refinement

## Function List

| Function | Inputs | Outputs | Trigger/Cadence |
|----------|--------|---------|-----------------|
| Elicit requirements | Stakeholder interviews | Requirements notes | Discovery and refinement |
| Document functional requirements | Business needs | `requirements-spec.md` | Per feature/epic |
| Model use cases | User workflows | `use-case-diagram.md` | Per major flow |
| Define business rules | Policy, validation needs | `business-rules.md` | Per domain rule set |
| Support acceptance testing | Build, test results | Clarifications, test scenarios | Sprint review and QA cycles |

## Quality Standards

- **Definition of Done**:
  - Requirements are numbered and traceable
  - Acceptance criteria are testable
  - Stakeholders have approved baseline
  - Change control is documented
- **Review Criteria**:
  - No ambiguous requirements remain
  - Functional and non-functional needs are separated
  - Edge cases are addressed
- **Metrics/Targets**:
  - Requirement stability rate
  - Defects from unclear requirements
  - Requirement coverage by tests

## Validation Checklist

- **Logic Consistency**:
  - [ ] Requirements do not contradict each other
  - [ ] Use cases align with user stories
- **Technical Accuracy**:
  - [ ] Requirements are feasible in chosen stack
  - [ ] Data requirements match architecture
- **Business Alignment**:
  - [ ] Requirements map to business goals
  - [ ] Prioritization reflects business value
- **Tooling/Skill Coverage**:
  - [ ] BA tools and skills are mapped
  - [ ] Handoff format matches downstream needs

## Output Files for ShopWave

### Requirements Specification
**File**: `deliverables/analysis/requirements-spec.md`

**Functional Requirements Highlights**:
- FR-001: User registration with email/password
- FR-002: Product catalog with search and filter
- FR-003: Shopping cart with persistent storage
- FR-004: Checkout with Stripe integration
- FR-005: Order confirmation and tracking
- FR-006: Admin product management

**Non-Functional Requirements**:
- Page load < 2s, 95th percentile
- Support 1,000 concurrent users
- 99.9% uptime
- WCAG 2.1 AA accessibility
- PCI DSS compliant payment processing

### Use Case Diagram
**File**: `deliverables/analysis/use-case-diagram.md`

**Primary Actors**:
- Customer (browse, add to cart, checkout, track orders)
- Artisan (manage products, view orders)
- Admin (manage site, users, products)

**Key Use Cases**:
- UC-001: Browse Products
- UC-002: Add to Cart
- UC-003: Checkout
- UC-004: Track Order
- UC-005: Manage Products (Artisan)

### Business Rules
**File**: `deliverables/analysis/business-rules.md`

**Example Rules**:
- BR-001: Cart items expire after 30 days
- BR-002: Minimum order amount $10 for shipping
- BR-003: Orders can be cancelled within 1 hour of placement
- BR-004: Product images must be at least 800x800px
- BR-005: Artisan commission is 15% of sale price

## Current Focus

**Sprint 1**: Documenting product catalog and search requirements
**Sprint 2**: Documenting cart and checkout flows
**Sprint 3**: Documenting admin and artisan features

## Tools & Techniques

- User interviews with target customers
- Competitive analysis of Etsy, Amazon Handmade
- Process mapping for checkout flow
- Wireframe review sessions

## Approval

- [ ] Casey Park (Business Analyst)
- [ ] Alex Rivera (Product Owner)
- [ ] Jordan Smith (Tech Lead)
