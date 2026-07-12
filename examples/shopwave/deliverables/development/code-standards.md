# ShopWave - Code Standards

## Metadata
- **Version**: 1.0
- **Author**: Morgan Lee (Tech Lead)
- **Date**: 2026-01-15
- **Project**: ShopWave
- **Status**: Approved

## Purpose

This document defines code style, structure, and quality standards for ShopWave. All code must adhere to these standards.

## General Principles

1. **Readability First**: Code is read more than written
2. **DRY**: Don't repeat yourself
3. **KISS**: Keep it simple
4. **YAGNI**: Don't build until needed

## Naming Conventions

### File Naming

**Frontend**:
- Components: `PascalCase` (e.g., `ProductCard.tsx`)
- Hooks: `camelCase` with `use` prefix (e.g., `useCart.ts`)
- Utilities: `camelCase` (e.g., `formatPrice.ts`)
- Types: `camelCase` with `.types.ts` suffix

**Backend**:
- Controllers: `camelCase` with `.controller.ts` suffix
- Services: `camelCase` with `.service.ts` suffix
- Models: `camelCase` with `.model.ts` suffix
- Middleware: `camelCase` with `.middleware.ts` suffix

### Variable Naming
- `camelCase` for variables and functions
- `PascalCase` for classes and components
- `UPPER_SNAKE_CASE` for constants

### Function Naming
- Use verbs: `getUser()`, `calculateTotal()`, `validateEmail()`
- Boolean functions start with `is`, `has`, `should`: `isValid()`, `hasPermission()`

## Code Structure

### Frontend Structure
```
src/
├── components/           # Reusable UI components
│   ├── common/          # Button, Input, Card
│   ├── product/         # ProductCard, ProductList
│   └── cart/            # CartDrawer, CartItem
├── hooks/               # Custom React hooks
├── pages/               # Page components
├── services/            # API service functions
├── utils/               # Utility functions
├── types/               # TypeScript type definitions
├── styles/              # Global styles
└── App.tsx              # Root component
```

### Backend Structure
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

## Commenting & Documentation

### When to Comment
- Explain **why**, not **what**
- Document complex algorithms
- Explain workarounds

### JSDoc Example
```typescript
/**
 * Calculates the total price including tax.
 * @param price - Base price before tax
 * @param taxRate - Tax rate as decimal (e.g., 0.08 for 8%)
 * @returns Total price with tax applied
 */
function calculateTotal(price: number, taxRate: number): number {
  return price * (1 + taxRate);
}
```

## Error Handling

### Frontend
```typescript
try {
  const data = await fetchData();
  return data;
} catch (error) {
  if (error instanceof ApiError) {
    toast.error(error.message);
  } else {
    toast.error('An unexpected error occurred');
  }
  throw error;
}
```

### Backend
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

## Testing Requirements

### Test Coverage
- Minimum: 80% code coverage
- Target: 90%+ for critical paths

### Test Structure
```typescript
describe('calculateTotal', () => {
  it('should calculate total with tax', () => {
    expect(calculateTotal(100, 0.08)).toBe(108);
  });
});
```

## Performance Guidelines

### Frontend
- Lazy load routes and components
- Optimize images (WebP, lazy loading)
- Minimize re-renders

### Backend
- Use database indexes
- Implement caching (Redis)
- Use connection pooling
- Implement pagination

## Security Best Practices

### Input Validation
- Validate all user input
- Use parameterized queries
- Sanitize HTML

### Authentication & Authorization
- Use bcrypt for password hashing (cost factor 12)
- Implement JWT with short expiry (15 minutes)
- Store secrets in environment variables

## Code Review Standards

All code must be reviewed before merging:
- At least one approval required
- CI checks must pass
- No console.log statements
- No commented-out code
- No hardcoded values

## Approval

- [ ] Morgan Lee (Tech Lead)
- [ ] All Developers
