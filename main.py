"""
📄 Project 10: Simple Password Manager (CLI)
👨‍💻 Created by: Hashir Adnan
🌐 Website: www.techthf.xyz
🗓️ Date: [Insert today’s date]

🧠 Description:
This CLI-based Python password manager allows you to save and retrieve website login credentials.
It stores data in a local JSON file for persistent storage and easy access.

📦 Features:
- Add new website credentials
- View all saved accounts
- Stores data in a JSON file (like a database)
- Easy to upgrade with encryption or GUI later

🧰 Tools & Modules Used:
- json: for saving and reading credentials
- os: for file checking and handling

💡 How to Use:
1. Run the script: `python main.py`
2. Choose an option:
   - [1] Add new password
   - [2] View saved passwords
   - [3] Exit
3. Your data will be saved in `passwords.json` file

✅ Example:
> Website: github.com  
> Username: hashir@techthf.xyz  
> Password: ********  
Saved Successfully!
"""

import json
import os

DATA_FILE = "passwords.json"

# Load existing data or create empty file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
        print("✅ Saved successfully!")

# Add new credential
def add_password():
    website = input("🔹 Website: ").strip()
    username = input("👤 Username: ").strip()
    password = input("🔑 Password: ").strip()

    data = load_data()
    data[website] = {
        "username": username,
        "password": password
    }
    save_data(data)

# View all credentials
def view_passwords():
    data = load_data()
    if not data:
        print("❌ No credentials saved yet.")
    else:
        print("\n🔐 Saved Credentials:")
        for site, creds in data.items():
            print(f"\n🌐 {site}")
            print(f"   👤 {creds['username']}")
            print(f"   🔑 {creds['password']}")
        print()

# Main Menu
def main():
    while True:
        print("\n🔐 PASSWORD MANAGER")
        print("1. Add new password")
        print("2. View saved credentials")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
