# 🏦 Banking Simulator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

A desktop-based banking application built using Python that simulates core banking operations with secure authentication and real-time features.

---

## 📌 Overview

A desktop-based Banking Simulator that replicates real-world banking operations with secure authentication and role-based access control. The application ensures smooth financial transactions along with enhanced security features like Captcha and OTP verification.

---

## ✨ Features

### 🔐 Authentication
- Role-based login system (Admin & Customer)
- Captcha verification for secure access

### 💳 Banking Operations
- Deposit funds
- Withdraw money
- Transfer funds between accounts

### 👨‍💼 Account Management
- Admin can create, view, and close accounts
- Customers can update personal details

### 📧 Email Integration
- OTP verification for password recovery
- Secure account closure via email

---

## 📸 Screenshots

### 🔐 Login Screen
![Login](screenshots/login.png)

### 👨‍💼 Admin Panel
![Admin](screenshots/admin.png)

### 👤 Customer Dashboard
![Dashboard](screenshots/dashboard.png)

### ✏️ Edit Details
![Edit](screenshots/edit.png)

### 💸 Transactions
![Transaction](screenshots/transaction.png)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core Programming |
| 🖥️ Tkinter | GUI Development |
| 🗄️ SQLite | Database |
| 📬 Gmail API | Email & OTP System |

---

## ⚙️ Installation

```bash
pip install gmail
```

---

## ▶️ Usage

```bash
python main.py
```

---

## 📁 Project Structure

```
Banking-Simulator/
│
├── main.py        # Main application logic
├── tables.py      # Database setup
├── generator.py   # Captcha & OTP generation
├── mailing.py     # Email functionality
└── README.md      # Documentation
```

---

## 🔒 Security Features

- Captcha-based login protection
- OTP verification via email
- Role-based access control

---

## 🚧 Future Enhancements

- Transaction history tracking
- Data visualization (charts/graphs)
- Web-based version (Flask/Django)

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## 📄 License

This project is for educational purposes. You may modify and use it as needed.

---

## 👩‍💻 Author

**Mansi Nishad**
🔗 [GitHub](https://github.com/Mansi-Nishad)

> ⭐ If you found this project helpful, consider giving it a star!
