# Business Rules

## Metadata
- **Version**: 1.0
- **Author**: Business Analyst
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Last Updated**: YYYY-MM-DD

## Rule Overview

This document defines all business rules for the system. Business rules are constraints that govern or influence business behavior.

## Rule Categories

- **Validation Rules**: Data validation constraints
- **Computation Rules**: Calculations and formulas
- **Inference Rules**: Business logic deductions
- **Action Enablers**: Conditions that trigger actions
- **Timing Rules**: Time-based constraints

---

## Rule 1: User Registration Validation

**Rule ID**: BR-001
**Category**: Validation Rule
**Priority**: High
**Status**: Draft / In Review / Approved

### Rule Definition
A user can only register if their email address is unique and valid.

### Business Context
Prevents duplicate accounts and ensures data integrity.

### Validation Logic
```
IF email EXISTS in users table
THEN reject registration with error "Email already registered"

IF email FORMAT is invalid
THEN reject registration with error "Invalid email format"

IF password LENGTH < 8
THEN reject registration with error "Password must be at least 8 characters"

IF password DOES NOT MATCH confirm_password
THEN reject registration with error "Passwords do not match"
```

### Error Messages
- "Email already registered": User tries to register with existing email
- "Invalid email format": Email format is malformed
- "Password must be at least 8 characters": Password too short
- "Passwords do not match": Password and confirm password fields don't match

### Dependencies
- BR-002: Password Complexity Requirements
- User table schema

### Examples
- **Valid**: user@example.com / Password123! → Registration succeeds
- **Invalid**: user@example.com / Password123! / Password1234! → "Passwords do not match"

### Test Cases
- [ ] TC-001: Register with existing email → Error
- [ ] TC-002: Register with invalid email format → Error
- [ ] TC-003: Register with weak password → Error
- [ ] TC-004: Register with mismatched passwords → Error
- [ ] TC-005: Register with valid data → Success

---

## Rule 2: Password Complexity Requirements

**Rule ID**: BR-002
**Category**: Validation Rule
**Priority**: High
**Status**: Draft / In Review / Approved

### Rule Definition
Password must meet complexity requirements.

### Business Context
Ensures account security and compliance with security standards.

### Validation Logic
```
Password MUST contain:
- At least 8 characters
- At least 1 uppercase letter
- At least 1 lowercase letter
- At least 1 number
- At least 1 special character (!@#$%^&*)

IF password DOES NOT meet ALL requirements
THEN reject with error "Password must contain at least 8 characters, including uppercase, lowercase, number, and special character"
```

### Error Messages
- "Password must contain at least 8 characters, including uppercase, lowercase, number, and special character"

### Dependencies
- BR-001: User Registration Validation

### Examples
- **Valid**: Password123!
- **Invalid**: password123 (no uppercase, no special char)
- **Invalid**: Password123 (no special char)

### Test Cases
- [ ] TC-006: Password with all requirements → Success
- [ ] TC-007: Password missing uppercase → Error
- [ ] TC-008: Password missing number → Error
- [ ] TC-009: Password missing special char → Error

---

## Rule 3: Cart Total Calculation

**Rule ID**: BR-003
**Category**: Computation Rule
**Priority**: High
**Status**: Draft / In Review / Approved

### Rule Definition
Cart total = Sum of (item price × quantity) + tax - discount

### Business Context
Ensures accurate pricing and order totals.

### Computation Logic
```
cart_total = 0
FOR EACH item IN cart:
  cart_total += item.price × item.quantity

tax = cart_total × tax_rate (e.g., 0.10 for 10%)
cart_total += tax

IF discount_code IS valid:
  discount_amount = cart_total × discount_percentage
  cart_total -= discount_amount

ROUND cart_total TO 2 decimal places
```

### Dependencies
- BR-004: Discount Code Validation
- Tax rate configuration

### Examples
- **Example 1**:
  - Item A: $10 × 2 = $20
  - Item B: $15 × 1 = $15
  - Subtotal: $35
  - Tax (10%): $3.50
  - Total: $38.50

- **Example 2**:
  - Subtotal: $100
  - Tax (10%): $10
  - Discount (10% off): -$10
  - Total: $100

### Test Cases
- [ ] TC-010: Calculate cart with single item
- [ ] TC-011: Calculate cart with multiple items
- [ ] TC-012: Calculate cart with tax
- [ ] TC-013: Calculate cart with discount
- [ ] TC-014: Calculate cart with tax and discount

---

## Rule 4: Discount Code Validation

**Rule ID**: BR-004
**Category**: Validation Rule
**Priority**: Medium
**Status**: Draft / In Review / Approved

### Rule Definition
Discount codes can only be applied if valid, not expired, and order meets minimum amount.

### Business Context
Controls promotional pricing and prevents fraud.

### Validation Logic
```
IF discount_code EXISTS AND IS active
  AND discount_code.expiry_date > current_date
  AND cart_total >= discount_code.minimum_amount
  AND discount_code.usage_count < discount_code.max_usage
THEN apply discount
ELSE reject with appropriate error message
```

### Error Messages
- "Invalid discount code": Code doesn't exist or is inactive
- "Discount code expired": Code has passed expiry date
- "Minimum order amount not met": Cart total below threshold
- "Discount code usage limit reached": Code has been used maximum times

### Dependencies
- BR-003: Cart Total Calculation
- Discount code management system

