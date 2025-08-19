# 🧪 Create User API Test Cases – GoRest API

This document outlines the positive and negative test cases for the `POST /users` and `GET /users` endpoints.

All tests are designed to validate user creation behavior, input validation, and proper error handling.

---

## 📋 Preconditions
- Valid Bearer Token is available and set in the Postman environment (`{{token}}`).
- Base URL is set as an environment variable (`{{baseUrl}}`).
- Unique email addresses must be used for successful user creation tests.

---

## ✅ Positive Test Cases

### 1. Create User with Valid Data

| Field         | Value |
|---------------|-------|
| **Method**    | POST |
| **Endpoint**  | `{{baseUrl}}/users` |
| **Preconditions** | Valid token; JSON payload with all required fields |
| **Test Steps** | 1. Send POST request with name, gender, email, status.<br>2. Verify response. |
| **Expected Result** | 201 Created. Response body matches input. New user ID returned. |

**Sample Payload**:
```json
{
  "name": "QA Test User",
  "gender": "female",
  "email": "qatestuser001@example.com",
  "status": "active"
}
```

---

### 2. Retrieve Created User by ID

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**    | GET                                           |
| **Endpoint**  | `{{baseUrl}}/users/{{userId}}`               |
| **Preconditions** | Valid token; successful user creation in Test 1 |
| **Test Steps** | 1. Send GET request with a valid user ID.<br>2. Observe response and verify values match the previously created user. |
| **Expected Result** | 200 OK. Response body contains correct user details including `name`, `email`, and `status`. |

---

## ❌ Negative Test Cases

### 3. Create User with Missing Required Field (Email)

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**    | POST                                          |
| **Endpoint**  | `{{baseUrl}}/users`                          |
| **Preconditions** | Valid token |
| **Test Steps** | 1. Send POST request omitting the `email` field.<br>2. Observe response. |
| **Expected Result** | 422 Unprocessable Entity. Response body includes error message stating that `email` is required. |

**Sample Payload**:
```json
{
  "name": "QA Test User Missing Email",
  "gender": "male",
  "status": "active"
}
```

---


---

### 4. Create User with Invalid Email Format

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**    | POST                                          |
| **Endpoint**  | `{{baseUrl}}/users`                          |
| **Preconditions** | Valid token |
| **Test Steps** | 1. Send POST request with improperly formatted email.<br>2. Observe response. |
| **Expected Result** | 422 Unprocessable Entity. Error message about invalid email format is returned. |

**Sample Payload**:
```json
{
  "name": "Invalid Email User",
  "gender": "male",
  "email": "invalid-email-format",
  "status": "active"
}
```

---


---

### 5. Create Duplicate User (Same Email)

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**    | POST                                          |
| **Endpoint**  | `{{baseUrl}}/users`                          |
| **Preconditions** | Valid token; previously used email from successful user creation |
| **Test Steps** | 1. Send POST request using an email that was already used in a previous test.<br>2. Observe response. |
| **Expected Result** | 422 Unprocessable Entity. Response body includes message about email already being taken. |

**Sample Payload**:
```json
{
  "name": "Duplicate User",
  "gender": "female",
  "email": "qatestuser001@example.com",
  "status": "active"
}
