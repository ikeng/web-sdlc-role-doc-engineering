# Solution Architect

## Role Overview

The Solution Architect designs the overall system architecture, selects technology stack, and ensures the solution meets functional and non-functional requirements.

## Responsibilities

- Design system architecture and components
- Select and justify technology stack
- Design API contracts and data models
- Ensure scalability, performance, and reliability
- Define integration patterns and third-party services
- Document architectural decisions (ADRs)
- Review code for architectural compliance
- Mentor developers on architectural patterns

## Output Files

| File | Phase | Description |
|------|-------|-------------|
| `architecture-doc.md` | Architecture | System architecture and design decisions |
| `tech-stack.md` | Architecture | Technology stack selection and rationale |
| `api-design.md` | Architecture | API contracts and specifications |

## File Dimensions

### architecture-doc.md

**Purpose**: Document the overall system architecture and design decisions.

**Required Sections**:
- Document metadata (version, authors, date)
- System overview and context
- Architecture style (monolith, microservices, serverless, etc.)
- Component diagram
- Data flow diagram
- Technology stack overview
- Deployment architecture
- Security architecture
- Scalability and performance considerations
- Architectural Decision Records (ADRs)
- Trade-offs and alternatives considered

**Quality Gates**:
- [ ] Architecture meets all requirements
- [ ] Scalability and performance are addressed
- [ ] Security considerations are documented
- [ ] ADRs are documented for major decisions
- [ ] Stakeholders have reviewed and approved

### tech-stack.md

**Purpose**: Define the technology stack with rationale and constraints.

**Required Sections**:
- Frontend framework and libraries
- Backend framework and runtime
- Database(s) and ORM
- Caching strategy
- Authentication and authorization
- API protocols (REST, GraphQL, WebSocket)
- Deployment platform and infrastructure
- Monitoring and logging
- CI/CD tools
- Rationale for each choice
- Alternatives considered
- Constraints and limitations

**Quality Gates**:
- [ ] Stack is justified with rationale
- [ ] All requirements can be met
- [ ] Team has expertise or training plan
- [ ] Cost and licensing are considered
- [ ] Scalability is addressed

### api-design.md

**Purpose**: Define API contracts, endpoints, and data models.

**Required Sections**:
- API overview and principles
- Authentication and authorization
- Endpoint specifications (path, method, description)
- Request/response schemas
- Error handling and status codes
- Rate limiting and throttling
- Versioning strategy
- Data models and relationships
- Example requests/responses
- API documentation standards

**Quality Gates**:
- [ ] All endpoints are documented
- [ ] Request/response schemas are clear
- [ ] Error handling is consistent
- [ ] API is versioned
- [ ] Examples are provided
- [ ] Frontend and backend teams have reviewed

## Interaction Patterns

**Inputs From**:
- Business Analyst (functional requirements)
- Product Owner (feature priorities)
- UX Designer (technical constraints)

**Outputs To**:
- Tech Lead (implementation guidance)
- Full-stack Developer (implementation specs)
- DevOps Engineer (deployment requirements)
- Security Engineer (security requirements)

**Review Cycle**:
- Sprint: Architecture review meetings
- Release: Architecture compliance audit
- Quarterly: Architecture evolution planning

## Tools & Templates

- Diagramming tools (Mermaid, Draw.io, Lucidchart)
- Architecture decision record (ADR) templates
- API specification tools (OpenAPI, Swagger)
- Architecture evaluation frameworks
