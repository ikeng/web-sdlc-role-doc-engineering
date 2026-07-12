# Test Cases

## Metadata
- **Version**: 1.0
- **Author**: QA Engineer
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Epic/Feature**: [Name]

## Test Case Overview

**Total Test Cases**: X
**Automated**: X
**Manual**: X
**Coverage**: X%

## Test Cases

### TC-001: User Registration - Valid Input

**Test Type**: Functional / Integration
**Priority**: High
**Status**: Draft / Ready / Executed / Passed / Failed
**Requirement**: FR-001

**Preconditions**:
- Application is running
- Test user email is not registered
- Email service is available

**Test Steps**:
1. Navigate to `/register`
2. Enter valid email: `testuser@example.com`
3. Enter valid password: `SecurePass123!`
4. Enter name: `Test User`
5. Accept terms of service
6. Click "Register" button

**Expected Result**:
- User is redirected to `/dashboard`
- Success message is displayed
- Welcome email is sent
- User account is created in database

**Actual Result**:
[To be filled during execution]

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

**Notes**:
[Any additional notes]

---

### TC-002: User Registration - Duplicate Email

**Test Type**: Functional / Integration
**Priority**: High
**Status**: Draft / Ready / Executed / Passed / Failed
**Requirement**: FR-001

**Preconditions**:
- Application is running
- User with email `testuser@example.com` already exists

**Test Steps**:
1. Navigate to `/register`
2. Enter existing email: `testuser@example.com`
3. Enter valid password: `SecurePass123!`
4. Enter name: `Test User 2`
5. Accept terms of service
6. Click "Register" button

**Expected Result**:
- User remains on registration page
- Error message displayed: "Email already registered"
- No new user account created
- No email sent

**Actual Result**:
[To be filled during execution]

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-003: User Login - Valid Credentials

**Test Type**: Functional / Integration
**Priority**: High
**Status**: Draft / Ready / Executed / Passed / Failed
**Requirement**: FR-002

**Preconditions**:
- Application is running
- User account exists: `testuser@example.com` / `SecurePass123!`

**Test Steps**:
1. Navigate to `/login`
2. Enter email: `testuser@example.com`
3. Enter password: `SecurePass123!`
4. Click "Login" button

**Expected Result**:
- User is redirected to `/dashboard`
- Session cookie is set
- JWT token is returned

**Actual Result**:
[To be filled during execution]

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-004: User Login - Invalid Password

**Test Type**: Functional / Integration
**Priority**: High
**Status**: Draft / Ready / Executed / Passed / Failed
**Requirement**: FR-002

**Preconditions**:
- Application is running
- User account exists

**Test Steps**:
1. Navigate to `/login`
2. Enter valid email: `testuser@example.com`
3. Enter invalid password: `WrongPass123!`
4. Click "Login" button

**Expected Result**:
- User remains on login page
- Error message: "Invalid email or password"
- No session created
- Failed login attempt is logged

**Actual Result**:
[To be filled during execution]

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-005: Product Search - Valid Search

**Test Type**: Functional / Integration
**Priority**: Medium
**Status**: Draft / Ready / Executed / Passed / Failed
**Requirement**: FR-010

**Preconditions**:
- Application is running
- Products exist in database
- User is on `/products` page

**Test Steps**:
1. Locate search input
2. Enter search term: `laptop`
3. Press Enter or click search button

**Expected Result**:
- Search results are displayed
- Results match search term
- Results count is shown
- No errors in console

**Actual Result**:
[To be filled during execution]

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-006: Add to Cart - Valid Product

**Test Type**: Functional / Integration
**Priority**: High
**Status**: Draft / Ready / Executed / Passed / Failed
**Requirement**: FR-015

**Preconditions**:
- Application is running
- User is logged in
- Product exists and is in stock
- User is on product detail page

**Test Steps**:
1. View product details
2. Click "Add to Cart" button
3. Navigate to cart page

**Expected Result**:
- Product is added to cart
- Cart count increases
- Cart page shows added product
- Product details are correct (name, price, quantity)

