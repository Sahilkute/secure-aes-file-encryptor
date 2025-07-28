# 🔐 Secure AES File Encryptor (Flask Web App)

A simple and secure file encryption and decryption web application built with **Flask** and **AES (Advanced Encryption Standard)**. This app allows users to upload any file, encrypt it securely, and download the encrypted version — and vice versa.

---

## 🚀 Features

- 🔒 AES-128 encryption for strong data protection
- 🧾 Simple web interface to upload, encrypt, and decrypt files
- 🧠 Built using Flask and Python’s cryptography library
- 💾 Works locally in your browser
- 💡 Easy to customize and expand

---

## 📸 Screenshot



---

## 🛠 Tech Stack

- Python 3
- Flask
- Cryptography (AES, CBC mode)
- HTML/CSS (for the frontend UI)

---

## 📁 Folder Structure

secure-aes-file-encryptor/
│
├── app.py # Main Flask app
├── app_utils.py # AES encryption/decryption logic
├── requirements.txt
│
├── templates/
│ └── index.html # User interface (UI)
├── static/
│ └── (optional CSS/images)


## ▶️ How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/Sahilkute/secure-aes-file-encryptor.git
   cd secure-aes-file-encryptor
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
python app.py
Open your browser

arduino
Copy
Edit
http://localhost:5000
