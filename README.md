# 🔐 Ghost Cipher V1.0
**Author:** HRD-024 (Hardik Prajapati) 😼  
**Category:** Cryptography / Privacy Tool

Ghost Cipher ek secure text encryption utility hai jo **AES-256 (Fernet)** standard ka use karti hai. Is tool ki khasiyat ye hai ki ye sirf password nahi, balki **PBKDF2HMAC** algorithm ka use karke aapke password ko 1,00,000 iterations ke saath ek military-grade key mein badal deta hai.

---

## 🛠️ Technical Specifications
- **Algorithm:** AES-256-CBC (Fernet)
- **Key Derivation:** PBKDF2 with SHA-256
- **Iterations:** 100,000 (Brute-force resistant)
- **Encoding:** Base64 URL-safe
- **Salting:** Unique static salt for consistent key derivation

---

## 🔍 Features
- **Master Password Security:** Bina master password ke data decode karna namumkin hai.
- **Interactive Menu:** Encrypt, Decrypt, aur Password Change karne ke liye easy-to-use CLI.
- **Memory Safe:** Original password ko safe rakhta hai aur sirf bytes par process karta hai.
- **Error Handling:** Galat password ya corrupted data par crash hone ki jagah alert deta hai.

---

## 🚀 Installation

1. Clone the repository:
```bash
git clone [https://github.com/yourusername/Ghost-Cipher-V1](https://github.com/yourusername/Ghost-Cipher-V1)
