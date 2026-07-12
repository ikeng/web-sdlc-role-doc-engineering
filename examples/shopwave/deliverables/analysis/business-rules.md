# ShopWave - Business Rules

## Metadata
- **Version**: 1.0
- **Author**: Casey Park (Business Analyst)
- **Date**: 2026-01-15
- **Project**: ShopWave
- **Last Updated**: 2026-01-15

## Rule Overview

This document defines business rules for ShopWave e-commerce platform.

---

## Rule 1: User Registration Validation

**Rule ID**: BR-001
**Category**: Validation Rule
**Priority**: High
**Status**: Approved

### Rule Definition
A user can only register with a valid, unique email address and a strong password.

### Business Context
Ensures data integrity and security.

### Validation Logic
```
IF email EXISTS in users table
THEN reject registration with error "Email already registered"

IF email FORMAT is invalid
THEN reject registration with error "Invalid email format"

IF password LENGTH < 8
OR password DOES NOT contain uppercase
OR password DOES NOT contain lowercase
OR password DOES NOT contain number
OR password DOES NOT contain special character
THEN reject registration with error "Password must be at least 8 characters with uppercase, lowercase, number, and special character"
```

### Error Messages
- "Email already registered"
- "Invalid email format"
- "Password must be at least 8 characters with uppercase, lowercase, number, and special character"

### Test Cases
- [ ] TC-001: Register with existing email → Error
- [ ] TC-002: Register with invalid email → Error
- [ ] TC-003: Register with weak password → Error
- [ ] TC-004: Register with valid data → Success

---

## Rule 2: Cart Total Calculation

**Rule ID**: BR-002
**Category**: Computation Rule
**Priority**: High
**Status**: Approved

### Rule Definition
Cart total = sum of (item price × quantity) + tax - discount

### Business Context
Ensures accurate pricing.

### Computation Logic
```
cart_total = 0
FOR EACH item IN cart:
  cart_total += item.price × item.quantity

tax = cart_total × tax_rate (e.g., 0.08 for 8%)
cart_total += tax

ROUND cart_total TO 2 decimal places
```

### Example
- Item A: $25 × 2 = $50
- Item B: $30 × 1 = $30
- Subtotal: $80
- Tax (8%): $6.40
- Total: $86.40

### Test Cases
- [ ] TC-005: Calculate cart with single item
- [ ] TC-006: Calculate cart with multiple items
- [ ] TC-007: Calculate cart with tax

---

## Rule 3: Order Status Transitions

**Rule ID**: BR-003
**Category**: Inference Rule
**Priority**: High
**Status**: Approved

### Rule Definition
Order status follows specific state transitions.

### State Machine
```
PENDING → PROCESSING → SHIPPED → DELIVERED
   ↓          ↓           ↓          ↓
CANCELLED  CANCELLED   RETURNED   RETURNED
```

### Transition Rules
- PENDING: Can transition to PROCESSING or CANCELLED
- PROCESSING: Can transition to SHIPPED, CANCELLED, or REFUNDED
- SHIPPED: Can transition to DELIVERED or RETURNED
- DELIVERED: Can transition to RETURNED (within 30 days)
- CANCELLED/REFUNDED/RETURNED: Terminal states

### Test Cases
- [ ] TC-008: PENDING → PROCESSING → Success
- [ ] TC-009: PENDING → SHIPPED → Error
- [ ] TC-010: DELIVERED → CANCELLED → Error

---

## Rule 4: Minimum Order Amount

**Rule ID**: BR-004
**Category**: Validation Rule
**Priority**: Medium
**Status**: Approved

### Rule Definition
Orders must meet minimum amount for shipping.

### Business Context
Ensures cost-effective shipping.

### Validation Logic
```
IF cart_total < MINIMUM_ORDER_AMOUNT ($25)
THEN reject checkout with error "Minimum order amount is $25"
```

### Test Cases
- [ ] TC-011: Order $30 → Success
- [ ] TC-012: Order $20 → Error

---

## Rule 5: Inventory Management

**Rule ID**: BR-005
**Category**: Action Enabler
**Priority**: High
**Status**: Approved

### Rule Definition
Inventory is reserved when order is placed and decremented when shipped.

### Business Logic
```
WHEN order is created:
  - Reserve inventory for each item
  - IF available_quantity < order_quantity
    THEN reject order with "Insufficient inventory"
  - ELSE decrement available_quantity by order_quantity

WHEN order is shipped:
  - Mark inventory as shipped

WHEN order is cancelled:
  - Return inventory to available_quantity
```

### Test Cases
- [ ] TC-013: Place order with sufficient inventory → Success
- [ ] TC-014: Place order with insufficient inventory → Error
- [ ] TC-015: Cancel order → Inventory returned

---

## Rule 6: Rate Limiting

**Rule ID**: BR-006
**Category**: Timing Rule
**Priority**: Medium
**Status**: Approved

### Rule Definition
API endpoints have rate limits to prevent abuse.

### Rate Limits
```
Authentication endpoints: 5 requests per minute per IP
API endpoints: 100 requests per minute per user
Password reset: 3 requests per hour per email
```

### Test Cases
- [ ] TC-016: Requests within limit → Success
- [ ] TC-017: Requests exceeding limit → 429 error

---

## Rule 7: Cancellation Window

**Rule ID**: BR-007
**Category**: Timing Rule
**Priority**: Medium
**Status**: Approved

### Rule Definition
Orders can only be cancelled within 1 hour of placement.

### Business Logic
```
IF order.status == PENDING
AND current_time - order.created_at < 1 hour
THEN allow cancellation
ELSE reject cancellation with error "Order cannot be cancelled"
```

### Test Cases
- [ ] TC-018: Cancel within 1 hour → Success
- [ ] TC-019: Cancel after 1 hour → Error

---

## Rule Maintenance

### Change Control
- All rule changes require BA and Tech Lead approval
- Version number incremented on change
- Change log maintained

### Review Schedule
- Monthly review of all rules
- Quarterly stakeholder review

## Approval

- [ ] Casey Park (Business Analyst)
- [x] Alex Rivera (Product Owner)
- [x] Jordan Smith (Tech Lead)
- [ ] Quinn Brooks (QA Engineer)
