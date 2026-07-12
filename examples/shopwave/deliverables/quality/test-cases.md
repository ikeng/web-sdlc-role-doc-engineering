# ShopWave - Test Cases

## Metadata
- **Version**: 1.0
- **Author**: Quinn Brooks (QA Engineer)
- **Date**: 2026-01-15
- **Project**: ShopWave

## Test Cases

### TC-001: User Registration - Valid Input

**Test Type**: Functional / Integration
**Priority**: High
**Requirement**: FR-001

**Preconditions**:
- Application is running
- Test email is not registered

**Test Steps**:
1. Navigate to `/register`
2. Enter valid email: `testuser@example.com`
3. Enter valid password: `SecurePass123!`
4. Enter name: `Test User`
5. Accept terms of service
6. Click "Create Account"

**Expected Result**:
- User is redirected to homepage or dashboard
- Success message is displayed
- User account is created in database

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-002: User Registration - Duplicate Email

**Test Type**: Functional / Integration
**Priority**: High
**Requirement**: FR-001

**Preconditions**:
- User with email `testuser@example.com` already exists

**Test Steps**:
1. Navigate to `/register`
2. Enter existing email: `testuser@example.com`
3. Enter valid password and name
4. Click "Create Account"

**Expected Result**:
- User remains on registration page
- Error message: "Email already registered"

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-003: User Login - Valid Credentials

**Test Type**: Functional / Integration
**Priority**: High
**Requirement**: FR-002

**Preconditions**:
- User account exists

**Test Steps**:
1. Navigate to `/login`
2. Enter valid email and password
3. Click "Log In"

**Expected Result**:
- User is logged in
- Redirected to homepage or account page

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-004: User Login - Invalid Password

**Test Type**: Functional / Integration
**Priority**: High
**Requirement**: FR-002

**Test Steps**:
1. Navigate to `/login`
2. Enter valid email and invalid password
3. Click "Log In"

**Expected Result**:
- Error message: "Invalid email or password"

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-005: Product Search - Valid Search

**Test Type**: Functional / Integration
**Priority**: Medium
**Requirement**: FR-003

**Test Steps**:
1. Navigate to `/products`
2. Enter search term: `ceramic`
3. Press Enter

**Expected Result**:
- Search results displayed
- Results match search term

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-006: Add to Cart - Valid Product

**Test Type**: Functional / Integration
**Priority**: High
**Requirement**: FR-005

**Preconditions**:
- User is logged in
- Product exists and is in stock

**Test Steps**:
1. View product details
2. Click "Add to Cart"
3. Navigate to cart page

**Expected Result**:
- Product is added to cart
- Cart count increases
- Cart page shows added product

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-007: Checkout - Valid Order

**Test Type**: E2E
**Priority**: High
**Requirement**: FR-006

**Preconditions**:
- User is logged in
- User has items in cart

**Test Steps**:
1. Navigate to cart
2. Click "Proceed to Checkout"
3. Enter shipping address
4. Enter payment information (Stripe test card)
5. Click "Place Order"

**Expected Result**:
- Order is created
- Payment is processed
- Confirmation page is displayed
- Confirmation email is sent

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-008: API Response Time

**Test Type**: Performance
**Priority**: High
**Requirement**: NFR-P-002

**Test Steps**:
1. Send GET request to `/api/v1/products`
2. Measure response time
3. Repeat 100 times

**Expected Result**:
- 95th percentile response time < 500ms

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-009: SQL Injection - Login Endpoint

**Test Type**: Security
**Priority**: Critical
**Requirement**: NFR-S-004

**Test Steps**:
1. Send POST request to `/api/v1/auth/login`
2. Use SQL injection payload in email field
3. Observe response

**Expected Result**:
- Request is rejected
- No SQL injection occurs

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-010: Accessibility - Keyboard Navigation

**Test Type**: Accessibility
**Priority**: Medium
**Requirement**: NFR-U-002

**Test Steps**:
1. Navigate to homepage
2. Use Tab key to navigate
3. Use Enter/Space to activate elements

**Expected Result**:
- All interactive elements are focusable
- Focus order is logical

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

## Test Matrix

| Test Case ID | Test Type | Priority | Status |
|--------------|-----------|----------|--------|
| TC-001 | Functional | High | ☐ |
| TC-002 | Functional | High | ☐ |
| TC-003 | Functional | High | ☐ |
| TC-004 | Functional | High | ☐ |
| TC-005 | Functional | Medium | ☐ |
| TC-006 | Functional | High | ☐ |
| TC-007 | E2E | High | ☐ |
| TC-008 | Performance | High | ☐ |
| TC-009 | Security | Critical | ☐ |
| TC-010 | Accessibility | Medium | ☐ |

## Approval

- [ ] Quinn Brooks (QA Engineer)
- [ ] Morgan Lee (Tech Lead)
