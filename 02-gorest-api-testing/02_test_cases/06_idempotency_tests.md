# 🔄 Idempotency Test Cases – GoRest API

This document outlines test cases that verify the GoRest API's behavior when the same request is submitted multiple times.  
The goal is to ensure the system prevents duplicate records and responds consistently.

---

## 📋 Preconditions
- Base URL is configured in Postman environment as `{{baseUrl}}`.
- A valid Bearer Token (`{{token}}`) is set in the environment.
- Test payload prepared with all required fields (`name`, `gender`, `email`, `status`).
- Fixed email value is reused across duplicate requests to trigger idempotency behavior.

---

## ❌ Negative Test Cases

### 1. Create User Twice with Same Email

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**    | POST                                          |
| **Endpoint**  | `{{baseUrl}}/users`                          |
| **Preconditions** | Valid token; first request successfully creates a new user |
| **Test Steps** | 1. Send POST request with valid payload and unique email.<br>2. Send a second POST request with the same payload (same email).<br>3. Observe both responses. |
| **Expected Result** | - First request → `201 Created`, response body contains new user details and `id`.<br>- Second request → `422 Unprocessable Entity`, response body includes error message stating that the `email` has already been taken. |

**Sample Payload (used for both requests)**:
```json
{
  "name": "Duplicate Email User",
  "gender": "female",
  "email": "idempotencyuser001@example.com",
  "status": "active"
}
```

---

## ✅ Notes
- This test ensures the API enforces unique constraints on user emails.
- Idempotency is critical in preventing duplicate records when requests are retried due to network or system errors.
- Actual observed responses should be attached as evidence in the execution log.