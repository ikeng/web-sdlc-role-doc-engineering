# UX/UI Designer

## Role Overview

The UX/UI Designer creates intuitive, accessible, and visually appealing user experiences through research, wireframing, and high-fidelity designs.

## Responsibilities

- Conduct user research and create personas
- Design information architecture and user flows
- Create wireframes and prototypes
- Design visual UI components and design system
- Ensure accessibility (WCAG 2.1 compliance)
- Collaborate with developers on implementation
- Conduct usability testing
- Maintain design consistency across the product

## Output Files

| File | Phase | Description |
|------|-------|-------------|
| `wireframes.md` | Design | Low-fidelity wireframes and layouts |
| `ui-spec.md` | Design | High-fidelity UI specifications |
| `design-system.md` | Design | Design system with components and tokens |

## File Dimensions

### wireframes.md

**Purpose**: Define the structure and layout of screens before visual design.

**Required Sections**:
- Screen/flow name and purpose
- User flow description
- Wireframe diagrams (ASCII or image references)
- Layout grid specifications
- Component placement
- Interaction notes
- Responsive breakpoints
- Accessibility considerations

**Quality Gates**:
- [ ] All user flows are covered
- [ ] Layouts are responsive
- [ ] Navigation is intuitive
- [ ] Stakeholders have reviewed

### ui-spec.md

**Purpose**: High-fidelity design specifications for implementation.

**Required Sections**:
- Screen/component name
- Visual design mockups (image references)
- Color palette and typography
- Spacing and layout specifications
- Component states (default, hover, active, disabled)
- Animation and transition specifications
- Responsive behavior
- Accessibility requirements (contrast, focus states)
- Design tokens (colors, fonts, spacing)

**Quality Gates**:
- [ ] Designs match wireframes
- [ ] Accessibility standards met (WCAG 2.1 AA)
- [ ] Responsive designs for all breakpoints
- [ ] Design system consistency
- [ ] Developer handoff complete

### design-system.md

**Purpose**: Central repository of design components and standards.

**Required Sections**:
- Design principles and philosophy
- Color system (primary, secondary, semantic, neutral)
- Typography scale and font families
- Spacing system (base unit, scale)
- Component library (buttons, forms, navigation, etc.)
- Icon library and usage guidelines
- Illustration and imagery style
- Animation and motion guidelines
- Accessibility standards
- Usage examples and do's/don'ts

**Quality Gates**:
- [ ] All components are documented
- [ ] Components are accessible
- [ ] Design tokens are defined
- [ ] Usage guidelines are clear
- [ ] Developers can implement from specs

## Interaction Patterns

**Inputs From**:
- Product Owner (feature requirements)
- Business Analyst (user requirements)
- Users (feedback, pain points)

**Outputs To**:
- Full-stack Developer (design specs)
- QA Engineer (accessibility requirements)
- Solution Architect (technical constraints)

**Review Cycle**:
- Weekly: Design review with team
- Sprint: Design handoff to development
- Release: Design consistency audit

## Tools & Templates

- Design tools (Figma, Sketch, Adobe XD)
- Prototyping tools (Figma, Principle)
- Design system tools (Storybook)
- Usability testing tools
