### Title: Password Manager

---

### Short Description
- A Python-based **CLI Password Manager**, to **store, retrieve, and generate strong passwords securely**.
- Includes **ANSI-styled terminal output** for an interactive user experience.

---

### Features
- **Add Passwords** for different accounts/sites
- **Retrieve Passwords** securely
- **Generate Strong Passwords** with optional special characters
- **Encrypted storage** using `cryptography.Fernet`
- ANSI-styled output for prompts, success, and error messages
- Automatically saves passwords to a local JSON file

---

### Requirements
- Python 3
- [`cryptography`](https://pypi.org/project/cryptography/) library
- Install dependencies:
  ```bash
  pip install cryptography
- How to Run:
  ```bash
  python password_manager.py

---

### License
- This project is licensed under the MIT License.