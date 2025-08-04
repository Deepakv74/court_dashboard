import sqlite3
from datetime import datetime

DB_NAME = "court_queries.db"

def save_query(case_type, case_number, filing_year, raw_html):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            query_time TEXT,
            raw_html TEXT
        )
    """)
    cur.execute("INSERT INTO queries (case_type, case_number, filing_year, query_time, raw_html) VALUES (?, ?, ?, ?, ?)",
                (case_type, case_number, filing_year, datetime.now().isoformat(), raw_html))
    conn.commit()
    conn.close()