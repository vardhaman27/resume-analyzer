
import sqlite3

def init_db():
    conn = sqlite3.connect("reports.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            score INTEGER,
            matched TEXT,
            missing TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_report(filename, score, matched, missing):
    conn = sqlite3.connect("reports.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reports (filename, score, matched, missing) VALUES (?, ?, ?, ?)",
        (filename, score, ",".join(matched), ",".join(missing))
    )
    conn.commit()
    conn.close()

def get_all_reports():
    conn = sqlite3.connect("reports.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows