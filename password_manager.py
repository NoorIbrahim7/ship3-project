"""Simple password manager (basic implementation for Ship 3)."""

import json
import hashlib
from pathlib import Path


DATA_DIR = Path("data")
USER_FILE = DATA_DIR / "user_data.json"
PASSWORD_FILE = DATA_DIR / "passwords.json"


def register_user(username: str, master_password: str) -> None:
    """Register a new user by hashing and saving their master password."""
    hashed_pw = hashlib.sha256(master_password.encode()).hexdigest()

    # Load existing users or create new dict
    if USER_FILE.exists():
        with open(USER_FILE, "r") as f:
            users = json.load(f)
    else:
        users = {}

    # Add / update user
    users[username] = hashed_pw

    # Save updated data
    DATA_DIR.mkdir(exist_ok=True)
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=2)

    print(f"User '{username}' registered successfully.")


def add_password(site: str, username: str, password: str) -> None:
    """Add a password entry and save it to passwords.json."""
    entry = {"site": site, "username": username, "password": password}

    # Load existing passwords or start fresh list
    if PASSWORD_FILE.exists():
        with open(PASSWORD_FILE, "r") as f:
            entries = json.load(f)
    else:
        entries = []

    entries.append(entry)

    # Save
    DATA_DIR.mkdir(exist_ok=True)
    with open(PASSWORD_FILE, "w") as f:
        json.dump(entries, f, indent=2)

    print(f"Password for '{site}' added.")


def get_passwords() -> list[dict]:
    """Return all stored password entries."""
    if not PASSWORD_FILE.exists():
        return []
    with open(PASSWORD_FILE, "r") as f:
        return json.load(f)


def main() -> None:
    """Temporary entry point for manual testing."""
    print("Welcome to the Password Manager!")
    # Quick test block — comment out when done
    # register_user("testuser", "mypass123")
    # add_password("example.com", "testuser", "1234")
    # print(get_passwords())


if __name__ == "__main__":
    main()
