# 🧪 API Test Cases Overview – GoRest API

This folder contains structured test cases designed to validate the core API workflows of the GoRest platform. I approached this project from the perspective of a QA analyst working in a real-world SaaS or CRM environment — focusing primarily on CRUD operations, negative validation, and authorization behavior.

All test cases were executed manually using Postman and tracked inside Qase.io to support future automation using Python.

---

## 🔍 What I Tested

| Area | Description |
|------|-------------|
| **User CRUD** | Create, read, update, and delete user records using `/users` endpoints |
| **Authorization** | Positive and negative bearer token handling — valid token, missing token, and invalid token edge cases |
| **Negative Testing** | Invalid payloads (missing fields, bad formats), duplicate data, and operations on deleted resources |
| **Data Integrity** | Verifying the consistency of created and updated user data across endpoints |

---

## 🧱 Test Case Structure

Each test case includes:

- **Title** – Clear, descriptive scenario name
- **Preconditions** – Data/token required before execution
- **Test Steps** – Step-by-step instructions for execution
- **Expected Result** – What should happen if the API behaves correctly
- **Notes** – Any special handling, reusable variables, or edge case coverage

---

## 📂 Linked Test Case Files

| File | Description |
|------|-------------|
| [`create-user-tests.md`](./create-user-tests.md) | Tests for `POST /users`, `GET /users`, and negative creation scenarios |
| [`update-user-tests.md`](./update-user-tests.md) | Tests for `PATCH /users/{id}`, `DELETE /users/{id}`, and negative updates on deleted users |
| [`auth-edge-case-tests.md`](./auth-edge-case-tests.md) | Token-related negative tests — missing token, invalid token |

---

## 💡 Future Automation Notes

Test cases in this folder are written with automation in mind. Variables like `{{baseUrl}}`, `{{token}}`, and `{{userId}}` are used throughout to allow seamless conversion to Python scripting and automation frameworks.

Automation candidates will be prioritized and noted in [`../04-automation-notes/automation-ideas.md`](../04-automation-notes/automation-ideas.md).

---

## ✅ Status

- Manual test case documentation: **Completed**
- Manual test execution: **Completed**
- Test results logged in [`../01-postman-collections/gorest-execution-report.md`](../01-postman-collections/gorest-execution-report.md)

---

