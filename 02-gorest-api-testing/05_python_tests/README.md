# GoRest API Automation – Phase 1

This folder contains my starter automation scripts for the GoRest API.

## 👏🏽 Why I Built This
I'm expanding my manual API testing project into basic automation using Python.  
The goal was to keep it clean, beginner-to-mid-level friendly, and reflective of the kind of real-world API validations I'd handle in a QA role — without overcomplicating things with heavy frameworks right away.

## 🛠 Tools I Used
- Python 3.x
- Requests library
- (Optional later) Pytest for organizing and scaling the tests
- VS Code for scripting
- GitHub for version control and sharing my work

## 📂 What's Inside
| 📝 Script | ✅ Focus |
|-----------|---------|
| **test_create_user.py** | Create user with valid data → expect **201 Created** |
| **test_negative_create_user.py** | Missing email → expect **422 Validation Error** |
| **test_auth_invalid_token.py** | Invalid token → expect **401 Unauthorized** |


Each script is standalone and focuses on building core automation skills first: making the API call, validating the response, and handling assertions cleanly.

## How I Approached It
- I focused on making sure every test is readable, simple, and realistic for junior-to-mid QA roles.
- I used the Requests library to keep it lightweight and easy to understand.
- Future plans include expanding this into a Pytest-driven test suite for even cleaner organization and batch running.

---
💡 Next step:  
---
> Expanding into Pytest for structured suites and CI/CD integration.

