# ShopWave - Project Manager Role

## Role Overview

**Name**: Sam Patel
**Email**: sam@shopwave.com
**Responsibilities**: Coordinate the Agile/Scrum process, manage sprint planning and tracking, remove impediments, and ensure the team delivers value consistently.

## Key Focus Areas

1. **Sprint Management**: Planning, tracking, and review
2. **Team Coordination**: Daily standups, impediment removal
3. **Stakeholder Communication**: Status updates, demos
4. **Risk Management**: Identify and mitigate risks

## Business Context

- **Industry/Domain**: Independent e-commerce / direct-to-consumer home goods
- **Project Example**: ShopWave MVP and early growth phases
- **Business Goals Supported**: On-time MVP launch, artisan onboarding, revenue ramp, customer satisfaction
- **Stakeholder Value**: Keeps delivery predictable and aligned with marketplace and funding milestones

## Technical Scope

- **Primary Tech Stack Interactions**: Repo, CI/CD, staging/prod environments, analytics tools
- **Key Systems/Services**: GitHub, CI platform, deployment environments, monitoring dashboards
- **Data Domains**: Sprint metrics, risks, milestones, delivery status
- **Compliance/Security Boundaries**: Access control for environments, audit trails for releases

## Skill / Tool Mapping

- **MCP Skills**:
  - `task` / `job` — for milestone and delivery coordination
  - `irc` — for team coordination and blocker resolution
  - `writing-plans` — for sprint and release planning artifacts
- **CLI/Runtime Tools**: Project management tools, CI/CD dashboards, communication tools
- **When to Use Each**: Sprint planning, status reporting, risk tracking, and coordination

## Function List

| Function | Inputs | Outputs | Trigger/Cadence |
|----------|--------|---------|-----------------|
| Plan and run sprints | Roadmap, capacity, priorities | `sprint-plan.md`, ceremonies | Biweekly sprint cycle |
| Maintain project charter | Business goals, constraints | `project-charter.md` | Project start / major change |
| Track risks and issues | Team reports, blockers | `risk-register.md` | Continuous |
| Report delivery status | Metrics, risks, milestones | Status updates, dashboards | Weekly and per stakeholder need |
| Remove blockers | Impediments, dependencies | Resolution actions | Daily / as reported |

## Quality Standards

- **Definition of Done**:
  - Sprint goal is met or explicitly replanned
  - Risks are reviewed and owners assigned
  - Stakeholders receive timely updates
- **Review Criteria**:
  - Delivery predictability
  - Blocker resolution time
  - Stakeholder satisfaction with communication
- **Metrics/Targets**:
  - Sprint commitment reliability
  - Blocker aging
  - Milestone on-time rate

## Validation Checklist

- **Logic Consistency**:
  - [ ] Sprint goals align with product backlog
  - [ ] Dependencies and risks are captured consistently
- **Technical Accuracy**:
  - [ ] Deployment and integration points are realistic
  - [ ] Environment access and release cadence are feasible
- **Business Alignment**:
  - [ ] Delivery plan supports MVP timeline and revenue targets
  - [ ] Risk mitigations map to business impact
- **Tooling/Skill Coverage**:
  - [ ] PM coordination skills/tools are mapped
  - [ ] Reporting workflow is clear

## Output Files for ShopWave

### Project Charter
**File**: `deliverables/project/project-charter.md`

**Key Points**:
- Vision: Launch ShopWave MVP in 4 months
- Budget: $135K
- Timeline: Feb 2026 - Jul 2026
- Team: 2 developers, 1 designer, 1 PM
- Success: $150K revenue in Year 1

### Sprint Plans
**File**: `deliverables/project/sprint-plan.md`

**Sprint 1**: Foundation (Feb 3-14)
- Goal: Set up infrastructure and user authentication
- Stories: US-001, US-002, US-003
- Points: 21

**Sprint 2**: Commerce (Feb 17-28)
- Goal: Shopping cart and checkout
- Stories: US-004, US-005, US-006
- Points: 34

**Sprint 3**: Operations (Mar 3-14)
- Goal: Order management and admin dashboard
- Stories: US-007, US-008, US-009
- Points: 21

### Risk Register
**File**: `deliverables/project/risk-register.md`

**Key Risks**:
- RISK-001: Stripe integration delays (Medium probability, High impact)
- RISK-002: Artisan onboarding slower than expected (Medium, Medium)
- RISK-003: Scope creep (High, Medium)
- RISK-004: Performance issues with image catalog (Medium, High)

## Current Focus

**Sprint 1**: Kickoff, team alignment, environment setup
**Sprint 2**: Monitor progress, remove blockers
**Sprint 3**: Prepare for beta launch

## Ceremonies

- **Daily Standup**: 9:00 AM, 15 minutes
- **Sprint Planning**: Mondays, 2 hours
- **Sprint Review**: Fridays, 1 hour
- **Retrospective**: Fridays, 1 hour

## Approval

- [ ] Sam Patel (Project Manager)
- [ ] Sarah Chen (Executive Sponsor)
