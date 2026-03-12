
# Secure Chat Application

A real-time encrypted messaging application built using Python socket programming with hybrid encryption (RSA + AES) to ensure secure communication between clients.

## Overview

This project demonstrates the implementation of a secure client-server chat system. Messages exchanged between clients are encrypted using AES for efficiency, while RSA is used for secure key exchange.

The system ensures that communication remains private and protected from unauthorized access.

---

## Features

- Secure client-server communication
- Hybrid encryption using RSA and AES
- Secure key generation for users
- Encrypted message transmission
- GUI-based chat interface
- Multiple client support

---

## Tech Stack

- Python
- Socket Programming
- RSA Encryption
- AES Encryption
- PyCryptodome Library
- Tkinter (GUI)

---

## Project Structure

```

secure-chat-application
│
├── User1
│   ├── client.py
│   ├── crypto_utils.py
│   └── gui.py
│
├── User2
│   ├── client.py
│   ├── crypto_utils.py
│   └── gui.py
│
├── generate_keys.py
├── server.py
└── .gitignore

```

---

## Installation

### 1 Install dependencies

```

pip install pycryptodome

```

### 2 Clone the repository

```

git clone [https://github.com/Aayu4473/secure-chat-application.git]
cd secure-chat-application

```

---

## Usage

### Step 1: Generate RSA keys

```

python generate_keys.py

```

### Step 2: Start the server

```

python server.py

```

### Step 3: Start the clients

Run clients in separate terminals.

```

python User1/client.py
python User2/client.py

```

---

## Security Implementation

This project uses **Hybrid Encryption**:

- **RSA** for secure key exchange
- **AES** for fast message encryption
- Each message is encrypted before transmission
- Only the intended recipient can decrypt the message

---

## Learning Outcomes

- Understanding hybrid encryption
- Implementing secure communication protocols
- Working with socket programming in Python
- Designing encrypted client-server applications

---

## Future Improvements

- Group chat functionality
- Message authentication
- Secure file sharing
- Improved GUI design
- User authentication system

---

## Author

Aayushi Tiwari  
B.Tech Computer Science Engineering 
