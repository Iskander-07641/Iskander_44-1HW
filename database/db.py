# database/db.py
import os
import sqlite3

class Database:
    def __init__(self, db_path):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                visit_date TEXT NOT NULL,
                food_rating INTEGER NOT NULL,
                cleanliness_rating INTEGER NOT NULL,
                extra_comments TEXT
            )
        ''')
        self.connection.commit()
        print("Table created or already exists")  # Отладочное сообщение

    def add_review(self, name, phone_number, visit_date, food_rating, cleanliness_rating, extra_comments):
        self.cursor.execute('''
            INSERT INTO reviews (name, phone_number, visit_date, food_rating, cleanliness_rating, extra_comments)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, phone_number, visit_date, food_rating, cleanliness_rating, extra_comments))
        self.connection.commit()
        print("Review added")  # Отладочное сообщение

    def close(self):
        self.connection.close()
