import sqlite3
from datetime import date

def init_db ():
    conn = sqlite3.connect ("expenses.db")
    cursor = conn.cursor()
    cursor.execute ("""
    CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Amount REAL,
    category TEXT,
    description TEXT,
    notes TEXT,
    date TEXT
    )
    """)
    conn.commit()
    conn.close()
init_db

    