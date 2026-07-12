# ShopWave - UI Specification

## Metadata
- **Version**: 1.0
- **Author**: Taylor Kim (UX Designer)
- **Date**: 2026-01-15
- **Project**: ShopWave
- **Screen/Component**: Global Design System

## Visual Design

### Color Palette

#### Primary Colors
- **Primary Green**: #2D5A3D
  - Usage: Primary buttons, links, active states
  - Hover: #1E3D2B
  - Active: #142D1F

- **Secondary Orange**: #F4A261
  - Usage: Accent buttons, highlights
  - Hover: #E08E4A
  - Active: #D17F3B

#### Semantic Colors
- **Success**: #34C759
- **Warning**: #FF9500
- **Error**: #FF3B30
- **Info**: #5AC8FA

#### Neutral Colors
- **Text Primary**: #1D1D1F
- **Text Secondary**: #6E6E73
- **Background**: #FFFFFF
- **Surface**: #F5F5F7
- **Border**: #D2D2D7

### Typography

#### Font Family
- **Headings**: Inter (Bold, SemiBold)
- **Body**: Inter (Regular, Medium)
- **Accent**: Playfair Display (product names, hero)

#### Type Scale
| Level | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| H1 | 48px | 700 | 1.2 | Page titles |
| H2 | 36px | 600 | 1.3 | Section titles |
| H3 | 24px | 600 | 1.4 | Component titles |
| Body | 16px | 400 | 1.5 | Body text |
| Small | 14px | 400 | 1.5 | Helper text |

### Spacing System

**Base Unit**: 8px

| Token | Value | Usage |
|-------|-------|-------|
| xs | 4px | Tight spacing |
| sm | 8px | Component padding |
| md | 16px | Section padding |
| lg | 24px | Card padding |
| xl | 32px | Section spacing |

### Shadows

| Level | Shadow | Usage |
|-------|--------|-------|
| sm | 0 1px 3px rgba(0,0,0,0.1) | Small elements |
| md | 0 4px 6px rgba(0,0,0,0.1) | Cards |
| lg | 0 10px 15px rgba(0,0,0,0.1) | Modals |

## Component Specifications

### Button

**Variants**: Primary, Secondary, Tertiary, Destructive

**Primary Button**:
- Background: #2D5A3D
- Text: White
- Padding: 12px 24px
- Border Radius: 8px
- Font-size: 16px
- Font-weight: 600

**Hover**: Darken background by 10%
**Active**: Darken background by 20%
**Disabled**: Opacity 0.5

### Product Card

**Specification**:
- Background: White
- Border: 1px solid #E5E5EA
- Border Radius: 12px
- Padding: 16px
- Shadow: 0 4px 6px rgba(0,0,0,0.1)

**Image**: 4:3 aspect ratio, object-fit cover
**Content**: Product name, artisan name, price, "Add to Cart" button

**Hover**: Lift effect (translateY(-4px)), shadow increase

### Input

**Variants**: Default, Error, Success, Disabled

**Default Input**:
- Height: 40px
- Border: 1px solid #D2D2D7
- Border Radius: 8px
- Padding: 8px 12px
- Font-size: 16px

**Focus**: Border #2D5A3D, ring 2px #2D5A3D20

## Responsive Behavior

### Desktop (> 1200px)
- Full layout with 12-column grid
- Horizontal navigation

### Tablet (768px - 1199px)
- 8-column grid
- Simplified navigation

### Mobile (< 768px)
- Single column layout
- Bottom navigation or hamburger menu

## Accessibility Requirements

### Color Contrast
- All text meets WCAG AA (4.5:1 ratio)

### Focus States
- 2px solid #2D5A3D, 2px offset

### Screen Reader
- All images have alt text
- Form inputs have labels
- Interactive elements have ARIA labels

## Animation & Transitions

### Timing
- **Fast**: 150ms (hover effects)
- **Normal**: 300ms (transitions, modals)

### Easing
- **Ease-in-out**: Standard transitions
- **Ease-out**: Entrance animations

## Design Tokens

```json
{
  "colors": {
    "primary": "#2D5A3D",
    "secondary": "#F4A261",
    "success": "#34C759",
    "warning": "#FF9500",
    "error": "#FF3B30",
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
  }
}
```

## Approval

- [ ] Taylor Kim (UX Designer)
- [ ] Alex Rivera (Product Owner)
- [ ] Jordan Smith (Tech Lead)
