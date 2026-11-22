import os
import sqlite3
from getpass import getpass
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "secureverify.db")

usn = input("USN: ").strip().upper()
name = input("Name: ").strip()
dob = input("Date of birth (YYYY-MM-DD): ").strip()
email = input("Email: ").strip()
phone = input("Phone: ").strip()
course = input("Course: ").strip()
branch = input("Branch: ").strip()
year = input("Year: ").strip()
password = getpass("Password: ")

conn = sqlite3.connect(DB_PATH)
try:
    exists = conn.execute(
        "SELECT 1 FROM students WHERE usn = ?",
        (usn,),
    ).fetchone()

    if exists:
        print(f"USN {usn} already exists; no student was added.")
    else:
        conn.execute(
            """
            INSERT INTO students
                (usn, name, dob, email, phone, course, branch, year, password_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                usn, name, dob, email, phone, course, branch, year,
                generate_password_hash(password),
            ),
        )
        conn.commit()
        print(f"Student {usn} added.")
finally:
    conn.close()
