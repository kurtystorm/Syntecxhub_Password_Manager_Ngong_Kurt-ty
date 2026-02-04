
# Syntecxhub Password Manager

A secure local password manager built in Python as part of the Syntecxhub Internship Program.

This project implements encrypted credential storage using AES-based symmetric encryption and a master password system. It demonstrates secure key handling, encryption, JSON storage, and command-line interface design.

---

## Extended Description

The Syntecxhub Password Manager is a lightweight offline credential manager designed to securely store sensitive login information. All data is encrypted before being written to disk using industry-standard symmetric encryption (Fernet/AES).

The application requires a master password to unlock the vault. Without the correct password, stored credentials cannot be decrypted. This ensures that even if the storage file is stolen, the information remains protected.

The vault is stored as encrypted JSON, allowing structured and portable data storage while maintaining confidentiality. The project focuses on practical cybersecurity principles such as encryption, hashing, secure authentication, and safe data persistence.

This project was built to simulate how real password managers operate while reinforcing secure software development practices.

---

## Features

- Master password authentication
- AES-based encryption using Fernet
- Encrypted local vault storage
- Add password entries
- View stored credentials
- Search entries
- Delete entries
- Secure JSON storage format
- Hidden password input in terminal
- Exception handling for wrong password

---

## Requirements

- Python 3.8+
- cryptography library

Install dependency:

```bash
pip install cryptography
```

or

```bash
pip install -r requirements.txt
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/kurtystorm/Syntecxhub_PasswordManager.git
cd Syntecxhub_PasswordManager
```

Run the program:

```bash
python password_manager.py
```

---

## Project Structure

```
Syntecxhub_PasswordManager/
│
├── password_manager.py
├── vault.dat
├── requirements.txt
└── README.md
```

---

## Security Model

- Master password is never stored
- Encryption key derived using SHA-256 hashing
- Vault stored only in encrypted format
- Fernet encryption ensures confidentiality and integrity
- No plaintext credentials written to disk

---

## Disclaimer

This tool is for educational purposes only.

It is designed to demonstrate encryption and secure storage concepts in a controlled environment.

---

## Author

Ngong Kwa Wolfgang Kurt-Ty  
Cybersecurity & Network Administration  
Syntecxhub Internship Project

