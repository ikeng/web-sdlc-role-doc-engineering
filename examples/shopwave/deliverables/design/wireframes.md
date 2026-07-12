# ShopWave - Wireframes

## Metadata
- **Version**: 1.0
- **Author**: Taylor Kim (UX Designer)
- **Date**: 2026-01-15
- **Project**: ShopWave
- **Screen/Flow**: Homepage

## Screen Overview

**Screen Name**: Homepage
**User Flow**: Entry point → Featured products → Browse → Product detail → Add to cart
**Device**: Desktop / Tablet / Mobile
**Priority**: High

## Layout Grid

### Desktop (1440px)
- **Max Width**: 1200px
- **Columns**: 12 columns
- **Margins**: 120px left/right
- **Header Height**: 72px

### Tablet (768px)
- **Max Width**: 720px
- **Margins**: 24px left/right
- **Header Height**: 64px

### Mobile (375px)
- **Max Width**: 375px
- **Margins**: 16px left/right
- **Header Height**: 56px

## Wireframe: Homepage

### Desktop Layout

```
┌─────────────────────────────────────────────────────────────┐
│ HEADER (72px)                                              │
│ [ShopWave Logo]    [Shop] [Artisans] [About]    [🔍] [🛒] [👤] │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  HERO SECTION (500px)                                      │
│  "Handcrafted Home Goods"                                   │
│  Subheadline: Supporting independent artisans               │
│  [Shop Now]                                                │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  FEATURED ARTISANS (300px)                                 │
│  [Artisan 1] [Artisan 2] [Artisan 3]                      │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PRODUCT GRID (auto)                                       │
│  [Product] [Product] [Product] [Product]                   │
│  [Product] [Product] [Product] [Product]                   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CATEGORIES (200px)                                        │
│  [Ceramics] [Textiles] [Woodwork] [Lighting]               │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ FOOTER                                                      │
└─────────────────────────────────────────────────────────────┘
```

### Mobile Layout

```
┌───────────────────┐
│ HEADER (56px)     │
│ [☰] [Logo] [🔍] [🛒] │
├───────────────────┤
│                   │
│  HERO SECTION     │
│  "Handcrafted     │
│   Home Goods"     │
│  [Shop Now]       │
│                   │
├───────────────────┤
│                   │
│  PRODUCT GRID     │
│  [Product]        │
│  [Product]        │
│  [Product]        │
│                   │
├───────────────────┤
│  CATEGORIES       │
│  [Ceramics]       │
│  [Textiles]       │
├───────────────────┤
│ FOOTER            │
└───────────────────┘
```

## Component Placement

### Header
- **Logo**: Top-left, links to homepage
- **Navigation**: Center, horizontal (Shop, Artisans, About)
- **Search**: Right, icon + expandable input
- **Cart**: Right, icon with badge
- **User Menu**: Right, avatar icon

### Hero Section
- **Headline**: "Handcrafted Home Goods"
- **Subheadline**: "Supporting independent artisans"
- **CTA Button**: "Shop Now" → /products

### Featured Artisans
- **Section Title**: "Meet Our Artisans"
- **Artisan Cards**: Photo, name, specialty, product count

### Product Grid
- **Section Title**: "New Arrivals"
- **Product Cards**: Image, name, price, artisan, "Add to Cart" button
- **3 columns desktop, 2 tablet, 1 mobile**

### Categories
- **Section Title**: "Shop by Category"
- **Category Cards**: Image, category name, product count
- **4 columns desktop, 2 tablet, 2 mobile**

### Footer
- **Links**: About, Contact, Shipping, Returns
- **Social**: Instagram, Pinterest, Facebook
- **Newsletter**: Email signup
- **Copyright**: © 2026 ShopWave

## Responsive Breakpoints

### Desktop → Tablet (< 1200px)
- Reduce margins to 24px
- Navigation collapses to hamburger menu
- Product grid: 2 columns

### Tablet → Mobile (< 768px)
- Full-width layout
- Single column layout
- Hamburger menu for navigation

## Interaction Notes

### Header
- **Scroll**: Header becomes sticky with shadow
- **Mobile Menu**: Hamburger opens full-screen overlay
- **Search**: Expands on focus, submits on Enter
- **Cart**: Opens slide-out panel from right

### Hero Section
- **CTA Button**: Hover effect (scale, shadow)
- **Background**: Image with overlay

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

## Design Notes

- **Typography**: Inter (headings), system fonts (body)
- **Colors**:
  - Primary: #2D5A3D (forest green)
  - Secondary: #F4A261 (warm orange)
  - Text: #1D1D1F
  - Background: #FFFFFF
- **Spacing**: 8px base unit

## Next Steps

- [ ] Review with stakeholders
- [ ] Create high-fidelity mockups
- [ ] Create interactive prototype
- [ ] Conduct usability testing

## Approval

- [ ] Taylor Kim (UX Designer)
- [ ] Alex Rivera (Product Owner)
- [ ] Jordan Smith (Tech Lead)
