# 📅 Weekly Trend Reports
*MedAccess Claims Portal – Simulated Project*

---

## 📅 Week 1 Report (March 3–7, 2025)

- **Total defects logged:** 5
- **Modules impacted:** Login, Registration
- **Key issues:**
  - Multiple login failures post-security update (High severity)
  - Registration field validation error allowing letters in phone numbers (Medium severity)
  - Poorly worded error message during registration (Low severity)
- **Risk focus:**
  - Login reliability impacted user access, posing a significant risk to portal usability.
- **Recommendation:**
  - Prioritize hotfix for login failures.
  - Tighten field validation rules in the registration workflow.

---

## 📅 Week 2 Report (March 10–14, 2025)

- **Total defects logged:** 3
- **Modules impacted:** Claims Module, Dashboard
- **Key issues:**
  - App crash during claim submission (Critical severity)
  - Broken links found on the dashboard page (Low severity)
- **Risk focus:**
  - Claims submission is a core functionality — crashes could delay reimbursements and affect user trust.
- **Recommendation:**
  - Immediate crash debugging for claims workflows.
  - Conduct a full audit of dashboard links for validity.

---

## 📅 Week 3 Report (March 17–21, 2025)

- **Total defects logged:** 3
- **Modules impacted:** User Profile, Login
- **Key issues:**
  - Profile changes not saving correctly (High severity)
  - Profile picture upload hanging indefinitely (Medium severity)
  - Premature session timeouts during inactive periods (Medium severity)
- **Risk focus:**
  - Data integrity issues in user profile updates could result in support tickets and user dissatisfaction.
- **Recommendation:**
  - Implement autosave on profile forms.
  - Adjust session timeout settings for more user-friendly durations.

---

## 📅 Week 4 Report (March 24–28, 2025)

- **Total defects logged:** 1
- **Modules impacted:** Login, Claims Module
- **Key issues:**
  - Multi-factor authentication failure (Critical severity)
  - Slow processing time during claims submission (Medium severity)
- **Risk focus:**
  - MFA failures present a serious security risk for member accounts.
- **Recommendation:**
  - Urgent remediation of MFA login issues.
  - Optimize backend processing for faster claim submissions.

---
