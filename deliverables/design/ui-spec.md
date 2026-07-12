# UI Specification

## Metadata
- **Version**: 1.0
- **Author**: UX/UI Designer
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Screen/Component**: [Name]

## Visual Design

### Color Palette

#### Primary Colors
- **Primary Blue**: #007AFF
  - Usage: Primary buttons, links, active states
  - Hover: #0056CC
  - Active: #004BB5

- **Secondary Purple**: #5856D6
  - Usage: Secondary buttons, accents
  - Hover: #4342B8
  - Active: #3A39A8

#### Semantic Colors
- **Success**: #34C759
  - Usage: Success messages, positive actions
- **Warning**: #FF9500
  - Usage: Warning messages, caution states
- **Error**: #FF3B30
  - Usage: Error messages, destructive actions
- **Info**: #5AC8FA
  - Usage: Informational messages

#### Neutral Colors
- **Text Primary**: #1D1D1F
  - Usage: Headlines, body text
- **Text Secondary**: #6E6E73
  - Usage: Subtitles, helper text
- **Background**: #FFFFFF
  - Usage: Page background
- **Surface**: #F5F5F7
  - Usage: Card backgrounds, sections
- **Border**: #D2D2D7
  - Usage: Input borders, dividers

### Typography

#### Font Family
- **Headings**: Inter (Bold, SemiBold)
- **Body**: Inter (Regular, Medium)
- **Monospace**: SF Mono (code, technical content)

#### Type Scale
| Level | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| H1 | 48px | 700 | 1.2 | Page titles |
| H2 | 36px | 600 | 1.3 | Section titles |
| H3 | 24px | 600 | 1.4 | Component titles |
| H4 | 20px | 600 | 1.4 | Card titles |
| Body | 16px | 400 | 1.5 | Body text |
| Small | 14px | 400 | 1.5 | Helper text |
| Caption | 12px | 400 | 1.4 | Labels, captions |

#### Font Loading
- Load from Google Fonts or self-hosted
- Font-display: swap
- Preload critical fonts

### Spacing System

**Base Unit**: 8px

| Token | Value | Usage |
|-------|-------|-------|
| xs | 4px | Tight spacing, icon padding |
| sm | 8px | Component padding, gaps |
| md | 16px | Section padding |
| lg | 24px | Large gaps, card padding |
| xl | 32px | Section spacing |
| 2xl | 48px | Large section spacing |
| 3xl | 64px | Hero section spacing |

### Shadows

| Level | Shadow | Usage |
|-------|--------|-------|
| sm | 0 1px 3px rgba(0,0,0,0.1) | Small elements, inputs |
| md | 0 4px 6px rgba(0,0,0,0.1) | Cards, dropdowns |
| lg | 0 10px 15px rgba(0,0,0,0.1) | Modals, popovers |
| xl | 0 20px 25px rgba(0,0,0,0.15) | Large modals |

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| sm | 4px | Small buttons, inputs |
| md | 8px | Cards, buttons |
| lg | 12px | Large cards |
| xl | 16px | Modals, panels |
| full | 9999px | Pills, avatars |

## Component Specifications

### Button

#### Variants
- **Primary**: Background #007AFF, text white
- **Secondary**: Background transparent, border #007AFF, text #007AFF
- **Tertiary**: Background transparent, text #007AFF
- **Destructive**: Background #FF3B30, text white

#### Sizes
- **Small**: Height 32px, padding 8px 16px, font-size 14px
- **Medium**: Height 40px, padding 10px 20px, font-size 16px
- **Large**: Height 48px, padding 12px 24px, font-size 18px

#### States
- **Default**: As specified above
- **Hover**: Darken background by 10%
- **Active**: Darken background by 20%
- **Disabled**: Opacity 0.5, cursor not-allowed
- **Loading**: Show spinner, disable interaction

