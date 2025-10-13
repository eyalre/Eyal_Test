# consume_env_secret.py
import os
import sys

def main():
    username = os.environ.get("APP_USER")
    password = os.environ.get("APP_PASS")

    if not username or not password:
        print("Missing APP_USER or APP_PASS environment variables.", file=sys.stderr)
        sys.exit(1)

    # --- Example use (replace with your actual logic) ---
    # e.g., connect_to_database(username, password)
    print(f"Successfully loaded credentials for {username}.")
    print("Performing secure operation...")

    # Avoid leaving password in memory longer than needed
    password = None

if __name__ == "__main__":
    main()
