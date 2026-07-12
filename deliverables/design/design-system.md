# Design System

## Metadata
- **Version**: 1.0
- **Authors**: [UX/UI Designer]
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Status**: Draft / In Review / Approved

## Design Principles

### 1. Clarity
Design should be intuitive and easy to understand. Users should never have to guess what something does.

### 2. Consistency
Use the same patterns, components, and terminology throughout the product.

### 3. Efficiency
Minimize user effort. Reduce steps, provide defaults, and automate where possible.

### 4. Feedback
Every action should have a clear, immediate response.

### 5. Accessibility
Design for all users, including those with disabilities. Meet WCAG 2.1 AA standards.

### 6. Performance
Design should load quickly and respond instantly to user interactions.

## Color System

### Primary Colors

| Token | Value | Usage |
|-------|-------|-------|
| `color-primary` | #007AFF | Primary buttons, links, active states |
| `color-primary-hover` | #0056CC | Primary button hover |
| `color-primary-active` | #004BB5 | Primary button active |
| `color-primary-light` | #E6F2FF | Primary color background tints |

### Secondary Colors

| Token | Value | Usage |
|-------|-------|-------|
| `color-secondary` | #5856D6 | Secondary buttons, accents |
| `color-secondary-hover` | #4342B8 | Secondary button hover |
| `color-secondary-active` | #3A39A8 | Secondary button active |

### Semantic Colors

| Token | Value | Usage |
|-------|-------|-------|
| `color-success` | #34C759 | Success messages, positive actions |
| `color-success-light` | #E8F8ED | Success backgrounds |
| `color-warning` | #FF9500 | Warning messages, caution states |
| `color-warning-light` | #FFF3E6 | Warning backgrounds |
| `color-error` | #FF3B30 | Error messages, destructive actions |
| `color-error-light` | #FFE6E6 | Error backgrounds |
| `color-info` | #5AC8FA | Informational messages |
| `color-info-light` | #E6F7FD | Info backgrounds |

### Neutral Colors

| Token | Value | Usage |
|-------|-------|-------|
| `color-text-primary` | #1D1D1F | Headlines, body text |
| `color-text-secondary` | #6E6E73 | Subtitles, helper text |
| `color-text-tertiary` | #8E8E93 | Disabled text, placeholders |
| `color-background` | #FFFFFF | Page background |
| `color-surface` | #F5F5F7 | Card backgrounds, sections |
| `color-border` | #D2D2D7 | Input borders, dividers |

### Color Usage Guidelines
- **Primary**: Use for primary actions and key interactive elements
- **Secondary**: Use for secondary actions and accents
- **Semantic**: Use sparingly for status and feedback
- **Neutral**: Use for text, backgrounds, and borders

## Typography

### Font Family
- **Primary**: Inter (headings, body text)
- **Monospace**: SF Mono (code, technical content)

### Type Scale

| Token | Size | Weight | Line Height | Letter Spacing | Usage |
|-------|------|--------|-------------|----------------|-------|
| `text-h1` | 48px | 700 | 1.2 | -0.02em | Page titles |
| `text-h2` | 36px | 600 | 1.3 | -0.01em | Section titles |
| `text-h3` | 24px | 600 | 1.4 | 0em | Component titles |
| `text-h4` | 20px | 600 | 1.4 | 0em | Card titles |
| `text-body` | 16px | 400 | 1.5 | 0em | Body text |
| `text-small` | 14px | 400 | 1.5 | 0em | Helper text |
| `text-caption` | 12px | 400 | 1.4 | 0.01em | Labels, captions |

### Typography Usage Guidelines
- **Headlines**: Bold, high contrast, limited to 2-3 lines
- **Body**: Readable line height (1.5), adequate line length (50-75 chars)
- **Helper Text**: Smaller size, lower contrast, supportive role

## Spacing System

### Base Unit: 8px

| Token | Value | Usage |
|-------|-------|-------|
| `space-xs` | 4px | Tight spacing, icon padding |
| `space-sm` | 8px | Component padding, gaps |
| `space-md` | 16px | Section padding |
| `space-lg` | 24px | Large gaps, card padding |
| `space-xl` | 32px | Section spacing |
| `space-2xl` | 48px | Large section spacing |
| `space-3xl` | 64px | Hero section spacing |

### Spacing Guidelines
- Use consistent spacing multiples of 8px
- Maintain visual hierarchy through spacing
- Use whitespace to group related elements

## Elevation System

### Shadows