#### Implementation
```css
.btn-primary {
  background-color: #007AFF;
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: background-color 0.2s;
}

.btn-primary:hover {
  background-color: #0056CC;
}

.btn-primary:active {
  background-color: #004BB5;
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

### Input

#### Variants
- **Default**: Border #D2D2D7, background white
- **Error**: Border #FF3B30, background #FFF5F5
- **Success**: Border #34C759, background #F5FFF5
- **Disabled**: Background #F5F5F7, border #E5E5EA

#### States
- **Default**: Border #D2D2D7
- **Focus**: Border #007AFF, ring 2px #007AFF20
- **Error**: Border #FF3B30, error message below
- **Disabled**: Background #F5F5F7, opacity 0.6

#### Implementation
```css
.input {
  width: 100%;
  height: 40px;
  padding: 8px 12px;
  border: 1px solid #D2D2D7;
  border-radius: 8px;
  font-size: 16px;
  background: white;
  transition: border-color 0.2s;
}

.input:focus {
  outline: none;
  border-color: #007AFF;
  box-shadow: 0 0 0 2px #007AFF20;
}

.input:disabled {
  background: #F5F5F7;
  opacity: 0.6;
  cursor: not-allowed;
}
```

### Card

#### Specification
- **Background**: White
- **Border**: 1px solid #E5E5EA
- **Border Radius**: 12px
- **Padding**: 24px
- **Shadow**: 0 4px 6px rgba(0,0,0,0.1)

#### Implementation
```css
.card {
  background: white;
  border: 1px solid #E5E5EA;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
```

## Responsive Behavior

### Desktop (> 1200px)
- Full layout with sidebars
- 3-column grids
- Full navigation

### Tablet (768px - 1199px)
- Collapsed sidebars
- 2-column grids
- Simplified navigation

### Mobile (< 768px)
- Single column layout
- Bottom navigation
- Hamburger menu

## Accessibility Requirements

### Color Contrast
- All text meets WCAG AA (4.5:1 ratio)
- Interactive elements meet WCAG AAA (7:1 ratio)

### Focus States
- All interactive elements have visible focus indicator
- Focus indicator: 2px solid #007AFF, 2px offset

### Screen Reader
- All images have alt text
- Form inputs have labels
- Interactive elements have ARIA labels
- Error messages are announced

### Keyboard Navigation
- Tab order follows visual layout
- All interactive elements are keyboard accessible
- Skip links provided

## Animation & Transitions

### Timing
- **Fast**: 150ms (hover effects)
- **Normal**: 300ms (transitions, modals)
- **Slow**: 500ms (complex animations)

### Easing
- **Ease-in-out**: Standard transitions
- **Ease-out**: Entrance animations
- **Ease-in**: Exit animations

### Examples
```css
.button {
  transition: all 0.3s ease-in-out;
}

.card {
  transition: transform 0.2s ease-out, box-shadow 0.2s ease-out;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 15px rgba(0,0,0,0.1);
}
```

## Design Tokens

```json
{
  "colors": {
    "primary": "#007AFF",
    "secondary": "#5856D6",
    "success": "#34C759",
    "warning": "#FF9500",
    "error": "#FF3B30",
    "info": "#5AC8FA",
    "text-primary": "#1D1D1F",
    "text-secondary": "#6E6E73",
    "background": "#FFFFFF",
    "surface": "#F5F5F7",
    "border": "#D2D2D7"
  },
  "typography": {
    "font-family": "Inter, sans-serif",
    "h1": { "size": "48px", "weight": "700", "line-height": "1.2" },
    "h2": { "size": "36px", "weight": "600", "line-height": "1.3" },
    "body": { "size": "16px", "weight": "400", "line-height": "1.5" }
  },
  "spacing": {
    "xs": "4px",
    "sm": "8px",
    "md": "16px",
    "lg": "24px",
    "xl": "32px"
  },
  "border-radius": {
    "sm": "4px",
    "md": "8px",
    "lg": "12px"
  }
}
```

## Approval

- [ ] UX/UI Designer
- [ ] Product Owner
- [ ] Engineering Lead
