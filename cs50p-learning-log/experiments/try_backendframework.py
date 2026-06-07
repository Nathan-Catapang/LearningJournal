import csv
import json
import os
import sys

DB_FILE = "users_db.csv"

def main():
    # Verify command line arguments are present
    if len(sys.argv) < 2:
        sys.exit("Usage: python db_engine.py [init | add | export]")
    
    command = sys.argv[1].strip().lower()

    # Route commands based on argument strings
    if command == "init":
        initialize_database()
    elif command == "add":
        add_user_flow()
    elif command == "export":
        export_to_json()
    else:
        sys.exit(f"Error: Unknown command '{command}'. Use init, add, or export.")

def initialize_database():
    if os.path.exists(DB_FILE):
        print(f"Database '{DB_FILE}' already exists.")
        return
        
    try:
        with open(DB_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "username", "email", "role"])
        print(f"Success: Initialized database system at '{DB_FILE}'.")
    except IOError as e:
        sys.exit(f"System Error: Could not write file. Details: {e}")

def add_user_flow():
    if not os.path.exists(DB_FILE):
        sys.exit("Error: Database not initialized. Run 'python db_engine.py init' first.")

    print("\n--- Add New System User ---")
    
    # 1. ID Check (Using standard .isdigit string verification)
    while True:
        user_id = input("Enter Numeric ID: ").strip()
        if user_id.isdigit():
            break
        print("Validation Error: ID must contain numbers only.")

    # 2. Username Check (Using standard string methods and indexing)
    while True:
        username = input("Enter Username: ").strip().lower()
        if len(username) >= 3 and len(username) <= 15 and username.isalnum() and username[0].isalpha():
            break
        print("Validation Error: 3-15 chars, alphanumeric, must start with a letter.")

    # 3. Email Check (Using standard split and containment syntax)
    while True:
        email = input("Enter Email Address: ").strip()
        if "@" in email and "." in email:
            # Simple check to ensure characters exist around the symbols
            parts = email.split("@")
            if len(parts) == 2 and parts[0] != "" and parts[1] != "":
                break
        print("Validation Error: Invalid basic email structure.")

    # 4. Role Check
    role = input("Enter Role (admin/user): ").strip().lower()
    if role not in ["admin", "user"]:
        role = "user" 

    try:
        with open(DB_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([user_id, username, email, role])
        print(f"Success: User '{username}' safely written to storage.")
    except IOError:
        sys.exit("Critical Error: Database file is locked.")

def export_to_json():
    if not os.path.exists(DB_FILE):
        sys.exit("Error: No data found to export.")

    records = []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                records.append(row)
        
        print("\n--- Exported JSON Payload ---")
        print(json.dumps(records, indent=4))
        
    except FileNotFoundError:
        sys.exit("Error: Target database file vanished.")

if __name__ == "__main__":
    main()
