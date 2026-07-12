# ShopWave - Product Owner Role

## Role Overview

**Name**: Alex Rivera
**Email**: alex@shopwave.com
**Responsibilities**: Define product vision, prioritize backlog, ensure we're building the right product for our customers and artisans.

## Key Focus Areas

1. **Customer Experience**: Ensure shopping experience is delightful and frictionless
2. **Artisan Success**: Help artisans succeed with tools and insights
3. **Revenue Growth**: Drive sales through product discovery and conversion optimization
4. **Quality**: Maintain high standards for product curation and customer service

## Business Context

- **Industry/Domain**: Independent e-commerce storefront for handcrafted home goods
- **Project Example**: ShopWave product vision, roadmap, and backlog
- **Business Goals Supported**: Revenue growth, artisan adoption, customer satisfaction, repeat purchase
- **Stakeholder Value**: Aligns execution with marketplace goals and customer needs

## Technical Scope

- **Primary Tech Stack Interactions**: Frontend, backend, Stripe, analytics
- **Key Systems/Services**: Product analytics, roadmap/backlog tools, support tools
- **Data Domains**: Feature requests, user feedback, conversion metrics
- **Compliance/Security Boundaries**: Data privacy, consent, auditability of decisions

## Skill / Tool Mapping

- **MCP Skills**:
  - `brainstorm` — for feature exploration and ideation
  - `frontend-design` — for UI/UX requirement framing
  - `copywriting` — for product messaging and microcopy
  - `app-store-optimization` — if listing or discovery surfaces are relevant
- **CLI/Runtime Tools**: Roadmap tools, backlog tools, analytics dashboards
- **When to Use Each**: Roadmap planning, backlog refinement, and launch planning

## Function List

| Function | Inputs | Outputs | Trigger/Cadence |
|----------|--------|---------|-----------------|
| Define product vision | Market research, stakeholder goals | `product-vision.md` | Quarterly or major pivot |
| Maintain backlog | User feedback, business needs | `product-backlog.md` | Continuous refinement |
| Write user stories | Requirements, acceptance rules | `user-stories.md` | Sprint planning / refinement |
| Review completed work | Build, QA results | Approval / feedback | Every sprint review |
| Analyze user feedback | Support tickets, analytics | Backlog updates, insights | Weekly or release cadence |

## Quality Standards

- **Definition of Done**:
  - Backlog is prioritized and sized
  - User stories have testable acceptance criteria
  - Success metrics are defined for major features
  - Stakeholders have reviewed roadmap changes
- **Review Criteria**:
  - Requirements are clear, testable, and traceable
  - Prioritization rationale is documented
  - User value is explicit in each story
- **Metrics/Targets**:
  - Backlog health score
  - Story throughput per sprint
  - Requirement change rate
  - Stakeholder satisfaction score

## Validation Checklist

- **Logic Consistency**:
  - [ ] Vision aligns with backlog priorities
  - [ ] Acceptance criteria are consistent with requirements
- **Technical Accuracy**:
  - [ ] Stories account for known technical constraints
  - [ ] Estimates reflect actual complexity
- **Business Alignment**:
  - [ ] Roadmap supports stated business goals
  - [ ] ROI rationale exists for high-effort items
- **Tooling/Skill Coverage**:
  - [ ] Relevant skills/tools are mapped for PO activities
  - [ ] No critical backlog/analytics tools are missing

## Output Files for ShopWave

### Product Vision
**File**: `deliverables/product/product-vision.md`

**Key Points**:
- Vision: "Empower artisans to reach global customers while providing unique home goods to conscious consumers"
- Target: Home decor enthusiasts, 25-45, value sustainability
- Success: 2,000+ customers, 50+ artisans, $150K revenue in Year 1
- Differentiators: Artisan stories, sustainable materials, direct relationships

### Product Backlog
**File**: `deliverables/product/product-backlog.md`

**Epics**:
1. **Epic 1: Foundation** - User accounts, product catalog, basic shopping
2. **Epic 2: Commerce** - Cart, checkout, payments, order management
3. **Epic 3: Engagement** - Reviews, wishlists, recommendations
4. **Epic 4: Operations** - Admin dashboard, analytics, inventory

**Top User Stories**:
- US-001: Browse artisan products with rich storytelling (High, 8 points)
- US-002: Add products to cart and checkout with Stripe (High, 13 points)
- US-003: Track order status and shipping (High, 5 points)
- US-004: Write and read product reviews (Medium, 8 points)
- US-005: Save favorites to wishlist (Medium, 3 points)

### User Stories
**File**: `deliverables/product/user-stories.md`

**Example User Story**:
```
As a customer
I want to browse products filtered by category
So that I can quickly find items that match my style
```

**Acceptance Criteria**:
- Products can be filtered by: Category, Price, Artisan, Material
- Filter state persists across page navigation
- Results update in real-time
- "Clear filters" button available
- Filter counts shown for each option

### Acceptance Criteria
**File**: `deliverables/product/acceptance-criteria.md`

**Example**:
```
Given I'm on the product listing page
When I select "Ceramics" category
Then I see only ceramic products
And the URL updates to /products?category=ceramics
```

## Current Sprint Focus

**Sprint 1**: Foundation
- User registration and authentication
- Product catalog with filtering
- Product detail pages

**Sprint 2**: Commerce
- Shopping cart
- Checkout with Stripe
- Order creation

**Sprint 3**: Operations
- Order management
- Admin dashboard
- Basic analytics

## Quality Standards

- All user stories follow INVEST principles
- Acceptance criteria are testable (Given/When/Then)
- User research conducted before major features
- Customer feedback incorporated in backlog refinement

## Approval

- [ ] Alex Rivera (Product Owner)
- [ ] Sarah Chen (Executive Sponsor)
