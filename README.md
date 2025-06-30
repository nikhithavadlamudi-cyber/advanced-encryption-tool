🔐 Advanced Encryption Tool

A simple Python command‑line utility for AES‑256 file encryption and decryption using the cryptography library (Fernet).


---

✨ Features

Generate a 32‑byte symmetric key (stored in secret.key).

Encrypt any file → creates <filename>.enc.

Decrypt an .enc file → restores the original as decrypted_<filename>.

Lightweight, beginner‑friendly code (≈ 50 LOC).



---

📋 Requirements

Package	Version	Install Command

Python	3.7+	—
cryptography	latest	pip install cryptography



---

🚀 Quick Start

# clone the repo (or download ZIP)
cd advanced-encryption-tool

# install dependency
pip install cryptography

# run the tool
python encryption_tool.py

Menu

=== Advanced Encryption Tool ===
1. Generate Key
2. Encrypt File
3. Decrypt File
4. Exit


---

🔑 Key Generation

Select 1 to create secret.key. Keep this file safe— anyone with the key can decrypt your data.


---

🛡️ Encrypt a File

# choose option 2 in the menu
Enter the file name to encrypt: message.txt

Produces message.txt.enc.


---

🔓 Decrypt a File

# choose option 3 in the menu
Enter the file name to decrypt: message.txt.enc

Creates decrypted_message.txt.


---

📁 Project Structure

advanced-encryption-tool/
├── encryption_tool.py   # main script
├── secret.key           # generated after first run
├── message.txt          # sample file (user‑added)
└── README.md            # this file


---

⚠️ Disclaimer

This tool is for educational purposes only. Do not use it to encrypt or decrypt files you do not own or have permission to modify.


---

📜 License

MIT


---

👤 Author

Nikhitha Vadlamudi – Cybersecurity Intern

Feel free to open issues or pull requests to improve the tool!
