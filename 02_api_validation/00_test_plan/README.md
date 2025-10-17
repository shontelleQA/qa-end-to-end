# 🧪 Test Plan — GoRest API (Users) — Manual + Starter Automation

---

## 📋 Overview
End-to-end validation of the public GoRest **Users** service covering Create/Read/Update/Delete (CRUD), authorization behavior, field/data validation, and light contract and pagination checks. Executed manually in Postman and tracked in Qase; Phase-1 automation in Python (`requests`) for a few high-signal tests.

---

## 🎯 Objectives
- Validate CRUD for `/users`.
- Exercise authorization paths: valid, missing, invalid, and expired/revoked (sim).
- Confirm data validation: required fields, email format, uniqueness, enum fields.
- Add reliability signals: minimal JSON schema (contract) checks and pagination sanity.
- Provide reproducible artifacts + runnable starter automation.

---

## 🛠️ Tools
| Area              | Tool                                |
|-------------------|-------------------------------------|
| Manual execution  | Postman (collections, env, runner)  |
| Test management   | Qase.io                             |
| Automation        | Python 3.x + `requests` (Pytest planned) |
| Repo/docs         | GitHub + Markdown                   |
| OS                | Windows 11                          |
| AUT               | `https://gorest.co.in/public/v2`    |

---

## 🔍 Scope
| In Scope                                    | Out of Scope                           |
|---------------------------------------------|-----------------------------------------|
| `/users` CRUD                               | Other endpoints (`/posts`, `/comments`) |
| Auth (valid/missing/invalid/expired sim)    | Full security pen-testing               |
| Data validation (required/format/enum)      | Perf/load beyond light rate-limit probe |
| Contract (JSON schema), Pagination sanity   | Full contract suite across all resources |

---

## 🔐 Environment & Auth
- **Base URL:** `https://gorest.co.in/public/v2`
- **Token:** Bearer, stored as `{{token}}` in Postman env.
- **Vars:** `{{baseUrl}}`, `{{token}}`, `{{userId}}` (captured on create).
- **Expired token** is simulated by using an intentionally revoked/garbage token and documenting the expected 401/403 behavior.

---

## 🧪 Test Types
| Type          | Examples |
|---------------|----------|
| Functional    | Create, Get by ID, Update, Delete |
| Negative      | Missing fields, invalid email, duplicate email, invalid enums |
| Authorization | Valid, missing, invalid, expired (sim) |
| Contract      | Validate response shape for Create + Get by ID with JSON schema |
| Reliability   | Idempotency (duplicate create), Pagination sanity |

---

## 📂 Test Artifacts
- **Test Cases:** [test_cases/](../02_test_cases/)  
  - [create_user_tests.md](../02_test_cases/02_create_user_tests.md)  
  - [update_user_tests.md](../02_test_cases/03_update_user_tests.md)  
  - [auth_edge_case_tests.md](../02_test_cases/04_auth_edge_case_tests.md)  
  - [data_validation_tests.md](../02_test_cases/05_data_validation_tests.md)  
  - [idempotency_tests.md](../02_test_cases/06_idempotency_tests.md)  
  - [pagination_tests.md](../02_test_cases/07_pagination_tests.md)  

- **Postman:** `./postman/`  
  - `gorest-user-tests.postman_collection.json`  
  - `gorest-env.json`  
  - `schemas/user.create.response.schema.json`  
  - `schemas/user.get.response.schema.json`  
  - *(optional)* run report / screenshots  

- **Defects:** `./defects/README.md`  
- **Automation Notes:** `./automation-notes/README.md`  
- **Python Tests:** `./python-tests/` (Phase-1 scripts)  
- **Execution Logs:** Qase export in `./postman/` or `./defects/`  

---

## ✅ Entry Criteria
- Postman env configured (`{{baseUrl}}`, `{{token}}`).  
- Seed data approach defined (unique emails via timestamp).  
- Test cases reviewed and linked to collection requests.  

---

## 🛑 Exit Criteria
- Manual cases executed with results in Qase.  
- High-signal checks executed (contract, pagination, idempotency).  
- Phase-1 automation runs locally and passes.  
- Artifacts committed with working links.  

---

## ⚙️ Automation Overview
- **Current scripts:**  
  - `test_create_user.py` → 201 create, capture `id`, verify via GET  
  - `test_negative_create_user.py` → 422 missing email  
  - `test_auth_invalid_token.py` → 401 invalid token  

- **Next automation:**  
  - Add Pytest structure + markers (`smoke`, `auth`, `neg`, `contract`, `paging`)  
  - Automate idempotency + pagination checks  
  - Add schema validation with `jsonschema`  

---

## 🗓️ Timeline
- Manual design & execution: April 2025  
- Phase-1 automation (basic Python): April 2025  
- Systems-assurance expansion (manual + planned automation): August 2025  
- Pytest + CI integration: September 2025  

---

## 🔗 Repository
This folder: `02-gorest-api-testing/`

---

## 💡 Notes for Reviewers
This project uses a public demo API. Some defects are **simulated for demonstration**. Contract checks are intentionally minimal to keep the project recruiter-readable.
