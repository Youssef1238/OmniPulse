import sqlite3


class Database:
    def __init__(self):

        self.path = "omnipulse.db"
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS targets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE,
                name TEXT UNIQUE,
                last_seen TEXT UNIQUE,
                title TEXT,
                selectors TEXT
            );
        """)
        connection.commit()
        cursor.close()
        

    def create_target(self,url,name,last_seen,title,selectors):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO targets(url,name,last_seen,title,selectors) VALUES(?,?,?,?,?)",(url,name,last_seen,title,selectors))
            connection.commit()
        
    def update_target(self,id,selectors):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE targets SET selectors = ? WHERE id = ?",(selectors,id))
            connection.commit()
    
    def update_state(self,id,last_seen,title):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE targets SET last_seen = ? title = ? WHERE id = ?",(last_seen,title,id))
            connection.commit()
    
    def find_target_by_name(self,name) -> dict | None:
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            res = cursor.execute("SELECT * FROM targets WHERE name = ?",(name,)).fetchone()
            return None if res is None else {"id": res[0], "url": res[1], "name": res[2], "selectors": res[3]}
    
    def find_target_by_url(self,url) -> dict | None:
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            res = cursor.execute("SELECT * FROM targets WHERE url = ?",(url,)).fetchone()
            return None if res is None else {"id": res[0], "url": res[1], "name": res[2], "selectors": res[3]}
    
    def findall(self):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            res = cursor.execute("SELECT * FROM targets").fetchall()
            return None if res is None else [{"id": r[0], "url": r[1], "name": r[2], "last_seen": r[3], "title": r[4], "selectors": r[5]} for r in res]