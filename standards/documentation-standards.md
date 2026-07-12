# Documentation Standards

## Purpose

This document defines documentation standards to ensure consistency, clarity, and completeness across all SDLC artifacts.

## Document Structure

### Standard Document Format

All documents must follow this structure:

1. **Metadata** (required)
2. **Purpose** (required)
3. **Content** (varies by document type)
4. **Quality Gates** (required)
5. **Approval** (required)

### Metadata Section

```yaml
---
version: 1.0
author: [Name]
date: YYYY-MM-DD
status: Draft / In Review / Approved
reviewers: [Name 1, Name 2]
---
```

**Required Fields**:
- `version`: Document version (SemVer)
- `author`: Document author
- `date`: Creation/last update date
- `status`: Current status

**Optional Fields**:
- `reviewers`: List of reviewers
- `project`: Project name
- `sprint`: Sprint number

### Purpose Section

```markdown
## Purpose

[1-2 sentences describing what this document is for and who should use it.]
```

### Content Section

Organize content with clear headings:
```markdown
## Section 1

### Subsection 1.1

Content here...

### Subsection 1.2

Content here...

## Section 2

Content here...
```

### Quality Gates Section

```markdown
## Quality Gates

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3
```

### Approval Section

```markdown
## Approval

- [ ] Role 1
- [ ] Role 2
- [ ] Role 3
```

## Writing Style

### Clarity
- Use clear, concise language
- Avoid jargon and acronyms
- Define technical terms on first use
- Use active voice

### Consistency
- Use consistent terminology
- Follow naming conventions
- Use consistent formatting
- Use consistent structure

### Completeness
- Cover all required sections
- Provide examples where helpful
- Link to related documents
- Include all necessary details

### Readability
- Use short paragraphs (3-5 sentences)
- Use bullet points for lists
- Use tables for structured data
- Use code blocks for code examples

## Formatting

### Headings
- Use `##` for main sections
- Use `###` for subsections
- Use `####` for sub-subsections
- Don't skip heading levels

### Lists
- Use `-` for unordered lists
- Use `1.` for ordered lists
- Indent nested items with 2 spaces

### Code Blocks
- Use triple backticks with language identifier
- Example: ` ```javascript `
- Include syntax highlighting when possible

### Tables
- Use Markdown tables
- Align columns for readability
- Include header row

### Emphasis
- Use `**bold**` for emphasis
- Use `*italic*` for subtle emphasis
- Use `` `code` `` for code references

### Links
- Use descriptive link text
- Example: `[User Stories](./user-stories.md)`
- Avoid "click here" or "here"

## Examples (Few-Shot)

Provide examples for complex concepts:

```markdown
## Example

**User Story**:
```
As a registered user
I want to reset my password
So that I can regain access if I forget it
```
```

## Templates

- Use templates from `../templates/` directory
- Don't modify template structure
- Replace all placeholders with actual values
- Remove optional sections if not applicable

## Versioning

### Document Versioning
- Follow SemVer: `MAJOR.MINOR.PATCH`
- Increment MAJOR for breaking changes
- Increment MINOR for new features
- Increment PATCH for bug fixes

### Change Log

```markdown
## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | YYYY-MM-DD | Initial version | [Name] |
| 1.1 | YYYY-MM-DD | Added section X | [Name] |
```

## Review Process

### Document Review
1. Author creates document
2. Author reviews for completeness
3. Reviewers provide feedback
4. Author addresses feedback
5. Document is approved
6. Document is published

### Review Criteria
- [ ] All required sections present
- [ ] Content is accurate and complete
- [ ] Examples are provided where needed
- [ ] Quality gates are defined
- [ ] Approval section is complete
- [ ] Formatting is correct

## Maintenance

### Regular Updates
- Review documents quarterly
- Update when processes change
- Archive outdated documents

### Change Management
- Document all changes
- Notify stakeholders of significant changes
- Update version number
- Update change log

## Quality Gates

- [ ] Document follows standard structure
- [ ] Metadata is complete
- [ ] Content is clear and complete
- [ ] Examples are provided
- [ ] Quality gates are defined
- [ ] Approval section is complete
- [ ] Formatting is consistent

## Approval

- [ ] Tech Lead
- [ ] Project Manager
- [ ] QA Engineer
