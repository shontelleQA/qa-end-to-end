# 🐞 Bug Taxonomy Cheat Sheet

Clear categorization of defects helps prioritize fixes, communicate risks, and maintain product quality — especially in critical sectors like healthcare, insurance, and government technology.

This cheat sheet outlines common types of software bugs, examples based on real-world applications, and how I prioritize and communicate defects during testing.

---

## 🐛 Common Bug Types

| Bug Type | Description | Example |
|:---|:---|:---|
| Functional Defect | The system doesn't work according to requirements or user expectations. | Claim submission button doesn't trigger backend validation. |
| Usability Issue | The system works but is confusing, inefficient, or frustrating to use. | Appointment scheduling flow buries key options several clicks deep. |
| Data Integrity Bug | Information is lost, corrupted, or inaccurately displayed/stored. | Patient record fields overwrite prior entries without warning. |
| Security Vulnerability | The system improperly exposes data or allows unauthorized access. | Claim history visible without login under certain conditions. |
| Compatibility Issue | Application behaves differently across devices, browsers, or OS versions. | Payment portal fails to load on mobile Safari. |
| Performance Defect | System responds too slowly, crashes under load, or hangs. | Healthcare portal takes 20+ seconds to load after login. |
| Accessibility Barrier | Application isn't usable by people with disabilities (vision, mobility, etc.). | No screen reader labels for vital form fields in insurance application. |

---

## ⚡ Severity vs Priority

| Term | Meaning | Example |
|:---|:---|:---|
| Severity | Impact of the bug on system functionality or users. | "Critical" — app crashes when submitting a claim. |
| Priority | How urgently the bug should be fixed relative to business needs. | "High" — minor UI bug on login page of a live MedTech system. |

I evaluate and log bugs with both **severity** and **priority** to help stakeholders make informed release decisions.

---

## 🛠️ My Defect Logging Best Practices

When documenting bugs, I ensure:
- **Clear Title** — Short, specific (e.g., "Submit Button Unresponsive on Claims Page").
- **Detailed Steps to Reproduce** — Including environment, credentials if needed, and any relevant data inputs.
- **Observed vs Expected Behavior** — Clear contrast.
- **Attachments** — Screenshots, screen recordings, or logs when available.
- **Impact Statement** — Quick explanation of who/what is affected ("High-risk for claims processing delays").

---

## 🔗 Related Work

- [OrangeHRM Employee Flow Testing](../01_ui_workflow_testing/OrangeHRM_EmployeeFlow/03_execution_logs/) — Example of structured defect reporting during manual testing.
- [GoRest API Testing](../02-api-testing/gorest_api/03_defects/) — Sample defect logging for API workflow validations.



