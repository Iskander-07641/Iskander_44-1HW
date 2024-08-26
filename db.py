import sqlite3
import os


class Database:
    def __init__(self, db_name='reviews.db'):
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), db_name)
        db_path = os.path.abspath(db_path)

        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone_number TEXT,
                instagram_username TEXT,
                visit_date TEXT,
                food_rating INTEGER,
                cleanliness_rating INTEGER,
                extra_comments TEXT
            )
        ''')
        self.connection.commit()

    def close(self):
        self.connection.close()

    def add_review(self, name: object, phone_number: object, visit_date: object,
                   food_rating: object, cleanliness_rating: object, extra_comments: object) -> object:
        pass

    def insert_category(self, param):
        pass

    def insert_dish(self, param, param1):
        pass

    def get_dishes_by_category(self, param):
        pass
