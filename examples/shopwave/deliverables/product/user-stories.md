# ShopWave - User Stories

## Metadata
- **Version**: 1.0
- **Owner**: Alex Rivera
- **Last Updated**: 2026-01-15
- **Epic**: Epic 1: Foundation

## User Story Template

```
As a [user persona]
I want [feature/capability]
So that [business value/benefit]
```

## User Stories

### US-001: User Registration

**As a** customer
**I want** to create an account with email and password
**So that** I can save my information and track orders

#### Details
- **Epic**: Epic 1: Foundation
- **Priority**: High
- **Story Points**: 5
- **Sprint**: Sprint 1
- **Status**: To Do
- **Assignee**: Riley Chen

#### Acceptance Criteria

**Scenario 1: Successful registration**
- **Given** I am on the registration page
- **When** I enter valid email, password, and name
- **And** I accept terms of service
- **And** I click "Create Account"
- **Then** my account is created
- **And** I am automatically logged in
- **And** I see a welcome message

**Scenario 2: Email already exists**
- **Given** I am on the registration page
- **When** I enter an email that is already registered
- **And** I click "Create Account"
- **Then** I see error "Email already registered"
- **And** I remain on the registration page

**Scenario 3: Invalid password**
- **Given** I am on the registration page
- **When** I enter a password that doesn't meet requirements
- **And** I click "Create Account"
- **Then** I see error "Password must be at least 8 characters with uppercase, lowercase, number, and special character"

#### Definition of Done
- [ ] Frontend registration form implemented
- [ ] Backend registration endpoint created
- [ ] Password validation implemented
- [ ] Email uniqueness check
- [ ] Unit tests written
- [ ] Integration tests written
- [ ] Code reviewed and approved
- [ ] QA tested and passed

#### Dependencies
- None

#### Notes
- Send welcome email after registration
- Log registration event for analytics

---

### US-002: User Login

**As a** registered customer
**I want** to log in with my email and password
**So that** I can access my account and orders

#### Details
- **Epic**: Epic 1: Foundation
- **Priority**: High
- **Story Points**: 3
- **Sprint**: Sprint 1
- **Status**: To Do
- **Assignee**: Riley Chen

#### Acceptance Criteria

**Scenario 1: Successful login**
- **Given** I am on the login page
- **When** I enter valid email and password
- **And** I click "Log In"
- **Then** I am logged in
- **And** I am redirected to my account or homepage
- **And** I see a welcome message

**Scenario 2: Invalid credentials**
- **Given** I am on the login page
- **When** I enter invalid email or password
- **And** I click "Log In"
- **Then** I see error "Invalid email or password"
- **And** I remain on the login page

**Scenario 3: Forgot password link**
- **Given** I am on the login page
- **When** I click "Forgot password?"
- **Then** I am redirected to password reset page

#### Definition of Done
- [ ] Frontend login form implemented
- [ ] Backend login endpoint created
- [ ] JWT token generation
- [ ] Session management
- [ ] Unit tests written
- [ ] Integration tests written
- [ ] Code reviewed and approved
- [ ] QA tested and passed

#### Dependencies
- US-001: User registration

#### Notes
- Implement rate limiting to prevent brute force attacks
- Log login attempts for security

---

### US-003: Product Catalog

**As a** customer
**I want** to browse products organized by category
**So that** I can discover items that interest me

#### Details
- **Epic**: Epic 1: Foundation
- **Priority**: High
- **Story Points**: 8
- **Sprint**: Sprint 1
- **Status**: To Do
- **Assignee**: Riley Chen

#### Acceptance Criteria

**Scenario 1: View all products**
- **Given** I am on the products page
- **When** the page loads
- **Then** I see a grid of products
- **And** each product shows: image, name, price, artisan name
- **And** products are sorted by newest first

**Scenario 2: Filter by category**
- **Given** I am on the products page
- **When** I select a category from the filter
- **Then** only products in that category are shown
- **And** the URL updates to include the category filter

**Scenario 3: Search products**
- **Given** I am on the products page
- **When** I enter a search term
- **And** I press Enter
- **Then** I see products matching the search term
- **And** results highlight matching text

**Scenario 4: Pagination**
- **Given** there are more than 20 products
- **When** I scroll to the bottom
- **Then** I see a "Load More" button or pagination
- **And** clicking loads the next 20 products

#### Definition of Done
- [ ] Product listing page implemented
- [ ] Category filtering implemented
- [ ] Search functionality implemented
- [ ] Pagination implemented
- [ ] Responsive design
- [ ] Unit tests written
- [ ] Integration tests written
- [ ] Code reviewed and approved
- [ ] QA tested and passed

#### Dependencies
- None

#### Notes
- Optimize images for fast loading
- Implement lazy loading for images
- Cache product listings for performance

---

