# 📑 Pagination Test Cases – GoRest API

This document outlines test cases that verify pagination behavior of the GoRest API.  
These scenarios confirm that records are properly divided across pages without duplication.

---

## 📋 Preconditions
- Base URL is configured in Postman environment as `{{baseUrl}}`.
- A valid Bearer Token (`{{token}}`) is set in the environment.
- The `/users` endpoint contains multiple user records to allow meaningful pagination.

---

## ✅ Positive Test Cases

### 1. Retrieve Page 1 of Users

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**    | GET                                           |
| **Endpoint**  | `{{baseUrl}}/users?page=1`                   |
| **Preconditions** | Valid token |
| **Test Steps** | 1. Send GET request for page 1.<br>2. Observe response. |
| **Expected Result** | 200 OK. Response contains a non-empty array of user objects. Each user object includes `id`, `name`, `email`, `gender`, and `status`. |

---

### 2. Retrieve Page 2 of Users

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**    | GET                                           |
| **Endpoint**  | `{{baseUrl}}/users?page=2`                   |
| **Preconditions** | Valid token |
| **Test Steps** | 1. Send GET request for page 2.<br>2. Observe response. |
| **Expected Result** | 200 OK. Response contains a non-empty array of user objects. Data is distinct from page 1. |

---

## ❌ Negative/Validation Test Cases

### 3. Verify No Overlap Between Page 1 and Page 2

| Field         | Value                                         |
|---------------|-----------------------------------------------|
| **Method**    | GET                                           |
| **Endpoint**  | `{{baseUrl}}/users?page=1` and `{{baseUrl}}/users?page=2` |
| **Preconditions** | Valid token; multiple user records exist |
| **Test Steps** | 1. Retrieve user IDs from page 1.<br>2. Retrieve user IDs from page 2.<br>3. Compare both sets of IDs. |
| **Expected Result** | No overlapping IDs between page 1 and page 2. Both responses should contain distinct records. |

---

## ✅ Notes
- These tests validate that pagination works as expected and prevents data duplication across pages.
- If overlapping IDs are observed, it indicates a defect in pagination logic.
- Evidence should include screenshots of both responses and comparison of ID sets.