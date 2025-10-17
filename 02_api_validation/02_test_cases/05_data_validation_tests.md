# 🧾 Data Validation Test Cases – GoRest API

This document includes test cases that validate input field constraints for the GoRest API.  
These scenarios confirm the system enforces proper values for enum fields such as `gender` and `status`.

---

## 📋 Preconditions
- Base URL is configured in Postman environment as `{{baseUrl}}`.
- A valid Bearer Token (`{{token}}`) is set in the environment.
- Test payload prepared with all required fields (`name`, `gender`, `email`, `status`).

---

## ❌ Negative Test Cases

### 1. Create User with Invalid Gender Value

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**    | POST                                          |
| **Endpoint**  | `{{baseUrl}}/users`                          |
| **Preconditions** | Valid token; JSON payload with invalid `gender` field |
| **Test Steps** | 1. Send POST request with `gender` value outside of allowed enums.<br>2. Observe response. |
| **Expected Result** | 422 Unprocessable Entity. Response body includes error message about invalid gender. |

**Sample Payload**:
```json
{
  "name": "Invalid Gender User",
  "gender": "banana",
  "email": "invalidgender001@example.com",
  "status": "active"
}
```

### 2. Create User with Invalid Status Value

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**    | POST                                          |
| **Endpoint**  | `{{baseUrl}}/users`                          |
| **Preconditions** | Valid token; JSON payload with invalid `status` field |
| **Test Steps** | 1. Send POST request with `status` value outside of allowed enums.<br>2. Observe response. |
| **Expected Result** | 422 Unprocessable Entity. Response body includes error message about invalid status. |

**Sample Payload**:
```json
{
  "name": "Invalid Status User",
  "gender": "male",
  "email": "invalidstatus001@example.com",
  "status": "paused"
}
```

---

## ✅ Notes
- The official API documentation restricts `gender` to `male` or `female`, and `status` to `active` or `inactive`.
- Actual behavior should be recorded during execution — some APIs may silently accept invalid values, which is a defect worth logging.