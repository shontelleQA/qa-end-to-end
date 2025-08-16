# 🟠 OrangeHRM Employee Management Testing Project

This project demonstrates QA of the **Employee Management** workflow inside the [OrangeHRM Open Source Demo](https://opensource-demo.orangehrmlive.com/).

It simulates a real sprint cycle including test planning, manual test case design, execution tracking, and defect reporting. All artifacts are preserved in this folder to show a complete QA workflow, from scope to outcomes.

---

## 📁 Project Structure

```bash
01-live-app-testing/
└── 01-orangehrm-employee-flow/
    ├── test-plan/           # Test plan (scope, env, objectives, outcomes)
    ├── test-cases/          # Test design (XLSX + PDF export)
    ├── execution-logs/      # Test run results (XLSX + PDF export)
    ├── defect-reports/      # Markdown write-ups + Qase export
    ├── rtm/                 # Requirements Traceability Matrix
    ├── screenshots/         # Evidence of execution + defects
    └── README.md            # This case-study overview
```

---

## 🎯 Scope of Testing

- User login and logout flows
- Adding a new employee (valid + invalid data)- Searching for an employee in the directory
- Employee record validation in admin list
- Form-level and field-level error handling
- Field reset/cancel functionality
- Basic cross-browser validation (Chrome + Firefox)

---

## ⚙️ Tools & Tech Used

| Tool | Purpose |
|------|---------|
| Qase Test Management | Test case organization and execution tracking |
| Google Sheets (Excel export) | Test case management and RTM backup |
| VS Code + GitHub | Portfolio and artifact version control |
| Markdown | Documentation and reporting |
| Windows Snipping Tool | Screenshots for test evidence |

> 📌 **Note:** While Jira is a common industry standard for defect tracking and test management, this project uses [Qase.io](https://qase.io/) to simulate real-world workflows. Qase provides similar functionality for organizing test cases, managing execution cycles, and tracking defects — aligning closely with Agile QA practices.


---

## 📂 Project Artifacts

| Artifact | Description |
|----------|-------------|
| `Test_Plan.md` | Test scope, objectives, environment, risks, and strategy |
| `Test_Cases.xlsx` | Full manual test case set (positive, negative, edge cases) |
| `Execution_Log.xlsx` | Test run tracking and pass/fail status |
| `Defect_Report.md` | Documented defects found during execution |
| `RTM.xlsx` | Requirements mapped to corresponding test cases |
| `screenshots/` | Visual evidence of tests and defects |

---

## 🎯 Role Alignment

This project demonstrates core QA analyst responsibilities:

- ✅ Manual test case design and structured execution
- ✅ Defect identification, logging, and retesting workflows
- ✅ Requirements mapping and traceability practices
- ✅ Exploratory mindset for edge cases and validation scenarios
- ✅ Agile sprint simulation with deliverable artifacts

---

## 🔁 Sprint Summary

| Sprint | Focus | Result |
|--------|-------|--------|
| Sprint 1 | Core Employee Flow | 12 test cases executed, 2 defects identified and retested |
| Sprint 2 (Planned) | Permissions Testing | Extend coverage to role-based access (future enhancement) |

---

## 📫 Let’s Connect

I’m open to QA opportunities (manual or hybrid) across healthcare, edtech, and mission-driven products.  
Let's connect for a **coffee chat** ☕ or to talk all things quality and testing:

📍 [Connect with me on LinkedIn](https://www.linkedin.com/in/nicole-nealy/)

---

🧪 *Built with real QA process. Documented with care. Tested like a user, thought through like a developer.*
