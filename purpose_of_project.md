<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0A66C2,100:181717&height=100&section=header"/>
</p>

# “Why did I build this?”
I wanted to understand how real-world web applications implement security mechanisms beyond basic login systems, especially focusing on authentication security and attack prevention techniques.
## ❗ Problem Statement
Many web applications are vulnerable to attacks such as:
- Weak password handling
- Brute-force login attempts
- CSRF attacks
- Unauthorized access
This project aims to address these issues using practical implementations.
## 🔐 Security Features
- Password Hashing using Bcrypt
- CSRF Protection using Flask-WTF
- Brute-force Attack Prevention
- Role-Based Access Control (RBAC)
- Security Logging System
## ⚙️ How It Works
1. User registers with a strong password
2. Password is securely hashed before storage
3. Login attempts are monitored and limited
4. CSRF tokens protect form submissions
5. Users are assigned roles (admin/user)
6. Admin routes are restricted
7. All activities are logged for monitoring
## 🧠 Learning Outcomes
- Understanding of secure authentication systems
- Implementation of CSRF protection
- Handling user roles and permissions
- Logging and monitoring suspicious activity
- Applying OWASP security practices
## 🌍 Real-World Use Case
This project can be used as a base for:
- Secure login systems
- Admin dashboards
- SaaS platforms
- Cybersecurity learning environments
## 💡 Real-life analogy
It’s like a building:
- Password = your key
- Bcrypt = key is encrypted
- Brute-force protection = security guard blocking repeated attempts
- CSRF = prevents fake entry requests
- Roles = admin has master access, users have limited access
- Logs = CCTV recording everything
## 🏗️ Architecture Overview
- Flask (Backend)
- SQLite (Database)
- Flask-Login (Authentication)
- Flask-WTF (Form Security)
- Bcrypt (Password Hashing)
# Purpose of Project
## 🎯 1. Formal (Interview Answer)
### 👉 Short Version
I developed a secure web application using Flask that implements user authentication with multiple security features such as password hashing using bcrypt, CSRF protection, brute-force attack mitigation, and role-based access control. The system also includes security logging to track login attempts and suspicious activities, aligning with secure coding practices and OWASP guidelines.
### 👉 Detailed Version 

This project is a secure authentication-based web application where users can register and log in. I implemented strong password validation and hashing using bcrypt to ensure credential security.

I added brute-force protection by limiting login attempts per IP, and CSRF protection using Flask-WTF to prevent unauthorized form submissions.

The application also includes role-based access control, where admin users can access restricted routes. Additionally, I implemented logging to track events such as failed logins and suspicious activity, which is important for security monitoring and incident response.

---

## 🧠 Keywords used in Project
- Authentication system
- Bcrypt hashing
- CSRF protection
- Role-based access control (RBAC)
- Brute-force protection
- Security logging
- Secure coding practices
- OWASP Top 10

---

## 😎 2. Layman
### 👉 Simple Version
I made a secure login system like the ones you see on websites, but with extra protection.
It checks if your password is strong, stores it safely (not in plain text), blocks too many wrong login attempts, and even keeps track of suspicious activity.
It also has admin and normal user roles, so some pages are restricted.

---
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0A66C2,100:181717&height=100&section=footer"/>
</p>
