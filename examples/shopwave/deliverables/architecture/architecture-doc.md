# ShopWave - Architecture Document

## Metadata
- **Version**: 1.0
- **Authors**: Jordan Smith (Solution Architect)
- **Date**: 2026-01-15
- **Project**: ShopWave
- **Status**: Approved
- **Reviewers**: Morgan Lee (Tech Lead), Riley Park (Security Engineer), Alex Kim (DevOps)

## System Overview

### Purpose
ShopWave is an independent e-commerce platform connecting artisans with conscious consumers. It enables browsing, purchasing, and order tracking for handcrafted home goods.

### Scope
- **In Scope**: Product catalog, shopping cart, checkout, order management, admin dashboard
- **Out of Scope**: Multi-vendor marketplace, subscriptions, international shipping

### Key Stakeholders
- Sarah Chen (CEO): Business success
- Alex Rivera (PO): Product requirements
- Jordan Smith (Architect): Technical viability

## Architecture Style

### Chosen Architecture: Monolith with Modular Design

**Rationale**: Simpler to deploy and maintain for MVP. Can evolve to microservices later as team and traffic grow.

**Trade-offs**:
- Pros: Simple deployment, easy development, lower operational cost
- Cons: Less scalable long-term, single point of failure

**Alternatives Considered**:
- Microservices: Too complex for MVP, team size
- Serverless: Higher cold start latency, vendor lock-in

## System Architecture

### High-Level Architecture

```
┌─────────────┐
│   Users     │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────────┐
│         CloudFront CDN                  │
└────────────────┬────────────────────────┘
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
┌──────────────┐   ┌──────────────┐
│  Web Server  │   │  Web Server  │
│   (Node 1)   │   │   (Node 2)   │
└──────┬───────┘   └──────┬───────┘
       │                   │
       └────────┬──────────┘
                ▼
       ┌─────────────────────┐
       │   API Service       │
       │  (Express.js)       │
       └─────────┬───────────┘
                 │
      ┌──────────┼──────────┐
      ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ Primary  │ │   Cache  │ │   Queue  │
│ Database │ │  (Redis) │ │  (SQS)   │
│(Postgres)│ │          │ │          │
└──────────┘ └──────────┘ └──────────┘
```

### Component Diagram

| Component | Responsibility | Technology | Scale |
|-----------|---------------|------------|-------|
| Load Balancer | Distribute traffic | AWS ALB | Horizontal |
| Web Servers | Serve React app | Nginx | 2+ instances |
| API Service | Business logic | Express.js | Horizontal |
| Database | Persistent storage | PostgreSQL RDS | Primary + Read replicas |
| Cache | Session & data cache | Redis ElastiCache | Cluster |
| Storage | Product images | AWS S3 | Global |
| CDN | Static assets | CloudFront | Global |

## Data Architecture

### Data Models

**User**
- id: UUID
- email: string (unique)
- password_hash: string
- name: string
- role: enum (customer, artisan, admin)
- created_at: timestamp

**Product**
- id: UUID
- name: string
- description: text
- price: decimal
- inventory_count: integer
- artisan_id: UUID
- category_id: UUID
- images: json[]
- created_at: timestamp

**Order**
- id: UUID
- user_id: UUID
- status: enum (pending, processing, shipped, delivered, cancelled)
- total_amount: decimal
- shipping_address: json
- items: json[]
- created_at: timestamp

## Security Architecture

### Authentication & Authorization
- JWT tokens (access + refresh)
- Role-based access control (customer, artisan, admin)
- bcrypt password hashing (cost factor 12)

### Data Protection
- AES-256 encryption at rest
- TLS 1.3 encryption in transit
- Secrets in AWS Secrets Manager

### Network Security
- VPC with private subnets
- Security groups
- WAF for SQL injection, XSS protection
- DDoS protection

## Deployment Architecture

### Environments
- **Development**: Docker Compose
- **Staging**: AWS (single region)
- **Production**: AWS (multi-AZ, auto-scaling)

### Infrastructure as Code
- Terraform for AWS resources
- GitHub Actions for CI/CD

## Scalability & Performance

### Horizontal Scaling
- ECS for API servers
- Read replicas for database
- Redis cluster for cache

### Performance Targets
- Page load < 2s
- API response < 500ms
- Database query < 200ms
- 1,000 concurrent users

## Technology Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| Frontend | React + TypeScript | Component-based, type-safe |
| Backend | Node.js + Express | JavaScript unification, fast dev |
| Database | PostgreSQL | ACID, JSON support |
| Cache | Redis | Fast, in-memory |
| Auth | JWT | Stateless, scalable |
| Payments | Stripe | Best DX, comprehensive |
| Deployment | AWS ECS | Managed, scalable |
| CDN | CloudFront | Global distribution |

## Architectural Decision Records (ADRs)

### ADR-001: Use Monolith with Modular Design

**Status**: Accepted
**Date**: 2026-01-15

**Context**: Need to choose architecture for MVP.

**Decision**: Use monolith with modular design.

**Rationale**:
- Simpler to deploy and maintain
- Faster development for small team
- Can evolve to microservices later

**Consequences**:
- Less scalable long-term
- Single point of failure
- Will need refactoring as we grow

## Approval

- [ ] Jordan Smith (Solution Architect)
- [ ] Morgan Lee (Tech Lead)
- [ ] Riley Park (Security Engineer)
- [ ] Alex Kim (DevOps)
