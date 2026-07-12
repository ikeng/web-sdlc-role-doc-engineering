# ADR-003: Use PostgreSQL for Primary Database

## Status
Accepted

## Date
2026-01-10

## Context
We need to choose a primary database for the ShopWave application.

## Decision
We will use PostgreSQL as the primary database.

## Rationale
- **Relational data**: E-commerce requires structured data with relationships
- **ACID compliance**: Critical for transactions and order processing
- **JSON support**: Can store flexible product attributes
- **Mature**: Well-tested, large community, good tooling
- **AWS RDS**: Managed PostgreSQL available on AWS

## Alternatives Considered
- **MongoDB**: Flexible schema, but less suited for transactional data
- **MySQL**: Similar to PostgreSQL, but PostgreSQL has better JSON support
- **DynamoDB**: NoSQL, good for scale, but complex for relational data

## Consequences
- **Positive**: ACID compliance, mature ecosystem, good performance
- **Negative**: Requires careful schema design, vertical scaling limits

## Approval
- [ ] Jordan Smith (Solution Architect)
- [ ] Morgan Lee (Tech Lead)
- [ ] Alex Rivera (Product Owner)
