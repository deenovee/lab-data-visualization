import sqlite3

class Database:
    def __init__(self, db="injections.db"):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS injections (id INTEGER PRIMARY KEY AUTOINCREMENT, injector TEXT, injection_type TEXT, injected INTEGER, hatched INTEGER, percentage REAL)")
        self.conn.commit()
        self.conn.close()

    def fetch(self, injector=None):
        self.conn = sqlite3.connect("injections.db")
        self.cur = self.conn.cursor()
        if injector == None:
            self.cur.execute('SELECT * FROM injections;')
            results = self.cur.fetchall()
            self.conn.close()
            return results
        query = f"SELECT * FROM injections WHERE injector = {injector};"
        self.cur.execute(query)
        results = self.cur.fetchall()
        self.conn.close()
        # print(results)
        return results
    
    def insert(self, injector, injection_type, injected, hatched, percentage):
        self.conn = sqlite3.connect("injections.db")
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO injections (injector, injection_type, injected, hatched, percentage) VALUES (?, ?, ?, ?, ?)", (injector, injection_type, injected, hatched, percentage))
        self.conn.commit()
        self.conn.close()

