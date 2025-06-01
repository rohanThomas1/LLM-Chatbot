import sqlite3

def seed():
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        gender TEXT,
        location TEXT
    )""")

    cursor.executemany("INSERT INTO customers (name, gender, location) VALUES (?, ?, ?)", [
        ("Alice", "Female", "Mumbai"),
        ("Bob", "Male", "Delhi"),
        ("Carol", "Female", "Mumbai"),
        ("Dave", "Male", "Chennai"),
        ("Eve", "Female", "Bangalore"),
    ])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()
