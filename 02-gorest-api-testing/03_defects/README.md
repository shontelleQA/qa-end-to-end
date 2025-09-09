# 🐛 Defect Log – GoRest API Manual Testing
> **Note:** Since this project involved manual API testing without a frontend UI, screenshots are not applicable. All defects listed below were simulated for demonstration purposes, based on potential API response discrepancies observed or theorized during test planning.
---

## Defect 001 – Create User without Email Succeeds (Unexpected)

| Field | Value |
|------|-------|
| Feature | User Creation (POST /users) |
| Environment | GoRest Public API v2 |
| Reported By | Shontelle Nicole |
| Severity | Major |
| Priority | High |
| Description | Creating a user without providing an email address returned a `201 Created` response instead of a validation error. |
| Steps to Reproduce | 1. Send POST /users with missing `email` field. <br> 2. Observe the response. |
| Expected Result | API should return 422 Unprocessable Entity with an error message about missing email. |
| Actual Result | API returned 201 Created, and created a user with a blank email. |
| Status | Open |

---

## Defect 002 – Delete Non-Existent User Returns 500 Error

| Field | Value |
|------|-------|
| Feature | Delete User (DELETE /users/{userId}) |
| Environment | GoRest Public API v2 |
| Reported By | Shontelle Nicole |
| Severity | Minor |
| Priority | Medium |
| Description | Deleting a non-existent user ID returns a 500 Internal Server Error instead of a 404 Not Found. |
| Steps to Reproduce | 1. Send DELETE /users/9999999999 (non-existent ID). <br> 2. Observe the response. |
| Expected Result | API should return 404 Not Found. |
| Actual Result | API returned 500 Internal Server Error. |
| Status | Open |

---

