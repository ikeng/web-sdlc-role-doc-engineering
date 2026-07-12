# Naming Conventions

## Purpose

This document defines naming conventions for files, directories, versions, and metadata to ensure consistency across the SDLC framework.

## File Naming

### General Rules
- Use lowercase letters
- Use hyphens (`-`) to separate words
- Avoid spaces and special characters
- Be descriptive but concise

### File Types

**Documents**:
- Format: `{type}-{name}.md`
- Examples:
  - `product-vision.md`
  - `requirements-spec.md`
  - `architecture-doc.md`
  - `test-plan.md`

**Templates**:
- Format: `{type}-template.md`
- Examples:
  - `user-story-template.md`
  - `requirements-spec-template.md`

**Standards**:
- Format: `{type}-standards.md`
- Examples:
  - `code-review-standards.md`
  - `documentation-standards.md`

### Directory Naming

**Use lowercase with hyphens**:
- ✅ `product-backlog`
- ✅ `use-case-diagram`
- ❌ `ProductBacklog`
- ❌ `product_backlog`

### Special Cases

**Role files**: Use role name in kebab-case
- `product-owner.md`
- `business-analyst.md`
- `ux-designer.md`
- `solution-architect.md`
- `tech-lead.md`
- `fullstack-developer.md`
- `qa-engineer.md`
- `devops-engineer.md`
- `project-manager.md`
- `security-engineer.md`

## Version Numbering

### Semantic Versioning (SemVer)

Format: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, backward compatible

**Examples**:
- `1.0.0` - Initial release
- `1.1.0` - Added new features
- `1.1.1` - Fixed bugs
- `2.0.0` - Breaking changes

### Document Versions

Include version in document metadata:
```yaml
---
version: 1.0
date: YYYY-MM-DD
---
```

## Metadata Standards

### Required Metadata Fields

All documents must include:
```yaml
---
version: 1.0
author: [Name]
date: YYYY-MM-DD
status: Draft / In Review / Approved
---
```

### Optional Metadata Fields

```yaml
---
reviewers: [Name 1, Name 2]
project: [Project Name]
sprint: [Sprint Number]
---
```

## ID Conventions

### User Story IDs
- Format: `US-{number}`
- Examples: `US-001`, `US-002`, `US-100`

### Test Case IDs
- Format: `TC-{number}`
- Examples: `TC-001`, `TC-002`, `TC-100`

### Requirement IDs
- Functional Requirements: `FR-{number}`
- Non-Functional Requirements: `NFR-{category}-{number}`
- Examples:
  - `FR-001`
  - `NFR-P-001` (Performance)
  - `NFR-S-001` (Security)
  - `NFR-R-001` (Reliability)

### Risk IDs
- Format: `RISK-{number}`
- Examples: `RISK-001`, `RISK-002`

### Task IDs
- Format: `T-{number}`
- Examples: `T-001`, `T-002`

### Bug/Defect IDs
- Format: `DEF-{number}`
- Examples: `DEF-001`, `DEF-002`

## Git Conventions

### Branch Naming
- Feature branches: `feature/{story-id}-{description}`
  - Example: `feature/US-001-user-authentication`
- Bug fix branches: `fix/{bug-id}-{description}`
  - Example: `fix/DEF-001-login-redirect`
- Hotfix branches: `hotfix/{bug-id}-{description}`
  - Example: `hotfix/DEF-005-security-patch`

### Commit Messages
Follow Conventional Commits:
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

## Tag Conventions

### Document Tags
Use tags to categorize documents:
- `#product` - Product-related documents
- `#analysis` - Analysis documents
- `#design` - Design documents
- `#architecture` - Architecture documents
- `#development` - Development documents
- `#quality` - Quality assurance documents
- `#deployment` - Deployment documents
- `#project` - Project management documents
- `#security` - Security documents

### Status Tags
- `#draft` - Document in draft state
- `#review` - Document under review
- `#approved` - Document approved
- `#deprecated` - Document no longer valid

## Approval

- [ ] Tech Lead
- [ ] Project Manager
