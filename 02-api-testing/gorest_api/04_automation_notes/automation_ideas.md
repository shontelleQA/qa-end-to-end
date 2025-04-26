# 🤖 Automation Planning – GoRest API Project

---

## 📋 Goal

To automate selected GoRest API test cases using Python, focusing first on:

- Positive Create/Read/Update/Delete (CRUD) flows
- Negative scenarios like missing required fields
- Authorization edge cases (e.g., missing or invalid tokens)

---

## 🧪 Initial Test Cases Selected for Automation

| Manual Test Title | Automation Priority | Notes |
|-------------------|----------------------|-------|
| Create User with Valid Data | High | Core happy path, validates POST functionality |
| Create User Missing Email | High | Important negative validation |
| Update Existing User | Medium | Verifies PATCH functionality |
| Delete Existing User | Medium | Validates DELETE endpoint behavior |
| Retrieve User with Invalid ID | Low | Optional edge case for GET endpoint |

---

## 🛠️ Potential Tools and Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| Requests library | Sending API requests |
| Pytest | Test organization and execution |
| JSON Schema Validation (optional) | Validate API responses |

---

## 🔥 Stretch Goals (Future Enhancements)

- Data-driven tests using JSON or CSV
- Integration with a simple CI/CD setup (e.g., GitHub Actions)
- Enhanced reporting (e.g., Allure or HTML reports)

---