### Examples
- **Valid**: Code "SAVE10", min $50, 10% off, cart = $60 → Apply 10% discount
- **Invalid**: Code "SAVE10", min $50, cart = $40 → "Minimum order amount not met"

### Test Cases
- [ ] TC-015: Apply valid discount code → Success
- [ ] TC-016: Apply expired discount code → Error
- [ ] TC-017: Apply discount below minimum → Error
- [ ] TC-018: Apply discount after max usage → Error

---

## Rule 5: Order Status Transitions

**Rule ID**: BR-005
**Category**: Inference Rule
**Priority**: High
**Status**: Draft / In Review / Approved

### Rule Definition
Order status follows specific state transitions.

### Business Context
Ensures order processing follows correct workflow.

### State Machine
```
PENDING → PROCESSING → SHIPPED → DELIVERED
   ↓          ↓           ↓          ↓
CANCELLED  CANCELLED   RETURNED   RETURNED
   ↓          ↓
REFUNDED    REFUNDED
```

### Transition Rules
```
PENDING:
  - Can transition to: PROCESSING, CANCELLED
  - Triggered by: Payment confirmed, User cancellation

PROCESSING:
  - Can transition to: SHIPPED, CANCELLED, REFUNDED
  - Triggered by: Item shipped, Admin cancellation, Refund requested

SHIPPED:
  - Can transition to: DELIVERED, RETURNED
  - Triggered by: Delivery confirmed, Return requested

DELIVERED:
  - Can transition to: RETURNED
  - Triggered by: Return requested within 30 days

CANCELLED/REFUNDED/RETURNED:
  - Terminal states, no further transitions
```

### Error Messages
- "Invalid status transition": Attempting invalid state change

### Test Cases
- [ ] TC-019: PENDING → PROCESSING → Success
- [ ] TC-020: PENDING → SHIPPED → Error
- [ ] TC-021: DELIVERED → CANCELLED → Error

---

## Rule 6: Inventory Management

**Rule ID**: BR-006
**Category**: Action Enabler
**Priority**: High
**Status**: Draft / In Review / Approved

### Rule Definition
Inventory is reserved when order is placed and decremented when shipped.

### Business Context
Prevents overselling and ensures accurate inventory counts.

### Business Logic
```
WHEN order is created:
  - Reserve inventory for each item
  - IF available_quantity < order_quantity
    THEN reject order with "Insufficient inventory"
  - ELSE decrement available_quantity by order_quantity

WHEN order is shipped:
  - Mark inventory as shipped (no further changes)

WHEN order is cancelled/refunded:
  - Return inventory to available_quantity
```

### Error Messages
- "Insufficient inventory": Not enough stock to fulfill order

### Dependencies
- BR-005: Order Status Transitions
- Inventory management system

### Test Cases
- [ ] TC-022: Place order with sufficient inventory → Success
- [ ] TC-023: Place order with insufficient inventory → Error
- [ ] TC-024: Cancel order → Inventory returned
- [ ] TC-025: Ship order → Inventory marked as shipped

---

## Rule 7: Rate Limiting

**Rule ID**: BR-007
**Category**: Timing Rule
**Priority**: Medium
**Status**: Draft / In Review / Approved

### Rule Definition
API endpoints have rate limits to prevent abuse.

### Business Context
Protects system from abuse and ensures fair usage.

### Rate Limits
```
Authentication endpoints: 5 requests per minute per IP
API endpoints: 100 requests per minute per user
File upload: 10 requests per minute per user
Password reset: 3 requests per hour per email
```

### Enforcement Logic
```
IF request_count > rate_limit
WITHIN time_window
THEN return HTTP 429 (Too Many Requests)
AND include Retry-After header
```

### Error Messages
- HTTP 429: "Too many requests. Please try again in X seconds."

### Test Cases
- [ ] TC-026: Requests within limit → Success
- [ ] TC-027: Requests exceeding limit → 429 error
- [ ] TC-028: Retry after cooldown → Success

---

## Rule 8: Data Retention

**Rule ID**: BR-008
**Category**: Timing Rule
**Priority**: Medium
**Status**: Draft / In Review / Approved

### Rule Definition
User data is retained for a minimum period and deleted after retention period.

### Business Context
Compliance with data privacy regulations.

### Retention Periods
```
User accounts (active): Indefinite
User accounts (inactive): 3 years
Order history: 7 years
Analytics data: 2 years
Logs: 1 year
```

### Deletion Logic
```
WHEN user requests account deletion:
  - Anonymize personal data (name, email, address)
  - Retain order history for legal compliance (7 years)
  - Delete all other data
  - Send confirmation email

WHEN data exceeds retention period:
  - Automatically delete or anonymize
  - Log deletion action
```

### Compliance
- GDPR: Right to erasure
- SOC 2: Data retention policies

### Test Cases
- [ ] TC-029: Account deletion → Data anonymized
- [ ] TC-030: Retention period exceeded → Data deleted
- [ ] TC-031: Order history retained after account deletion

---

## Rule Maintenance

### Change Control
- All rule changes require BA and Tech Lead approval
- Version number incremented on change
- Change log maintained

### Review Schedule
- Monthly review of all rules
- Quarterly stakeholder review
- Annual audit and update

## Approval

- [ ] Business Analyst
- [ ] Product Owner
- [ ] Engineering Lead
- [ ] Legal/Compliance (if applicable)
