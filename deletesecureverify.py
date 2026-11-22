import os
import sqlite3

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "secureverify.db")
usn = input("Enter the USN to delete: ").strip().upper()

if not os.path.exists(db_path):
    raise FileNotFoundError(f"Database not found: {db_path}")

with sqlite3.connect(db_path) as conn:
    conn.execute("PRAGMA foreign_keys = ON")

    student = conn.execute(
        "SELECT id, name FROM students WHERE usn = ?",
        (usn,),
    ).fetchone()

    if student is None:
        print(f"No student found with USN {usn}.")
    else:
        print(f"Found: {student[1]} ({usn})")
        confirm = input(f"Type the USN {usn} to confirm: ").strip().upper()

        if confirm == usn:
            conn.execute("DELETE FROM students WHERE usn = ?", (usn,))
            print("Student and related records deleted.")
        else:
            print("Cancelled; nothing was deleted.")
