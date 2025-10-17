# 🔐 Auth Edge Case Test Cases – GoRest API

This document outlines test cases related to authentication and authorization handling for the GoRest API.  
These scenarios verify that the system properly enforces security requirements when a request is made without valid credentials.

---

## 📋 Preconditions
- Base URL is configured in Postman environment as `{{baseUrl}}`.
- Test payload prepared with valid `name`, `gender`, `email`, and `status`.
- No valid token (missing or invalid) is supplied for negative cases.

---

## ❌ Negative Test Cases

### 1. Missing Token – Create User Request

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**    | POST                                          |
| **Endpoint**  | `{{baseUrl}}/users`                          |
| **Preconditions** | Valid payload prepared; Authorization header omitted |
| **Test Steps** | 1. Send POST request with all required fields but no Authorization header.<br>2. Observe the response. |
| **Expected Result** | 401 Unauthorized (or 403 Forbidden, depending on API behavior). Response body indicates missing authentication. |

**Sample Payload**:
```json
{
  "name": "Unauthorized User",
  "gender": "male",
  "email": "unauthuser001@example.com",
  "status": "active"
}
```

### 2. Invalid/Expired Token – Create User Request

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**    | POST                                          |
| **Endpoint**  | `{{baseUrl}}/users`                          |
| **Preconditions** | Valid payload prepared; Authorization header set with invalid token (e.g., `Bearer bad_token`). |
| **Test Steps** | 1. Send POST request with Authorization header using invalid token value.<br>2. Observe the response. |
| **Expected Result** | 401 Unauthorized or 403 Forbidden. Response body includes error message about invalid/expired token. |

**Sample Payload**:
```json
{
  "name": "Expired Token User",
  "gender": "female",
  "email": "expiredtoken001@example.com",
  "status": "inactive"
}
```

---

## ✅ Notes
- These tests confirm the API rejects unauthorized requests and does not allow resource creation without valid tokens.
- Actual observed behavior (401 vs 403) should be recorded in the execution log and attached as evidence.