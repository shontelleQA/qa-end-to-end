# 🧪 GoRest API – Manual API Testing Project

This project documents manual functional testing of the public GoRest API, focusing on CRUD operations for user management.

The goal was to simulate realistic API validation scenarios a QA Engineer would encounter when testing a SaaS or CRM-style backend system — including positive, negative, and authorization-based testing workflows. The project was manually executed using Postman and tracked inside Qase.io for structured reporting.

---

## 🎯 Project Objectives

- Validate core CRUD operations (`Create`, `Read`, `Update`, `Delete`) for the `/users` endpoints.
- Cover positive scenarios (valid data) and negative scenarios (invalid/missing/duplicate data).
- Test authentication behavior using bearer tokens (positive and negative authorization cases).
- Document testing artifacts in a recruiter-readable, portfolio-ready structure.
- Prepare all test cases for future automation using Python and API frameworks.

---

## 🛠️ Tools and Technologies

| Tool | Purpose |
|------|---------|
| **Postman** | Manual API request execution |
| **Qase.io** | Test management and execution tracking |
| **GitHub** | Portfolio version control |
| **Markdown** | Test documentation and reporting |

---

## 🔐 Authentication

- The GoRest API requires authentication for `POST`, `PATCH`, and `DELETE` requests.
- A Bearer Token is required and stored securely in the Postman environment file (`gorest-env.json`).
- The token is automatically referenced in Authorization headers using the Postman variable `{{token}}`.

---

## 🌐 Environment Setup

| Variable | Purpose |
|----------|---------|
| `{{baseUrl}}` | Base URL for all API requests (`https://gorest.co.in/public/v2`) |
| `{{token}}` | Bearer Token for secured endpoints |
| `{{userId}}` | Captured dynamically during Create User tests for use in Update/Delete workflows |
| `{{postId}}` | Captured dynamically during Post creation tests (future scope) |

All environment variables are preconfigured in the `gorest-env.json` file for seamless request execution.

---

## 📂 Folder Structure Overview

| Folder | Purpose |
|--------|---------|
| `01-postman-collections/` | Postman collection, environment, and execution reports |
| `02-test-cases/` | Structured manual test cases for CRUD, auth, and nested resource testing |
| `03-defects/` | Bug logging if defects are found during manual execution |
| `04-automation-notes/` | Future automation ideas and candidate tests for Python scripting |
| `05_test_automation/` | Phase 1 automation scripts using Python + Requests (Create, Negative, Auth tests) |

---

## ✅ Status

- Manual test cases: **Completed** (Create, Read, Update, Delete + negative scenarios)
- Manual test execution: **Completed** (Logged via Postman and Qase.io)
- Defects observed:
  - 422 validation error confirmed when required fields are missing (e.g., email)
  - 401 Unauthorized error confirmed when using invalid tokens
- Phase 1 automation scripts: **Completed** using Python + Requests
- Ready for future expansion with Pytest and reporting tools


---

## ⚙️ Automation Expansion (Phase 1 Complete)

- Phase 1 automation scripts have been added inside `05_test_automation/`.
- Python + Requests used for scripting selected Create, Negative Create, and Authorization test cases.
- Scripts are standalone, beginner-to-mid level recruiter friendly, and designed for easy future migration to Pytest.
- Manual and automated validation now both documented in this project.
