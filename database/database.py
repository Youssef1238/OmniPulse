import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("omnipulse.db")
        cursor = self.connection.cursor()
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
        self.connection.commit()
        cursor.close()
        
    def commit(self):
        self.connection.commit()

    def create_target(self,url,name,last_seen,title,selectors):
        print(title)
        print(selectors)
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO targets(url,name,last_seen,title,selectors) VALUES(?,?,?,?,?)",(url,name,last_seen,title,selectors))
        cursor.close()
        self.commit()
    
    def update_target(self,id,selectors):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE targets SET selectors = ? WHERE id = ?",(selectors,id))
        cursor.close()
        self.commit()
    
    def update_state(self,id,last_seen,title):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE targets SET last_seen = ? title = ? WHERE id = ?",(last_seen,title,id))
        cursor.close()
        self.commit()
    
    def find_target_by_name(self,name) -> dict | None:
        cursor = self.connection.cursor()
        res = cursor.execute("SELECT * FROM targets WHERE name = ?",(name,)).fetchone()

        return None if res is None else {"id": res[0], "url": res[1], "name": res[2], "selectors": res[3]}
    
    def find_target_by_url(self,url) -> dict | None:
        cursor = self.connection.cursor()
        res = cursor.execute("SELECT * FROM targets WHERE url = ?",(url,)).fetchone()

        return None if res is None else {"id": res[0], "url": res[1], "name": res[2], "selectors": res[3]}
    