**Actual Result**:
[To be filled during execution]

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-007: Checkout - Valid Order

**Test Type**: E2E
**Priority**: High
**Status**: Draft / Ready / Executed / Passed / Failed
**Requirement**: FR-020

**Preconditions**:
- Application is running
- User is logged in
- User has items in cart
- Payment method is available

**Test Steps**:
1. Navigate to cart page
2. Click "Proceed to Checkout"
3. Enter shipping address
4. Select payment method
5. Click "Place Order"

**Expected Result**:
- Order is created
- Payment is processed
- Confirmation page is displayed
- Confirmation email is sent
- Inventory is updated

**Actual Result**:
[To be filled during execution]

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-008: API Response Time

**Test Type**: Performance
**Priority**: High
**Status**: Draft / Ready / Executed / Passed / Failed
**Requirement**: NFR-P-002

**Preconditions**:
- API is running
- Test data exists

**Test Steps**:
1. Send GET request to `/api/v1/products`
2. Measure response time
3. Repeat 100 times
4. Calculate 95th percentile

**Expected Result**:
- 95th percentile response time < 500ms
- No errors in responses

**Actual Result**:
[To be filled during execution]

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

**Metrics**:
- Average: [ ] ms
- 95th percentile: [ ] ms
- Max: [ ] ms

---

### TC-009: SQL Injection - Login Endpoint

**Test Type**: Security
**Priority**: Critical
**Status**: Draft / Ready / Executed / Passed / Failed
**Requirement**: NFR-S-004

**Preconditions**:
- API is running
- Login endpoint is accessible

**Test Steps**:
1. Send POST request to `/api/v1/auth/login`
2. Use SQL injection payload in email field: `admin' OR '1'='1`
3. Observe response

**Expected Result**:
- Request is rejected
- Error message: "Invalid email or password"
- No SQL injection occurs
- Attack is logged

**Actual Result**:
[To be filled during execution]

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

---

### TC-010: Accessibility - Keyboard Navigation

**Test Type**: Accessibility
**Priority**: Medium
**Status**: Draft / Ready / Executed / Passed / Failed
**Requirement**: NFR-U-002

**Preconditions**:
- Application is running
- Page is loaded

**Test Steps**:
1. Disconnect mouse
2. Use Tab key to navigate
3. Use Enter/Space to activate elements
4. Navigate through all interactive elements

**Expected Result**:
- All interactive elements are focusable
- Focus order is logical
- Focus indicator is visible
- All actions can be completed via keyboard

**Actual Result**:
[To be filled during execution]

**Status**: ☐ Pass / ☐ Fail / ☐ Blocked

**Issues Found**:
[List any accessibility issues]

---

## Test Matrix

| Test Case ID | Test Type | Priority | Status | Execution Date | Tester |
|--------------|-----------|----------|--------|----------------|--------|
| TC-001 | Functional | High | ☐ | | |
| TC-002 | Functional | High | ☐ | | |
| TC-003 | Functional | High | ☐ | | |
| TC-004 | Functional | High | ☐ | | |
| TC-005 | Functional | Medium | ☐ | | |
| TC-006 | Functional | High | ☐ | | |
| TC-007 | E2E | High | ☐ | | |
| TC-008 | Performance | High | ☐ | | |
| TC-009 | Security | Critical | ☐ | | |
| TC-010 | Accessibility | Medium | ☐ | | |

## Test Summary

**Total Test Cases**: X
**Passed**: X
**Failed**: X
**Blocked**: X
**Not Run**: X

**Pass Rate**: X%

## Defects Found

| Test Case ID | Defect ID | Severity | Description | Status |
|--------------|-----------|----------|-------------|--------|
| TC-001 | DEF-001 | High | [Description] | Open / Fixed / Closed |
| TC-002 | DEF-002 | Medium | [Description] | Open / Fixed / Closed |

## Approval

- [ ] QA Engineer
- [ ] Tech Lead
