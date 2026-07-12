# Development Guidelines

## Metadata
- **Version**: 1.0
- **Author**: Tech Lead
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Status**: Draft / In Review / Approved

## Purpose

This document provides development guidelines and best practices for the team. Follow these guidelines to ensure consistent, high-quality code.

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
- `style`: Code style changes (formatting, etc.)
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

1. **Create feature branch** from `main`
2. **Implement changes** following code standards
3. **Write tests** for new functionality
4. **Run tests locally**: `npm test`
5. **Run linter**: `npm run lint`
6. **Create PR** with descriptive title and description
7. **Request review** from at least one team member
8. **Address review comments**
9. **Squash and merge** after approval
10. **Delete feature branch**

**PR Description Template**:
```markdown
## Summary
[Brief description of changes]

## Changes
- [Change 1]
- [Change 2]
- [Change 3]

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Screenshots (if applicable)
[Before/after screenshots]

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed the code
- [ ] Commented complex logic
- [ ] Updated documentation
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
    expect(calculateTotal(100, 0.1)).toBe(110);
  });

  it('should handle zero tax rate', () => {
    expect(calculateTotal(100, 0)).toBe(100);
  });

  it('should handle negative price', () => {
    expect(() => calculateTotal(-100, 0.1)).toThrow('Price cannot be negative');
  });
});
```

### Integration Tests
- Test API endpoints end-to-end
- Test database interactions
- Test external service integrations
- Use test database (not production)

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
    expect(response.body.data.email).toBe('test@example.com');
  });
});
```

### E2E Tests
- Test critical user flows
- Test across different browsers
- Test responsive design
- Run in CI/CD pipeline

**Example (Playwright)**:
```typescript
test('user can login and view dashboard', async ({ page }) => {
  await page.goto('https://app.example.com/login');
  await page.fill('[data-testid=email]', 'user@example.com');
  await page.fill('[data-testid=password]', 'password');
  await page.click('[data-testid=login-button]');
  await page.waitForURL('https://app.example.com/dashboard');
  await expect(page.locator('h1')).toContainText('Dashboard');
});
```

## Debugging & Troubleshooting

### Frontend Debugging
- Use React DevTools for component debugging
- Use Redux DevTools for state debugging
- Use browser DevTools for network requests
- Use source maps for debugging minified code

### Backend Debugging
- Use console.log or logger for debugging (remove before commit)
- Use debugger statement for breakpoints
- Use Postman/Insomnia for API testing
- Check logs for errors

### Common Issues
- **CORS errors**: Check CORS configuration
- **401 errors**: Check JWT token validity
- **500 errors**: Check server logs for stack trace
- **Slow queries**: Check database query performance
- **Memory leaks**: Use Chrome DevTools Memory tab

## Performance Optimization

### Frontend
- Lazy load routes and components
- Optimize images (WebP, lazy loading)
- Minimize re-renders (React.memo, useMemo)
- Use virtual scrolling for long lists
- Code splitting for large bundles

### Backend
- Database indexing on frequently queried fields
- Caching with Redis
- Connection pooling
- Pagination for list endpoints
- Response compression (gzip)

## Security Guidelines

### Input Validation
- Validate all user input
- Sanitize HTML to prevent XSS
- Use parameterized queries to prevent SQL injection
- Validate file uploads

### Authentication & Authorization
- Use bcrypt for password hashing
- Implement JWT with short expiry
- Store secrets in environment variables
- Implement rate limiting

### Data Protection
- Encrypt sensitive data
- Never log passwords or tokens
- Use HTTPS in production
- Implement CORS properly

## Accessibility Guidelines

### WCAG 2.1 AA Compliance
- All images have alt text
- Form inputs have labels
- Sufficient color contrast (4.5:1)
- Keyboard navigation supported
- Screen reader compatible

### Testing Accessibility
- Use axe DevTools for automated testing
- Test with keyboard only
- Test with screen reader (NVDA, VoiceOver)
- Check color contrast with tools

## Internationalization (i18n)

### Guidelines
- Use i18n library (react-i18next)
- Store all user-facing text in translation files
- Support multiple languages
- Format dates, numbers, currencies per locale

**Example**:
```typescript
import { useTranslation } from 'react-i18next';

function Welcome() {
  const { t } = useTranslation();
  return <h1>{t('welcome.title')}</h1>;
}
```

## Common Patterns & Anti-Patterns

### ✅ Good Patterns

**Early Returns**:
```typescript
function processUser(user: User | null) {
  if (!user) {
    return null;
  }

  if (!user.email) {
    throw new Error('Email required');
  }

  // Process user
}
```

**Destructuring**:
```typescript
const { name, email } = user;
```

**Async/Await**:
```typescript
async function fetchUser(id: string) {
  try {
    const user = await userService.findById(id);
    return user;
  } catch (error) {
    logError(error);
    throw error;
  }
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

**Deep Nesting**:
```typescript
// Bad
if (user) {
  if (user.profile) {
    if (user.profile.settings) {
      if (user.profile.settings.notifications) {
        // Deeply nested
      }
    }
  }
}

// Good
if (!user?.profile?.settings?.notifications) {
  return;
}
// Handle case
```

**Callbacks (use Promises)**:
```typescript
// Bad
getUser(id, function(err, user) {
  if (err) {
    // Handle error
  }
});

// Good
try {
  const user = await getUser(id);
} catch (error) {
  // Handle error
}
```

## Code Review Best Practices

### As a Reviewer
- Be constructive and respectful
- Explain the "why" behind suggestions
- Prioritize issues (critical, important, nice-to-have)
- Provide examples when suggesting improvements
- Approve when code meets standards

### As an Author
- Be open to feedback
- Don't take criticism personally
- Ask questions if feedback is unclear
- Make requested changes or explain why not
- Thank reviewers for their time

## Approval

- [ ] Tech Lead
- [ ] All Developers
