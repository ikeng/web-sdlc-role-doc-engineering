# ShopWave - Design System

## Metadata
- **Version**: 1.0
- **Authors**: Taylor Kim (UX Designer)
- **Date**: 2026-01-15
- **Project**: ShopWave
- **Status**: Approved

## Design Principles

### 1. Storytelling First
Highlight artisan stories and craftsmanship through design.

### 2. Transparency
Show materials, sourcing, and impact clearly.

### 3. Simplicity
Clean, uncluttered interfaces that let products shine.

### 4. Warmth
Inviting colors and imagery that feel human and approachable.

## Color System

### Primary Colors

| Token | Value | Usage |
|-------|-------|-------|
| `color-primary` | #2D5A3D | Primary buttons, links, active states |
| `color-primary-hover` | #1E3D2B | Primary button hover |
| `color-secondary` | #F4A261 | Accent buttons, highlights |
| `color-secondary-hover` | #E08E4A | Secondary button hover |

### Semantic Colors

| Token | Value | Usage |
|-------|-------|-------|
| `color-success` | #34C759 | Success messages |
| `color-warning` | #FF9500 | Warning messages |
| `color-error` | #FF3B30 | Error messages |
| `color-info` | #5AC8FA | Informational messages |

### Neutral Colors

| Token | Value | Usage |
|-------|-------|-------|
| `color-text-primary` | #1D1D1F | Headlines, body text |
| `color-text-secondary` | #6E6E73 | Subtitles, helper text |
| `color-background` | #FFFFFF | Page background |
| `color-surface` | #F5F5F7 | Card backgrounds |
| `color-border` | #D2D2D7 | Input borders, dividers |

## Typography

### Font Family
- **Primary**: Inter (headings, body)
- **Accent**: Playfair Display (product names, hero headlines)

### Type Scale

| Token | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| `text-h1` | 48px | 700 | 1.2 | Page titles |
| `text-h2` | 36px | 600 | 1.3 | Section titles |
| `text-h3` | 24px | 600 | 1.4 | Component titles |
| `text-body` | 16px | 400 | 1.5 | Body text |
| `text-small` | 14px | 400 | 1.5 | Helper text |

## Spacing System

**Base Unit**: 8px

| Token | Value | Usage |
|-------|-------|-------|
| `space-xs` | 4px | Tight spacing |
| `space-sm` | 8px | Component padding |
| `space-md` | 16px | Section padding |
| `space-lg` | 24px | Card padding |
| `space-xl` | 32px | Section spacing |

## Component Library

### Button
**Purpose**: Trigger actions
**Variants**: Primary, Secondary, Tertiary, Destructive
**Sizes**: Small, Medium, Large

### Product Card
**Purpose**: Display product information
**Content**: Image, name, price, artisan, "Add to Cart"
**States**: Default, Hover, Selected

### Input
**Purpose**: Collect user input
**Variants**: Default, Error, Success, Disabled
**States**: Default, Focus, Filled, Error

### Modal
**Purpose**: Focus user attention
**Variants**: Default, Fullscreen
**States**: Open, Closed

## Icon Library

- **Style**: Outline (default), Filled (active)
- **Size**: 24px (standard)
- **Color**: Inherit from text color

## Accessibility Standards

- WCAG 2.1 AA compliance
- Color contrast ≥ 4.5:1
- Keyboard navigation supported
- Screen reader compatible

## Usage Examples

### Do's
- ✅ Use consistent spacing and alignment
- ✅ Follow color system guidelines
- ✅ Use design tokens

### Don'ts
- ❌ Don't create new colors outside the system
- ❌ Don't use arbitrary spacing values
- ❌ Don't ignore accessibility requirements

## Approval

- [ ] Taylor Kim (UX Designer)
- [ ] Alex Rivera (Product Owner)
- [ ] Jordan Smith (Tech Lead)
