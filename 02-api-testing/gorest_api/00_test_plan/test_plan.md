# 🧪 Test Plan – GoRest API Manual + Automation Testing

---

## 📋 Project Overview

This project covers both manual and automated testing of the public GoRest API, focused on validating the `/users` endpoint. It simulates real-world backend QA responsibilities — including CRUD validation, negative testing, authorization, defect documentation, and light automation using Python.

---

## 🎯 Objectives

- Verify the correct behavior of Create, Read, Update, and Delete operations on the `/users` endpoint.
- Validate status codes and response content across positive and negative scenarios.
- Test bearer token authentication enforcement (valid, missing, invalid).
- Document and execute manual test cases using Postman and Qase.
- Write starter automation scripts in Python to demonstrate API test scripting.

---

## 🛠️ Tools and Technologies

| Tool | Purpose |
|------|---------|
| **Postman** | Manual API test execution |
| **Qase** | Test management, execution tracking, and defect logging |
| **Python 3.x** | Automation scripting language |
| **Requests library** | Send API calls in Python |
| **VS Code** | Code editor and project management |
| **GitHub** | Version control and public documentation |
| **Windows 11** | Local test environment |
| **GoRest API** | Application under test (public RESTful service) |

---

## 🔍 Scope of Testing

| In Scope | Out of Scope |
|----------|--------------|
| `/users` endpoint (CRUD) | Other endpoints like `/posts`, `/comments` |
| Token-based auth (positive/negative) | Rate limiting, throttling behavior |
| JSON response validation | GraphQL schema testing |

---

## 📂 Test Artifacts

| Artifact | Description |
|----------|-------------|
| `create-user-tests.md` | Manual test cases for POST `/users` |
| `update-user-tests.md` | Manual test cases for PATCH and DELETE `/users/{id}` |
| `execution-log-qase.xlsx` | Qase export of execution results |
| `gorest-env.json` | Postman environment file (token and base URL) |
| `gorest-user-tests.postman_collection.json` | Postman collection used in execution |
| `defect-log.md` | Simulated defects with expected vs. actual outcomes |
| `README.md` | Project summary and usage overview |
| `automation-ideas.md` | Prioritized automation plan and stack planning |
| `03-test-automation/` | Live automation scripts written in Python |

---

## 🔐 Authentication Setup

- **Token Type:** Bearer Token (manually generated)
- **Stored in Postman Environment Variable:** `{{token}}`
- Required for: `POST`, `PATCH`, `DELETE` operations

---

## 🧪 Test Types

| Type | Description |
|------|-------------|
| Functional | Positive user creation and updates |
| Negative | Missing fields, invalid formats |
| Authorization | Invalid or missing tokens |
| Automated | Light scripting of selected manual tests in Python |

---

## ✅ Entry Criteria

- Postman setup completed with token and base URL
- Test cases written and reviewed in Qase
- Postman requests verified against test case steps

---

## 🛑 Exit Criteria

- Manual test cases executed and logged
- Simulated defects documented
- Automation scripts verified for core workflows
- All artifacts committed to GitHub in organized folders

---

## ⚙️ Automation Overview

Three scripts were created using Python and the `requests` library to demonstrate basic automation:

| Script | What it Tests |
|--------|----------------|
| `test_create_user.py` | Positive test: Create user with valid data (201 Created) |
| `test_negative_create_user.py` | Negative test: Missing email triggers 422 Validation Error |
| `test_auth_invalid_token.py` | Auth test: Invalid token returns 401 Unauthorized |

Future enhancements include using Pytest for better structure and scaling.

---

## 📅 Timeline

| Phase | Date |
|-------|------|
| Manual Test Design | April 2025 |
| Manual Execution | April 2025 |
| Automation Scripting | April 2025 |
| Final Documentation & Commit | April 2025 |

---

## 📁 Repository

All artifacts are publicly available in this GitHub repository:

📁 View the full project here →  
👉 [GoRest API Manual + Automation Project](https://github.com/shontelleQA/qa-portfolio-shontelle-nicole/tree/main/02-api-testing/gorest-api)


---
