import sqlite3
import datetime

DB_NAME = "memory_store.db"


def init_memory():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        user_input TEXT,
        aura_response TEXT
    )
    """)

    conn.commit()
    conn.close()


def store_memory(user_input, aura_response):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    timestamp = datetime.datetime.utcnow().isoformat()

    cursor.execute("""
    INSERT INTO memory (timestamp, user_input, aura_response)
    VALUES (?, ?, ?)
    """, (timestamp, user_input, aura_response))

    conn.commit()
    conn.close()


def get_recent_memories(limit=5):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT timestamp, user_input, aura_response
    FROM memory
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return rows