# Code Standards

## Metadata
- **Version**: 1.0
- **Author**: Tech Lead
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Status**: Draft / In Review / Approved

## Purpose

This document defines code style, structure, and quality standards for the project. All code must adhere to these standards to ensure consistency, maintainability, and quality.

## General Principles

### 1. Readability First
Code is read more than it is written. Prioritize clarity over cleverness.

### 2. DRY (Don't Repeat Yourself)
Avoid code duplication. Extract common logic into reusable functions or components.

### 3. KISS (Keep It Simple, Stupid)
Prefer simple solutions over complex ones. Avoid over-engineering.

### 4. YAGNI (You Aren't Gonna Need It)
Don't build functionality until it's needed.

## Naming Conventions

### General Rules
- Use descriptive, meaningful names
- Avoid abbreviations unless universally understood
- Use consistent casing for each type of identifier

### File Naming

**Frontend**:
- Components: `PascalCase` (e.g., `UserProfile.tsx`)
- Hooks: `camelCase` with `use` prefix (e.g., `useAuth.ts`)
- Utilities: `camelCase` (e.g., `formatDate.ts`)
- Types: `camelCase` with `.types.ts` suffix (e.g., `user.types.ts`)

**Backend**:
- Controllers: `camelCase` with `.controller.ts` suffix (e.g., `auth.controller.ts`)
- Services: `camelCase` with `.service.ts` suffix (e.g., `user.service.ts`)
- Models: `camelCase` with `.model.ts` suffix (e.g., `user.model.ts`)
- Middleware: `camelCase` with `.middleware.ts` suffix (e.g., `auth.middleware.ts`)

### Variable Naming
- Use `camelCase` for variables and functions
- Use `PascalCase` for classes and components
- Use `UPPER_SNAKE_CASE` for constants
- Use descriptive names: `userCount` not `uc`

### Function Naming
- Use verbs for functions: `getUser()`, `calculateTotal()`, `validateEmail()`
- Use descriptive names that explain what the function does
- Boolean functions should start with `is`, `has`, `should`: `isValid()`, `hasPermission()`

### Class Naming
- Use `PascalCase`
- Use nouns: `UserService`, `AuthController`, `ProductModel`

### Constant Naming
- Use `UPPER_SNAKE_CASE`
- Examples: `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT`, `API_BASE_URL`

## Code Structure

### File Organization

**Frontend**:
```
src/
├── components/           # Reusable UI components
│   ├── common/          # Shared components (Button, Input, etc.)
│   ├── forms/           # Form components
│   └── layouts/         # Layout components
├── hooks/               # Custom React hooks
├── pages/               # Page components
├── services/            # API service functions
├── utils/               # Utility functions
├── types/               # TypeScript type definitions
├── styles/              # Global styles
└── App.tsx              # Root component
```

**Backend**:
```
src/
├── controllers/         # Request handlers
├── services/           # Business logic
├── models/             # Data models
├── middleware/         # Express middleware
├── routes/            # Route definitions
├── utils/             # Utility functions
├── config/            # Configuration files
├── types/             # TypeScript type definitions
└── app.ts             # Express app setup
```

### Function Structure
- Keep functions small (ideally < 50 lines)
- Single responsibility: one function, one purpose
- Max 3-4 parameters (use object parameter for more)
- Early returns to reduce nesting

### Class Structure
- Single responsibility principle
- Max 200-300 lines per class
- Group related methods together
- Use access modifiers (public, private, protected)

## Commenting & Documentation

### When to Comment
- Explain **why**, not **what** (code shows what)
- Document complex algorithms or business logic
- Explain workarounds or non-obvious decisions
- Document public APIs and functions

### When NOT to Comment
- Don't state the obvious (e.g., `// increment i` before `i++`)
- Don't leave commented-out code (use version control)
- Don't use comments to justify bad code (fix the code instead)

### JSDoc Comments
```typescript
/**
 * Calculates the total price including tax.
 * @param price - Base price before tax
 * @param taxRate - Tax rate as decimal (e.g., 0.1 for 10%)
 * @returns Total price with tax applied
 * @example
 * calculateTotal(100, 0.1) // Returns 110
 */
function calculateTotal(price: number, taxRate: number): number {
  return price * (1 + taxRate);
}
```

## Error Handling

### Principles
- Fail fast: validate input early
- Provide meaningful error messages
- Log errors with context
- Don't swallow errors silently

