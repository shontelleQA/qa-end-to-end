# 🟠 OrangeHRM Employee Flow – Test Plan

## 📌 Project Overview

This test plan defines the QA approach for validating the Employee Flow in the OrangeHRM demo application. The objective was to ensure that critical HR workflows (login, employee creation, and record verification) function reliably in a realistic admin scenario. Testing combined functional UI validation, form validation, and exploratory checks to uncover edge cases.

---

## 🎯 Objectives

- Validate Admin login/logout flows across Chrome and Firefox.  
- Ensure new employee creation succeeds with required details.  
- Confirm that newly added employees appear in the admin employee list.  
- Verify field-level and form-level error handling for invalid data.  
- Capture defects with supporting screenshots and traceability to cases. 

---

## 🧪 Scope

### In Scope
- Admin login/logout
- Navigation to PIM > Add Employee
- Creating a new employee with valid and invalid data
- Employee record validation via employee list  
- Basic cross-browser validation (Chrome, Firefox)  


### Out of Scope
- Backend API validation  
- Role-based access control beyond Admin  
- File/document upload workflows 

---

## 🧰 Test Environment

- **URL**: https://opensource-demo.orangehrmlive.com/  
- **Browsers**: Chrome (v135.0.7049.96), Firefox (v137.0.2)  
- **OS**: Windows 11  
- **Test Data**: Static employee dataset (Excel) 

---

## ⏱️ Timeline

| Activity | Duration | Status                        |  
|----------|----------|-------------------------------|  
| Test Case Design | 1 day | ✅ Complete                    |  
| Test Execution | 1 day | ✅ Complete                    |  
| Defect Logging | Ongoing | ✅ Logged 2 functional defects |  
| Final Reporting | 0.5 day | ✅ Delivered                   |  

---

## 👩🏽‍💻 Roles & Responsibilities

| Name | Role |  
|------|------|  
| Nicole Nealy | QA Analyst – Test design, execution, defect reporting |  

---

🔍 Entry & Exit Criteria  
**Entry**  
- OrangeHRM demo site accessible.  
- Functional flow validated via exploratory smoke tests.  
- Test cases authored and reviewed.  

**Exit**  
- All high-priority test cases executed.  
- All critical defects logged and retested.  
- Test summary and RTM finalized.  

🛠️ Tools & Tracking  
- **Test Design/Execution**: Qase (cases, test runs, logs)  
- **Defect Tracking**: Qase defect log + exports  
- **Reporting**: Qase exports (PDF/XLSX)  
- **Screenshots**: Captured at runtime, linked to defects  

✅ Deliverables (Evidence)  
- **Test Cases**: `test-cases-qase.xlsx` (full coverage set)  
- **Execution Log**: `execution-log-qase.pdf` (pass/fail record)  
- **Defects**: `defect-report-qase.pdf` (2 logged issues: self-as-contact, blank name, emoji rendering)  
- **RTM**: `rtm.xlsx` (requirements mapped to cases + defects)  
- **Screenshots**: `/screenshots/` (visual proof of flows + bugs)  
- **README.md**: Case-study summary (scope, risks, results)  
- **This Test Plan**: Formal documentation of QA approach  

📊 Outcomes  
- **Defects found**: 2 functional issues tied to employee creation/validation.  
- **Impact**: Documented risks around input validation, user data integrity, and UI handling of special characters.  
- **Next Step**: Recommend automation of login and employee-add flows in Selenium for regression stability.  
