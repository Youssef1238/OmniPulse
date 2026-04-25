import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("omnipulse.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS targets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE,
                name TEXT UNIQUE,
                selectors TEXT
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS states (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_id INTEGER UNIQUE,
                last_seen TEXT UNIQUE,
                title TEXT,
                FOREIGN KEY (target_id) REFERENCES targets(id)
            );
        """)
        self.connection.commit()
        

