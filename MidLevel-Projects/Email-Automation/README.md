### Title: Email Automation

---

### Short Description
- Automate sending emails with optional attachments and HTML formatting using Python.
- This Project allows you to securely send emails to multiple recipients and supports email sending in a single session.

---

### Features
- Send emails via SMTP (Gmail SMTP used by default)
- Support for multiple recipients (comma-separated)
- Option to send messages as plain text or HTML
- Attach files to your emails
- ANSI-styled console output for better readability
- Loop to send multiple emails without restarting the program
- Securely input your email password using `getpass`

---

### Requirements
- Python 3
- Standard Python libraries: `smtplib`, `email`, `os`, `mimetypes`, `getpass`
- Internet connection for SMTP access
- A Gmail account with "Less secure app access" enabled (or use App Passwords for 2FA accounts)
- How to Run:
  ```bash
  python email_automation.py

---

### License
- This project is licensed under the MIT License