# API Design Template

## Instructions
Copy this template for each project's API design document.
Replace all `[placeholder]` text with actual values.

## Metadata
- **Version**: 1.0
- **Author**: Solution Architect
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Status**: Draft / In Review / Approved

## API Overview

### API Type
RESTful API with JSON payloads

### Base URL
- **Production**: `https://api.example.com/v1`
- **Staging**: `https://api-staging.example.com/v1`
- **Development**: `http://localhost:3000/api/v1`

### Authentication
All endpoints (except public ones) require authentication via JWT Bearer token:
```
Authorization: Bearer <access_token>
```

### Rate Limiting
- **Authenticated**: 100 requests/minute
- **Unauthenticated**: 20 requests/minute
- **Rate Limit Headers**:
  - `X-RateLimit-Limit`: Request limit
  - `X-RateLimit-Remaining`: Remaining requests
  - `X-RateLimit-Reset`: Time when limit resets (Unix timestamp)

### Versioning
- URL path versioning: `/v1/`, `/v2/`
- Breaking changes require new version
- Non-breaking changes can be deployed to current version

### Error Responses
All errors follow this format:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable error message",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

**HTTP Status Codes**:
- `200 OK`: Successful GET, PUT, PATCH
- `201 Created`: Successful POST
- `204 No Content`: Successful DELETE
- `400 Bad Request`: Invalid request body/parameters
- `401 Unauthorized`: Missing or invalid authentication
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `409 Conflict`: Resource conflict (e.g., duplicate email)
- `422 Unprocessable Entity`: Validation error
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error
- `503 Service Unavailable`: Service temporarily unavailable

## Endpoints

### [Resource Name]

#### GET /[resource]
[List all items with pagination]

**Authentication**: Optional/Required

**Query Parameters**:
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20, max: 100)
- `sort`: Sort field
- `order`: Sort order (asc, desc)

**Response 200**:
```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "totalPages": 5
  }
}
```

**Error Responses**:
- `400`: Invalid query parameters
- `401`: Authentication required

---

#### GET /[resource]/:id
[Get single item by ID]

**Authentication**: Optional/Required

**Response 200**:
```json
{
  "data": {
    "id": "uuid",
    "name": "Item Name",
    "createdAt": "2026-01-01T00:00:00Z"
  }
}
```

**Error Responses**:
- `404`: Resource not found
- `401`: Authentication required

---

#### POST /[resource]
[Create new item]

**Authentication**: Required

**Request**:
```json
{
  "field1": "value",
  "field2": "value"
}
```

**Response 201**:
```json
{
  "data": {
    "id": "uuid",
    "field1": "value",
    "field2": "value",
    "createdAt": "2026-01-01T00:00:00Z"
  }
}
```

**Error Responses**:
- `400`: Invalid request body
- `401`: Authentication required
- `409`: Resource already exists

---

#### PATCH /[resource]/:id
[Update item]

**Authentication**: Required

**Request**:
```json
{
  "field1": "new value"
}
```

**Response 200**: Updated item object

**Error Responses**:
- `400`: Invalid request body
- `401`: Authentication required
- `403`: Insufficient permissions
- `404`: Resource not found

---

#### DELETE /[resource]/:id
[Delete item]

**Authentication**: Required

**Response 204**: No content

**Error Responses**:
- `401`: Authentication required
- `403`: Insufficient permissions
- `404`: Resource not found

## Data Models

### [Model Name]
```typescript
{
  id: string; // UUID
  field1: string;
  field2: number;
  field3: Date;
  createdAt: Date;
  updatedAt: Date;
}
```

## Quality Gates

- [ ] All endpoints are documented
- [ ] Request/response schemas are clear
- [ ] Error handling is consistent
- [ ] API is versioned
- [ ] Examples are provided
- [ ] Frontend and backend teams have reviewed

## Approval

- [ ] Solution Architect
- [ ] Tech Lead
- [ ] Security Engineer
