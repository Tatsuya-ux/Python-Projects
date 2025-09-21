import json
import os
import base64
from cryptography.fernet import Fernet
import secrets
import string

# ANSI Styles
class Styles:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# File paths
DATA_FILE = 'passwords.json'
KEY_FILE = "secret.key"

# Load or generate encryption key
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, 'rb') as key_file:
            key = key_file.read()
    return Fernet(key)

# Load existing passwords
def load_passwords():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save passwords to file
def save_passwords(passwords):
    with open(DATA_FILE, 'w') as file:
        json.dump(passwords, file)

# Add a new password
def add_password(fernet, passwords):
    site = input("Enter account/site name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    encrypted_password = fernet.encrypt(password.encode()).decode()
    passwords[site] = {'username': username, 'password': encrypted_password}
    save_passwords(passwords)
    print(f"{Styles.GREEN}Password added and encrypted successfully!{Styles.RESET}")

# Retrieve a password
def retrieve_password(fernet, passwords):
    site = input("Enter account/site name to retrieve: ")
    if site in passwords:
        username = passwords[site]['username']
        encrypted = passwords[site]['password']
        decrypted = fernet.decrypt(encrypted.encode()).decode()
        print(f"{Styles.CYAN}Username: {username}\nPassword: {decrypted}{Styles.RESET}")
    else:
        print(f"{Styles.RED}No entry found for '{site}'.{Styles.RESET}")

# Generate a strong password
def generate_password():
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length < 1:
                print(f"{Styles.RED}Password length must be a positive integer.{Styles.RESET}")
                continue
            break
        except ValueError:
            print(f"{Styles.RED}Please enter a valid number.{Styles.RESET}")

    while True:
        complexity = input("Include special characters? (y/n): ").lower()
        if complexity in ['y', 'n']:
            break
        else:
            print(f"{Styles.RED}Please enter 'y' or 'n'.{Styles.RESET}")

    characters = string.ascii_letters + string.digits

    if complexity == 'y':
        characters += string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    print(f"{Styles.YELLOW}Generated Password: {password}{Styles.RESET}")

    store = input("Store this password? (y/n): ").lower()
    if store == 'y':
        site = input("Enter account/site name: ")
        username = input("Enter username: ")
        encrypted = fernet.encrypt(password.encode()).decode()
        passwords[site] = {'username': username, 'password': encrypted}
        save_passwords(passwords)
        print(f"{Styles.GREEN}Password stored successfully!{Styles.RESET}")

# Main Loop
def main():
    print(f"{Styles.BOLD}Welcome to the Password Manager!{Styles.RESET}")
    global fernet
    global passwords
    fernet = load_key()
    passwords = load_passwords()

    while True:
        print(f"""\n{Styles.BOLD}Menu:{Styles.RESET}
              [1] Add Password
              [2] Retrieve Password
              [3] Generate Password
              [4] Exit""")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_password(fernet, passwords)
        elif choice == '2':
            retrieve_password(fernet, passwords)
        elif choice == '3':
            generate_password()
        elif choice == '4':
            save_passwords(passwords)
            print(f"{Styles.BOLD}Goodbye! Changes saved.{Styles.RESET}")
            break
        else:
            print(f"{Styles.RED}Invalid choice. Please try again.{Styles.RESET}")

if __name__ == "__main__":
    main()