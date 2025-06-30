from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("✅ Key saved to secret.key")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)
    print(f"🔐 Encrypted: {filename} → {filename}.enc")

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted = file.read()
    decrypted = f.decrypt(encrypted)
    with open("decrypted_" + filename.replace(".enc", ""), "wb") as file:
        file.write(decrypted)
    print(f"🔓 Decrypted: {filename} → decrypted_{filename.replace('.enc', '')}")

def main():
    print("=== Advanced Encryption Tool ===")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        key = load_key()
        filename = input("Enter the file name to encrypt: ")
        encrypt_file(filename, key)
    elif choice == "3":
        key = load_key()
        filename = input("Enter the file name to decrypt: ")
        decrypt_file(filename, key)
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()