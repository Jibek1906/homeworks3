import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                 CREATE TABLE IF NOT EXISTS reviews (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT,
                     phone_number TEXT,
                     food_rating INTEGER,
                     cleanliness_rating INTEGER,
                     extra_comments TEXT,
                     date DATE 
                     )
            """)
            conn.execute("""
                 CREATE TABLE IF NOT EXISTS dishes (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT,
                     price FLOAT,
                     description TEXT,
                     category TEXT,
                     kitchen_type TEXT,
                     weight_unit TEXT,
                     weight INTEGER
                     )
            """)
            conn.commit()

    def save_reviews(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                 INSERT INTO reviews(name, phone_number, food_rating, cleanliness_rating, extra_comments, date)
                 VALUES (?, ?, ?, ?, ?, ?)
            """,
            (data["name"], data["phone_number"], data["food_rating"], data["cleanliness_rating"], data["extra_comments"], data["date"] )
            )
            conn.commit()

    def save_dishes(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
            INSERT INTO dishes(name, price, description, category, kitchen_type, weight_unit, weight)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (data["name"], data["price"], data["description"], data["category"], data["kitchen_type"], data["weight_unit"], data["weight"])
            )
            conn.commit()

    def get_dishes(self):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute(
                "SELECT * FROM dishes"
            )
            return result.fetchall()