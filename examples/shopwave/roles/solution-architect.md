# ShopWave - Solution Architect Role

## Role Overview

**Name**: Jordan Smith
**Email**: jordan@shopwave.com
**Responsibilities**: Design system architecture, select technology stack, ensure scalability and security for ShopWave.

## Key Focus Areas

1. **Performance**: Fast page loads, efficient database queries
2. **Scalability**: Handle growth in products, users, and traffic
3. **Security**: PCI DSS compliance, data protection
4. **Maintainability**: Clean architecture, easy to extend

## Business Context

- **Industry/Domain**: Independent e-commerce storefront for handcrafted home goods
- **Project Example**: ShopWave catalog, checkout, artisan onboarding, and admin platform
- **Business Goals Supported**: Fast browsing, reliable checkout, growth readiness, low ownership cost
- **Stakeholder Value**: Provides scalable foundation and reduces technical risk

## Technical Scope

- **Primary Tech Stack Interactions**: React, Node.js/Express, PostgreSQL, Redis, Stripe, AWS
- **Key Systems/Services**: S3/CloudFront, RDS, ElastiCache, CloudWatch, Stripe
- **Data Domains**: Products, cart, orders, users, sessions, images
- **Compliance/Security Boundaries**: PCI boundaries, customer PII, auth boundaries

## Skill / Tool Mapping

- **MCP Skills**:
  - `architecture-designer` — for system and module design
  - `system-design` — for scalability and tradeoff analysis
  - `frontend-architecture` — for client-side architecture decisions
  - `supabase-postgres-best-practices` — if PostgreSQL/data layer is involved
- **CLI/Runtime Tools**: Diagramming tools, OpenAPI tooling, ADR tools
- **When to Use Each**: Architecture design, API design, data-modeling, and tech-stack review

## Function List

| Function | Inputs | Outputs | Trigger/Cadence |
|----------|--------|---------|-----------------|
| Design system architecture | Requirements, constraints | `architecture-doc.md` | Project start / major change |
| Select tech stack | Requirements, team skills | `tech-stack.md` | Architecture phase |
| Design APIs | Product requirements | `api-design.md` | Per feature area |
| Write ADRs | Significant decisions | ADR documents | As decisions are made |
| Review implementation | Code, PRs, incidents | Architecture feedback | Ongoing |

## Quality Standards

- **Definition of Done**:
  - Architecture is documented and approved
  - Tech stack has clear rationale
  - API contracts are stable
  - ADRs exist for major decisions
- **Review Criteria**:
  - Requirements are satisfied without overengineering
  - Performance and scalability are addressed
  - Security and operability are built in
- **Metrics/Targets**:
  - Architectural change rate
  - Incident rate by component
  - Delivery predictability

## Validation Checklist

- **Logic Consistency**:
  - [ ] Components and flows are internally consistent
  - [ ] API contracts match data models
- **Technical Accuracy**:
  - [ ] Stack choices match requirements
  - [ ] Deployment model is realistic
- **Business Alignment**:
  - [ ] Architecture supports business goals
  - [ ] Non-functional requirements are met
- **Tooling/Skill Coverage**:
  - [ ] Architecture and API skills are mapped
  - [ ] No missing design or diagramming workflow

## Output Files for ShopWave

### Architecture Document
**File**: `deliverables/architecture/architecture-doc.md`

**Architecture Style**: Monolith with modular design
**Rationale**: Simpler to deploy and maintain for MVP, can evolve to microservices later

**Key Components**:
- Frontend: React SPA with SSR for SEO
- Backend: Express.js REST API
- Database: PostgreSQL (products, orders, users)
- Cache: Redis (sessions, cart, product listings)
- Storage: AWS S3 (product images)
- Payments: Stripe API

### Technology Stack
**File**: `deliverables/architecture/tech-stack.md`

**Frontend**:
- React 18 with TypeScript
- Vite for build
- React Query for data fetching
- Tailwind CSS for styling
- React Router for navigation

**Backend**:
- Node.js 20 LTS
- Express.js
- Prisma ORM
- JWT authentication
- Stripe SDK

**DevOps**:
- AWS ECS for deployment
- CloudFront CDN
- RDS PostgreSQL
- ElastiCache Redis
- CloudWatch monitoring

### API Design
**File**: `deliverables/architecture/api-design.md`

**Key Endpoints**:
- GET /api/v1/products - List products
- GET /api/v1/products/:id - Product details
- POST /api/v1/cart - Add to cart
- POST /api/v1/checkout - Create order
- GET /api/v1/orders - User orders
- POST /api/v1/admin/products - Create product (admin)

## Key Decisions

- **Why Stripe**: Best developer experience, comprehensive features
- **Why PostgreSQL**: ACID compliance for orders, JSON support for product attributes
- **Why Redis**: Fast session/cart storage, pub/sub for notifications
- **Why AWS**: Managed services, scalability, familiar to team

## Current Focus

**Sprint 1**: Set up development environment and core API structure
**Sprint 2**: Implement checkout flow with Stripe
**Sprint 3**: Optimize performance and add caching

## Approval

- [ ] Jordan Smith (Solution Architect)
- [ ] Tech Leads
- [ ] Morgan Lee (Project Manager)
