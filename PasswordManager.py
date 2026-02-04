import json
import os
import base64
from cryptography.fernet import Fernet, InvalidToken
from getpass import getpass
import hashlib

VAULT_FILE = "vault.dat"


# Convert master password into encryption key
def derive_key(password):
    hash_value = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hash_value)


# Load encrypted vault
def load_vault(key):
    if not os.path.exists(VAULT_FILE):
        return {}

    with open(VAULT_FILE, "rb") as f:
        encrypted = f.read()

    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted)
    return json.loads(decrypted.decode())


# Save encrypted vault
def save_vault(data, key):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(json.dumps(data).encode())

    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)


# Add entry
def add_entry(vault):
    site = input("Site name: ")
    username = input("Username: ")
    password = getpass("Password: ")

    vault[site] = {"username": username, "password": password}
    print("✔ Entry saved")


# View entries
def view_entries(vault):
    if not vault:
        print("Vault is empty.")
        return

    for site, creds in vault.items():
        print(f"\nSite: {site}")
        print(f"Username: {creds['username']}")
        print(f"Password: {creds['password']}")


# Search entry
def search_entry(vault):
    site = input("Search site: ")
    if site in vault:
        creds = vault[site]
        print(f"\nSite: {site}")
        print(f"Username: {creds['username']}")
        print(f"Password: {creds['password']}")
    else:
        print("Entry not found")


# Delete entry
def delete_entry(vault):
    site = input("Site to delete: ")
    if site in vault:
        del vault[site]
        print("✔ Entry deleted")
    else:
        print("Entry not found")


# Main program
def main():
    master = getpass("Enter master password: ")
    key = derive_key(master)

    try:
        vault = load_vault(key)
    except InvalidToken:
        print("Wrong password or corrupted vault!")
        return

    while True:
        print("\n1. Add entry")
        print("2. View entries")
        print("3. Search entry")
        print("4. Delete entry")
        print("5. Save & Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_entry(vault)
        elif choice == "2":
            view_entries(vault)
        elif choice == "3":
            search_entry(vault)
        elif choice == "4":
            delete_entry(vault)
        elif choice == "5":
            save_vault(vault, key)
            print("Vault saved securely.")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