| Token | Shadow | Usage |
|-------|--------|-------|
| `shadow-sm` | 0 1px 3px rgba(0,0,0,0.1) | Small elements, inputs |
| `shadow-md` | 0 4px 6px rgba(0,0,0,0.1) | Cards, dropdowns |
| `shadow-lg` | 0 10px 15px rgba(0,0,0,0.1) | Modals, popovers |
| `shadow-xl` | 0 20px 25px rgba(0,0,0,0.15) | Large modals |

### Z-Index Scale

| Token | Value | Usage |
|-------|-------|-------|
| `z-base` | 0 | Base layer |
| `z-dropdown` | 100 | Dropdowns |
| `z-sticky` | 200 | Sticky headers |
| `z-modal` | 300 | Modals |
| `z-tooltip` | 400 | Tooltips |

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `radius-sm` | 4px | Small buttons, inputs |
| `radius-md` | 8px | Cards, buttons |
| `radius-lg` | 12px | Large cards |
| `radius-xl` | 16px | Modals, panels |
| `radius-full` | 9999px | Pills, avatars |

## Component Library

### Button

**Purpose**: Trigger actions and navigation

**Variants**:
- Primary: Main action, high emphasis
- Secondary: Secondary action, medium emphasis
- Tertiary: Low emphasis, minimal visual weight
- Destructive: Dangerous actions (delete, remove)

**Sizes**:
- Small: Compact spaces, inline actions
- Medium: Standard UI elements
- Large: Hero sections, primary CTAs

**States**:
- Default, Hover, Active, Focus, Disabled, Loading

### Input

**Purpose**: Collect user input

**Variants**:
- Default: Standard input
- Error: Validation error state
- Success: Validation success state
- Disabled: Non-interactive state

**States**:
- Default, Focus, Filled, Error, Disabled

### Card

**Purpose**: Group related content

**Variants**:
- Default: Standard card
- Elevated: Prominent card with shadow
- Outlined: Minimal card with border

**States**:
- Default, Hover, Selected, Disabled

### Navigation

**Purpose**: Site and app navigation

**Variants**:
- Top Nav: Primary navigation bar
- Side Nav: Secondary navigation
- Bottom Nav: Mobile navigation
- Breadcrumbs: Hierarchical navigation

### Modal

**Purpose**: Focus user attention on critical content

**Variants**:
- Default: Standard modal
- Fullscreen: Mobile-optimized
- Center: Centered on screen

**States**:
- Open, Closed, Closing

## Icon Library

### Icon System
- **Style**: Outline (default), Filled (active state)
- **Size**: 16px (small), 24px (medium), 32px (large)
- **Stroke Width**: 2px
- **Color**: Inherit from text color or use semantic colors

### Usage Guidelines
- Use icons to reinforce text, not replace it
- Maintain consistent icon style across product
- Provide alt text or aria-label for accessibility

## Illustration & Imagery

### Illustration Style
- **Style**: Flat, minimal, geometric
- **Colors**: Use design system colors
- **Purpose**: Support content, not decoration

### Photography
- **Style**: Authentic, diverse, inclusive
- **Format**: WebP (preferred), JPEG (fallback)
- **Resolution**: 2x for retina displays

## Animation & Motion

### Timing
- **Fast**: 150ms (hover effects)
- **Normal**: 300ms (transitions, modals)
- **Slow**: 500ms (complex animations)

### Easing
- **Ease-in-out**: Standard transitions
- **Ease-out**: Entrance animations
- **Ease-in**: Exit animations

### Principles
- Purposeful: Animation should have a clear purpose
- Subtle: Avoid distracting animations
- Performant: Use transform and opacity for 60fps

## Accessibility Standards

### WCAG 2.1 AA Compliance
- **Color Contrast**: 4.5:1 for normal text, 3:1 for large text
- **Focus Indicators**: Visible on all interactive elements
- **Keyboard Navigation**: All features accessible via keyboard
- **Screen Reader**: Semantic HTML, ARIA labels, alt text
- **Motion**: Respect `prefers-reduced-motion`

### Accessibility Checklist
- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] Color is not the only indicator
- [ ] Text can be resized to 200%
- [ ] No keyboard traps
- [ ] Focus order is logical

## Usage Examples

### Do's
- ✅ Use consistent spacing and alignment
- ✅ Follow color system guidelines
- ✅ Use design tokens (not hardcoded values)
- ✅ Test on multiple devices and screen sizes
- ✅ Validate accessibility with tools

### Don'ts
- ❌ Don't create new colors outside the system
- ❌ Don't use arbitrary spacing values
- ❌ Don't ignore accessibility requirements
- ❌ Don't use animations that cause motion sickness
- ❌ Don't mix different design styles

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | YYYY-MM-DD | Initial version | [Name] |

## Approval

- [ ] UX/UI Designer
- [ ] Product Owner
- [ ] Engineering Lead
- [ ] QA Engineer