### Error Handling Patterns

**Frontend**:
```typescript
try {
  const data = await fetchData();
  return data;
} catch (error) {
  if (error instanceof ApiError) {
    // Handle API error
    toast.error(error.message);
  } else {
    // Handle unexpected error
    toast.error('An unexpected error occurred');
    logError(error);
  }
  throw error; // Re-throw for caller to handle
}
```

**Backend**:
```typescript
try {
  const user = await userService.findById(id);
  return res.json({ data: user });
} catch (error) {
  if (error instanceof NotFoundError) {
    return res.status(404).json({
      error: { code: 'NOT_FOUND', message: 'User not found' }
    });
  }
  logError(error);
  return res.status(500).json({
    error: { code: 'INTERNAL_ERROR', message: 'An error occurred' }
  });
}
```

### Custom Errors
Create custom error classes for different error types:
```typescript
class ValidationError extends Error {
  constructor(public field: string, message: string) {
    super(message);
    this.name = 'ValidationError';
  }
}

class NotFoundError extends Error {
  constructor(resource: string, id: string) {
    super(`${resource} with id ${id} not found`);
    this.name = 'NotFoundError';
  }
}
```

## Logging Standards

### Log Levels
- **ERROR**: System errors requiring immediate attention
- **WARN**: Potential issues that don't block execution
- **INFO**: General informational messages (startup, shutdown, major events)
- **DEBUG**: Detailed debugging information (development only)

### What to Log
- **ERROR**: Stack trace, context (user ID, request ID), timestamp
- **WARN**: Warning message, context
- **INFO**: Request start/end, user actions (login, logout), system events
- **DEBUG**: Variable values, execution flow (dev only)

### What NOT to Log
- Passwords or secrets
- PII (email, phone, address) in production
- Full request/response bodies in production
- Sensitive API keys or tokens

### Log Format
```json
{
  "timestamp": "2026-01-15T10:30:00.000Z",
  "level": "error",
  "message": "Failed to process payment",
  "context": {
    "userId": "uuid",
    "orderId": "uuid",
    "paymentMethod": "stripe"
  },
  "error": {
    "name": "PaymentError",
    "message": "Insufficient funds",
    "stack": "..."
  }
}
```

## Testing Requirements

### Test Coverage
- **Minimum**: 80% code coverage
- **Target**: 90%+ for critical paths
- **Required**: All business logic, utility functions, API endpoints

### Test Structure
```typescript
describe('calculateTotal', () => {
  it('should calculate total with tax', () => {
    // Arrange
    const price = 100;
    const taxRate = 0.1;

    // Act
    const result = calculateTotal(price, taxRate);

    // Assert
    expect(result).toBe(110);
  });

  it('should handle zero tax rate', () => {
    // Test case
  });

  it('should handle negative price', () => {
    // Test case
  });
});
```

### Test Naming
- Use descriptive test names: `should return error when email is invalid`
- Test one thing per test case
- Use `describe` blocks to group related tests

## Performance Guidelines

### Frontend
- Lazy load routes and components
- Optimize images (WebP, lazy loading, responsive images)
- Minimize re-renders (React.memo, useMemo, useCallback)
- Use virtual scrolling for long lists
- Bundle size monitoring (keep under 300KB initial load)

### Backend
- Use database indexes on frequently queried fields
- Implement caching (Redis) for frequently accessed data
- Use connection pooling for database
- Implement pagination for list endpoints
- Use compression (gzip) for responses

## Security Best Practices

### Input Validation
- Validate all user input on both client and server
- Use parameterized queries to prevent SQL injection
- Sanitize HTML to prevent XSS
- Validate file uploads (type, size, content)

### Authentication & Authorization
- Use bcrypt for password hashing (cost factor 12)
- Implement JWT with short expiry (15 minutes)
- Store refresh tokens securely (HTTP-only cookies)
- Implement rate limiting on auth endpoints
- Use HTTPS everywhere in production

### Data Protection
- Encrypt sensitive data at rest
- Never log passwords, tokens, or PII
- Use environment variables for secrets
- Implement CORS properly

## Code Review Standards

All code must be reviewed before merging:
- At least one approval required
- CI checks must pass (lint, test, build)
- No console.log statements (use logger)
- No commented-out code
- No hardcoded values (use constants)
- Proper error handling implemented

## Approval

- [ ] Tech Lead
- [ ] All Developers
