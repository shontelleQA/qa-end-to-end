# 🟠 OrangeHRM Employee Flow – Test Plan

## 📌 Project Overview

This test plan covers functional testing of the **Employee Flow** in the OrangeHRM demo application. The goal is to validate that users can log in, add a new employee, and verify employee details through the admin panel. Testing includes UI validation, functional flow, and basic error handling.

---

## 🎯 Objectives

- Verify that login functionality works for Admin users
- Ensure new employee creation is successful with required details
- Confirm added employee appears in the employee list
- Validate field-level and form-level error messages
- Confirm logout functionality

---

## 🧪 Scope

### In Scope
- Admin login/logout
- Navigation to PIM > Add Employee
- Creating a new employee with valid and invalid data
- Verifying employee details via employee list
- Basic cross-browser validation in Firefox for login flow


### Out of Scope
- Backend API testing
- Role-based access control
- Employee document uploads

---

## 🧰 Test Environment

- **Application URL:** https://opensource-demo.orangehrmlive.com/
- **Test Browser(s):** Chrome (v135.0.7049.96)
OS: (Windows 11), Firefox (v137.0.2)
- **Test Data:** Static employee data stored in Excel

---

## ⏱️ Timeline

| Activity              | Duration       | Status     |
|-----------------------|----------------|------------|
| Test Case Design      | 1 day          | ✅ Complete |
| Test Execution        | 1 day          | 🔄 In Progress |
| Defect Logging        | Ongoing        | ⏳ Pending |
| Final Reporting       | 0.5 day        | ⏳ Pending |

---

## 👩🏽‍💻 Roles & Responsibilities

| Name          | Role                     |
|---------------|--------------------------|
| Nicole Nealy  | QA Analyst / Tester      |

---

## 🔍 Entry & Exit Criteria

**Entry Criteria:**
- OrangeHRM demo site is accessible
- Functional flow is confirmed through exploratory testing
- Test cases are reviewed

**Exit Criteria:**
- All high-priority test cases executed
- All critical defects logged and retested
- Final test summary completed

---

## 🛠️ Tools Used

- Test Case Management: Qase (test design, organization, and test suite structure)
- Test Execution: Qase (manual execution with step-level tracking and result logging)
- Defect Tracking: Qase (linked to failed test cases and exported for reporting)
- Reporting & Traceability: Qase exports (PDF/XLSX for test cases, execution logs, defects)
- Screenshots: Captured during test execution and stored in `screenshots/` folder

---

## ✅ Deliverables

- `test-cases-qase.pdf` – Export of all test cases from Qase
- `execution-log-qase.pdf` – Test run summary with pass/fail results
- `defect-report-qase.pdf` – Exported list of all logged defects
- `traceability-matrix-qase.xlsx` – (optional) RTM generated or approximated via Qase case-defect links
- `screenshots/` – Visual proof of execution steps and bugs
- `README.md` – Summary of test objectives, coverage, and QA approach
- `test-plan.md` – This file, detailing the structured QA process
