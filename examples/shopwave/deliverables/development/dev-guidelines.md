# ShopWave - Development Guidelines

## Metadata
- **Version**: 1.0
- **Author**: Morgan Lee (Tech Lead)
- **Date**: 2026-01-15
- **Project**: ShopWave
- **Status**: Approved

## Purpose

This document provides development guidelines and best practices for the ShopWave team.

## Development Workflow

### Git Workflow

**Branching Strategy**: GitHub Flow
- `main`: Production-ready code
- `feature/*`: New features
- `fix/*`: Bug fixes
- `hotfix/*`: Critical production fixes

**Commit Convention**: Conventional Commits
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples**:
```
feat(auth): add password reset functionality

Implements password reset via email with token-based verification.

Closes #123
```

```
fix(api): handle null response in user endpoint

Prevents crash when user data is missing.

Fixes #456
```

### Pull Request Process

1. Create feature branch from `main`
2. Implement changes following code standards
3. Write tests for new functionality
4. Run tests locally: `npm test`
5. Run linter: `npm run lint`
6. Create PR with descriptive title and description
7. Request review from at least one team member
8. Address review comments
9. Squash and merge after approval
10. Delete feature branch

**PR Description Template**:
```markdown
## Summary
[Brief description of changes]

## Changes
- [Change 1]
- [Change 2]

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] No new warnings
```

## Testing Requirements

### Unit Tests
- Test all business logic
- Test edge cases and error conditions
- Mock external dependencies
- Aim for 80%+ coverage

**Example**:
```typescript
describe('calculateTotal', () => {
  it('should calculate total with tax', () => {
    expect(calculateTotal(100, 0.08)).toBe(108);
  });

  it('should handle zero tax rate', () => {
    expect(calculateTotal(100, 0)).toBe(100);
  });
});
```

### Integration Tests
- Test API endpoints end-to-end
- Test database interactions
- Use test database

**Example**:
```typescript
describe('POST /api/auth/register', () => {
  it('should register a new user', async () => {
    const response = await request(app)
      .post('/api/auth/register')
      .send({
        email: 'test@example.com',
        password: 'SecurePass123!',
        name: 'Test User'
      });

    expect(response.status).toBe(201);
    expect(response.body.data).toHaveProperty('id');
  });
});
```

### E2E Tests
- Test critical user flows
- Test across different browsers
- Run in CI/CD

**Example (Playwright)**:
```typescript
test('user can login and view dashboard', async ({ page }) => {
  await page.goto('https://shopwave.com/login');
  await page.fill('[data-testid=email]', 'user@example.com');
  await page.fill('[data-testid=password]', 'password');
  await page.click('[data-testid=login-button]');
  await page.waitForURL('https://shopwave.com/dashboard');
  await expect(page.locator('h1')).toContainText('Dashboard');
});
```

## Debugging & Troubleshooting

### Frontend Debugging
- Use React DevTools for component debugging
- Use browser DevTools for network requests
- Use source maps for debugging minified code

### Backend Debugging
- Use console.log or logger for debugging
- Use debugger statement for breakpoints
- Use Postman/Insomnia for API testing

## Performance Optimization

### Frontend
- Lazy load routes and components
- Optimize images (WebP, lazy loading)
- Minimize re-renders (React.memo, useMemo)

### Backend
- Database indexing on frequently queried fields
- Caching with Redis
- Connection pooling
- Pagination for list endpoints

## Security Guidelines

### Input Validation
- Validate all user input
- Sanitize HTML to prevent XSS
- Use parameterized queries to prevent SQL injection

### Authentication & Authorization
- Use bcrypt for password hashing
- Implement JWT with short expiry
- Store secrets in environment variables

## Accessibility Guidelines

### WCAG 2.1 AA Compliance
- All images have alt text
- Form inputs have labels
- Sufficient color contrast (4.5:1)
- Keyboard navigation supported

## Common Patterns & Anti-Patterns

### ✅ Good Patterns

**Early Returns**:
```typescript
function processUser(user: User | null) {
  if (!user) {
    return null;
  }
  // Process user
}
```

### ❌ Anti-Patterns to Avoid

**Magic Numbers**:
```typescript
// Bad
if (user.age > 18) { }

// Good
if (user.age > LEGAL_AGE) { }
```

## Code Review Best Practices

### As a Reviewer
- Be constructive and respectful
- Explain the "why" behind suggestions
- Prioritize issues (critical, important, nice-to-have)

### As an Author
- Be open to feedback
- Ask questions if feedback is unclear
- Make requested changes or explain why not

## Approval

- [ ] Morgan Lee (Tech Lead)
- [ ] All Developers
