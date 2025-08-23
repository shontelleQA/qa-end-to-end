# 🧪 GoRest API – Systems-Assurance Case Study (Users Service)

**Scope:** Validate Users CRUD and authorization for a public REST API, covering happy paths, error handling, and minimal contract/pagination checks. Executed in Postman with Phase 1 Python automation.

---

## 🎯 Why It’s Here (Signal)
- **UI/API/Data/Compliance breadth:** Manual + automated API validation with auth edges, negative testing, and traceable artifacts.  
- **SDET trajectory:** Ready to scale into Pytest + CI and add schema/contract tests.

---

## Objectives
- Validate CRUD for `/users` with realistic data.  
- Exercise authorization: valid, invalid, missing, (simulated) expired.  
- Confirm error handling: 422 validations, 401/403 auth failures.  
- Add light contract + pagination checks for reliability.  
- Produce recruiter-readable artifacts and Phase 1 automation.  

---

## 🛠️ Tools
| Area              | Tool                                |
|-------------------|-------------------------------------|
| Manual execution  | Postman (collection, env, runner)   |
| Test management   | Qase.io (planning & execution logs) |
| Automation        | Python 3.x + `requests`             |
| Docs              | Markdown (this repo)                |
| Version control   | GitHub                              |

---

## 🔐 Environment & Auth
- **Base:** `https://gorest.co.in/public/v2`  
- **Bearer token** stored in Postman env (`{{token}}`).  
- **Dynamic vars:** `{{userId}}` captured on create → reused for update/delete.  

> “Expired token” is simulated by using a deliberately revoked/garbage token and documenting the expected behavior.

---

## ✅ What I Tested

**Positive:**  
- `POST /users` with valid payload → 201; persisted via `GET /users/:id`.  
- `PATCH /users/:id` to update name/status → 200; field-level assert.  
- `DELETE /users/:id` → 204; follow-up `GET` → 404.  

**Negative & Auth:**  
- Missing required fields (email) → 422 with field message.  
- Invalid email format / duplicate email → 422.  
- Invalid token → 401; Missing token → 401; Expired token (sim) → 401/403.  

**Reliability checks (lightweight):**  
- **Contract:** minimal JSON schema for `POST`/`GET` response (id, name, email, gender, status).  
- **Pagination:** `GET /users?page=1` vs `page=2` non-overlap & expected page size.  
- **Idempotency:** retry `POST` with same email → 422 consistently.  

---

## 📂 Evidence
| Artifact | Link |
|----------|------|
| Test Plan | [00_test_plan/](00_test_plan/) |
| Postman (collection, env, run report) | [01_postman_collections/](01_postman_collections/) |
| Manual Test Cases | [02_test_cases/](02_test_cases/) |
| Defect Reports (simulated) | [03_defects/](03_defects/) |
| Automation Notes | [04_automation_notes/](04_automation_notes/) |
| Python Tests (Phase 1) | [05_python_tests/](05_python_tests/) |
   |

---

## 📊 Outcomes
- **Auth validated** → Confirmed only valid tokens can access resources, reducing risk of unauthorized data exposure.  
- **Data validation enforced** → API rejects malformed/duplicate emails (422), preventing downstream data corruption and ensuring reliable user records.  
- **Reliability checks added** → Contract and pagination sanity tests provide early warning for schema drift or query inconsistencies, boosting system resilience.  
- **Phase 1 automation delivered** → Python scripts now cover key flows; the structure is ready to scale into Pytest + CI/CD for faster regression feedback.  
  

---

## 🔮 Next Automation
- Migrate to **Pytest** with markers: `smoke`, `auth`, `neg`, `contract`.  
- Add JSON Schema validation library for response shape (contract tests).  
- Wire into **GitHub Actions** to run on push; store collection + env as artifacts.  
- Optional: add data seeding/cleanup helpers and minimal Allure report.  

---

## 🧩 Role-Signal Map
| Role Signal             | How this project shows it |
|--------------------------|---------------------------|
| Sr App Dev Eng (SDET)   | Negative tests, auth edges, contract checks, automation structure |
| IAM Analyst             | Token handling, missing/invalid/expired cases, error exposure review |
| Data Validation (QA ↔ Data) | Field constraints (email), deterministic IDs, pagination consistency → mirrors the same validation mindset used in data analyst roles (spotting anomalies, ensuring integrity). |
| Governance/Process      | Clear plan → cases → evidence → outcomes; defects documented and reproducible |

---

## 📁 Repo Structure
```text
02-gorest-api-testing/
├─ 00_test_plan/            # README.md (scope, risks, data, exit criteria)
├─ 01_postman_collections/  # collection, environment, run reports
├─ 02_test_cases/           # CRUD, auth, negative scenarios
├─ 03_defects/              # README.md (simulated defects + repro)
├─ 04_automation_notes/     # README.md (what's automated + backlog)
├─ 05_python_tests/         # Phase 1 scripts
└─ README.md                # (this file)
```


---

## 📝 Notes for Reviewers
Public demo API; defects are partly simulated to demonstrate logging and analysis. Automation is intentionally minimal and readable for hiring managers.
