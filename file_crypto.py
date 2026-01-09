from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)

    with open(filename, "wb") as file:
        file.write(encrypted)

def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    decrypted = f.decrypt(data)

    with open(filename, "wb") as file:
        file.write(decrypted)

if __name__ == "__main__":
    if not os.path.exists("secret.key"):
        generate_key()

    choice = input("Encrypt or Decrypt (E/D): ").upper()
    file_name = input("File name: ")

    if choice == "E":
        encrypt_file(file_name)
        print("File encrypted successfully.")
    elif choice == "D":
        decrypt_file(file_name)
        print("File decrypted successfully.")