### US-004: Product Detail

**As a** customer
**I want** to view detailed information about a product
**So that** I can make an informed purchase decision

#### Details
- **Epic**: Epic 1: Foundation
- **Priority**: High
- **Story Points**: 5
- **Sprint**: Sprint 1
- **Status**: To Do
- **Assignee**: Riley Chen

#### Acceptance Criteria

**Scenario 1: View product details**
- **Given** I am on a product page
- **When** the page loads
- **Then** I see: product images, name, price, description
- **And** I see: artisan information, materials, dimensions
- **And** I see: "Add to Cart" button

**Scenario 2: View product images**
- **Given** I am on a product page
- **When** I click on the product image
- **Then** I see a larger view of the image
- **And** I can navigate between multiple images

**Scenario 3: Related products**
- **Given** I am on a product page
- **Then** I see related products from the same artisan
- **And** I see products from the same category

#### Definition of Done
- [ ] Product detail page implemented
- [ ] Image gallery with zoom
- [ ] Related products section
- [ ] Responsive design
- [ ] Unit tests written
- [ ] Integration tests written
- [ ] Code reviewed and approved
- [ ] QA tested and passed

#### Dependencies
- US-003: Product catalog

#### Notes
- Include schema.org markup for SEO
- Optimize images for web

---

### US-005: Shopping Cart

**As a** customer
**I want** to add products to a shopping cart
**So that** I can purchase multiple items at once

#### Details
- **Epic**: Epic 2: Commerce
- **Priority**: High
- **Story Points**: 8
- **Sprint**: Sprint 2
- **Status**: To Do
- **Assignee**: Riley Chen

#### Acceptance Criteria

**Scenario 1: Add product to cart**
- **Given** I am on a product page
- **When** I click "Add to Cart"
- **Then** the product is added to my cart
- **And** I see a confirmation message
- **And** the cart icon updates with item count

**Scenario 2: View cart**
- **Given** I have items in my cart
- **When** I click the cart icon
- **Then** I see a cart drawer or page
- **And** I see all items with quantities and prices
- **And** I see the cart total

**Scenario 3: Update quantity**
- **Given** I am viewing my cart
- **When** I change the quantity of an item
- **Then** the cart total updates
- **And** the item count updates

**Scenario 4: Remove item**
- **Given** I am viewing my cart
- **When** I click "Remove" on an item
- **Then** the item is removed from my cart
- **And** the cart total updates

#### Definition of Done
- [ ] Cart functionality implemented
- [ ] Cart persists across sessions
- [ ] Quantity updates work
- [ ] Remove item functionality
- [ ] Cart total calculation
- [ ] Unit tests written
- [ ] Integration tests written
- [ ] Code reviewed and approved
- [ ] QA tested and passed

#### Dependencies
- US-004: Product detail

#### Notes
- Store cart in Redis for performance
- Persist cart for logged-in users in database

---

## Story Mapping

### User Journey: Browse and Buy

1. Landing page → Browse → Product Detail → Add to Cart → Checkout → Confirmation
   - US-003: Browse products
   - US-004: Product detail
   - US-005: Add to cart
   - US-006: Checkout
   - US-007: Order confirmation

### User Journey: Account Management

1. Landing page → Register → Login → View Orders → Track Order
   - US-001: Register
   - US-002: Login
   - US-008: View orders
   - US-009: Track order

## Story Prioritization

### Must Have (MVP)
- US-001: User registration
- US-002: User login
- US-003: Product catalog
- US-004: Product detail
- US-005: Shopping cart
- US-006: Checkout
- US-007: Order confirmation
- US-008: Order tracking

### Should Have
- US-009: Admin dashboard
- US-010: Product reviews

### Could Have
- US-011: Wishlist
- US-012: Recommendations

### Won't Have (for now)
- US-013: Subscription orders
- US-014: International shipping
- US-015: Mobile app

## Story Points Estimation

| Story ID | Title | Points | Rationale |
|----------|-------|--------|-----------|
| US-001 | User registration | 5 | Form, validation, email |
| US-002 | User login | 3 | Form, JWT, session |
| US-003 | Product catalog | 8 | Listing, filters, search, pagination |
| US-004 | Product detail | 5 | Page, images, related products |
| US-005 | Shopping cart | 8 | Cart logic, persistence, updates |
| US-006 | Checkout | 13 | Multi-step, Stripe, validation |
| US-007 | Order confirmation | 3 | Page, email notification |
| US-008 | Order tracking | 5 | Status updates, tracking page |
| US-009 | Admin dashboard | 13 | Product management, order management |
| US-010 | Product reviews | 8 | Review form, display, moderation |

## Approval

- [x] Alex Rivera (Product Owner)
- [x] Sarah Chen (Executive Sponsor)
- [ ] Jordan Smith (Tech Lead)
