# Wireframes

## Metadata
- **Version**: 1.0
- **Author**: UX/UI Designer
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Screen/Flow**: [Name]

## Screen Overview

**Screen Name**: [e.g., Homepage, Login Page, Dashboard]
**User Flow**: [e.g., Entry point → Browse → Product Detail → Add to Cart]
**Device**: Desktop / Tablet / Mobile
**Priority**: High/Medium/Low

## Layout Grid

### Desktop (1440px)
- **Max Width**: 1200px
- **Columns**: 12 columns, 80px each, 24px gutters
- **Margins**: 120px left/right
- **Header Height**: 72px
- **Footer Height**: 320px

### Tablet (768px)
- **Max Width**: 720px
- **Columns**: 8 columns, 76px each, 20px gutters
- **Margins**: 24px left/right
- **Header Height**: 64px

### Mobile (375px)
- **Max Width**: 375px
- **Columns**: 4 columns, 72px each, 16px gutters
- **Margins**: 16px left/right
- **Header Height**: 56px

## Wireframe: [Screen Name]

### Desktop Layout

```
┌─────────────────────────────────────────────────────────────┐
│ HEADER (72px)                                              │
│ [Logo]        [Nav] [Nav] [Nav]          [Search] [Cart] [👤] │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                                                             │
│                    MAIN CONTENT AREA                       │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ FOOTER (320px)                                             │
│ [Links] [Links] [Links]                                   │
│ [Social] [Social]                                          │
│ © 2026 Company                                             │
└─────────────────────────────────────────────────────────────┘
```

### Mobile Layout

```
┌───────────────────┐
│ HEADER (56px)     │
│ [☰]  [Logo]   [🔍] │
├───────────────────┤
│                   │
│  MAIN CONTENT     │
│                   │
│                   │
│                   │
│                   │
├───────────────────┤
│ FOOTER            │
│ [Links]           │
│ © 2026            │
└───────────────────┘
```

## Component Placement

### Header
- **Logo** (top-left, 120px × 40px)
  - Links to homepage
  - Alt text: "Company Name"

- **Navigation** (center, horizontal)
  - Home | Products | About | Contact
  - Active state: Underline, bold
  - Hover state: Color change

- **Search** (right, icon + input)
  - Placeholder: "Search..."
  - Expand on focus

- **Cart** (right, icon with badge)
  - Badge shows item count
  - Opens cart sidebar on click

- **User Menu** (right, avatar icon)
  - Dropdown on click
  - Options: Profile, Settings, Logout

### Main Content Area
- **Hero Section** (full width, 500px height)
  - Headline: [Text]
  - Subheadline: [Text]
  - CTA Button: [Text]
  - Background: Image or gradient

- **Product Grid** (below hero)
  - 3 columns (desktop), 2 columns (tablet), 1 column (mobile)
  - Product cards: Image, name, price, rating, "Add to Cart" button
  - Gap: 24px (desktop), 20px (tablet), 16px (mobile)

### Footer
- **Links Section** (3 columns)
  - Column 1: Company info, logo
  - Column 2: Quick links
  - Column 3: Contact info

- **Social Links** (centered)
  - Facebook, Twitter, Instagram, LinkedIn

- **Copyright** (bottom center)

## Responsive Breakpoints

### Desktop → Tablet (< 1200px)
- Reduce margins to 24px
- Navigation collapses to hamburger menu
- Product grid: 2 columns
- Footer columns stack vertically

### Tablet → Mobile (< 768px)
- Full-width layout
- Single column layout
- Hamburger menu for navigation
- Footer simplified

## Interaction Notes

### Header
- **Scroll**: Header becomes sticky with shadow
- **Mobile Menu**: Hamburger opens full-screen overlay
- **Search**: Expands on focus, submits on Enter
- **Cart**: Opens slide-out panel from right

### Hero Section
- **CTA Button**: Hover effect (scale, shadow)
- **Background**: Parallax effect on scroll

### Product Cards
- **Hover**: Lift effect with shadow
- **Add to Cart**: Button animation, cart badge update
- **Image**: Lazy load, fade-in effect

## Accessibility Considerations

### Keyboard Navigation
- All interactive elements are focusable
- Tab order follows visual layout
- Skip to main content link

### Screen Reader
- Semantic HTML (header, nav, main, footer)
- ARIA labels for icon buttons
- Alt text for all images

### Color Contrast
- Text/background ratio ≥ 4.5:1 (WCAG AA)
- Focus indicators visible
- Color not used as only indicator

## Design Notes

- **Typography**: Inter (headings), system fonts (body)
- **Colors**:
  - Primary: #007AFF
  - Secondary: #5856D6
  - Text: #1D1D1F
  - Background: #FFFFFF
- **Spacing**: 8px base unit (4, 8, 12, 16, 24, 32, 48, 64)

## Next Steps

- [ ] Review with stakeholders
- [ ] Create high-fidelity mockups
- [ ] Create interactive prototype
- [ ] Conduct usability testing

## Approval

- [ ] UX/UI Designer
- [ ] Product Owner
- [ ] Engineering Lead
