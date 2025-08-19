# 🔄 Update & Delete User API Test Cases – GoRest API

This document includes test cases for updating and deleting users using the `PATCH` and `DELETE` methods. These tests demonstrate control over entity state and response handling across different conditions.

---

## 📋 Preconditions
- A valid user has already been created and stored as `{{userId}}` in the Postman environment.
- A valid Bearer Token (`{{token}}`) is set in the environment.
- Base URL (`{{baseUrl}}`) is also configured.

---

## ✅ Positive Test Cases

### 1. Update Existing User – Valid Data

| Field | Value |
|------|-------|
| Method | PATCH |
| Endpoint | `{{baseUrl}}/users/{{userId}}` |
| Preconditions | `userId` points to an existing user |
| Test Steps | 1. Send PATCH request with new `name` and `status`.<br>2. Verify response. |
| Expected Result | 200 OK. Response body reflects updated values. |

Sample Payload:
```json
{
  "name": "Updated Test User",
  "status": "inactive"
}
```

---

### 2. Delete Existing User

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**     | DELETE                                        |
| **Endpoint**   | `{{baseUrl}}/users/{{userId}}`                |
| **Preconditions** | `userId` is set and points to a valid, existing user |
| **Test Steps** | 1. Send DELETE request to the user endpoint.<br>2. Send a follow-up GET request to `{{baseUrl}}/users/{{userId}}`. |
| **Expected Result** | 204 No Content on DELETE.<br>Follow-up GET returns 404 Not Found. |
| **Notes**      | Confirms proper user deletion and cleanup of resources. Use the same `userId` from Test 1 or a freshly created user. |

---

### 3. Attempt to Update a Deleted User

| Field         | Value                                          |
|---------------|------------------------------------------------|
| **Method**     | PATCH                                          |
| **Endpoint**   | `{{baseUrl}}/users/{{userId}}`                 |
| **Preconditions** | The `userId` refers to a user that has already been deleted (from Test 2). |
| **Test Steps** | 1. Send a PATCH request with valid JSON payload (e.g., updated name).<br>2. Observe the response code and message. |
| **Expected Result** | 404 Not Found. Response should indicate the resource no longer exists. |
| **Sample Payload** | ```json<br>{<br>  "name": "Should Not Work",<br>  "status": "active"<br>}<br>``` |
| **Notes**      | This test verifies that deleted users cannot be modified and ensures the API respects deletion rules. |
