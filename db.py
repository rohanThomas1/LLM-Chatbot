import sqlite3

DB_FILE = "customers.db"

def get_db():
    return sqlite3.connect(DB_FILE)

def execute_query(query):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        logging.error(f"Invalid SQL/Execution Error: {e}")
        raise
