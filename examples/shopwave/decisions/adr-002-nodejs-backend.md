# ADR-002: Use Node.js for Backend API

## Status
Accepted

## Date
2026-01-10

## Context
We need to choose a backend technology for the ShopWave API.

## Decision
We will use Node.js with Express and TypeScript for the backend API.

## Rationale
- **Full-stack consistency**: JavaScript/TypeScript across frontend and backend
- **Performance**: Node.js provides good I/O performance
- **Ecosystem**: Rich npm ecosystem
- **Scalability**: Can handle high concurrency with async/await
- **Deployment**: Easy deployment with Docker

## Alternatives Considered
- **Python/Django**: Good for data-heavy apps, but team has more Node.js experience
- **Ruby/Rails**: Convention over configuration, but less familiar to team
- **Go**: Excellent performance, but less familiar

## Consequences
- **Positive**: Consistent language, good performance, easy hiring
- **Negative**: CPU-bound tasks less efficient, callback management complexity

## Approval
- [ ] Morgan Lee (Tech Lead)
- [ ] Jordan Smith (Solution Architect)
- [ ] Alex Rivera (Product Owner)
