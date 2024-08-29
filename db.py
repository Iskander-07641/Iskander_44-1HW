import sqlite3
import os


class Database:
    def __init__(self, db_name='reviews.db'):
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_name)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Создаем таблицу для отзывов
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

        # Создаем таблицу для предупреждений
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS warnings (
                user_id INTEGER PRIMARY KEY,
                warning_count INTEGER
            )
        ''')
        self.connection.commit()

    def add_review(self, name, phone_number, visit_date, food_rating, cleanliness_rating, extra_comments):
        self.cursor.execute('''
            INSERT INTO reviews (name, phone_number, instagram_username, visit_date, food_rating, cleanliness_rating, extra_comments)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, phone_number, None, visit_date, food_rating, cleanliness_rating, extra_comments))
        self.connection.commit()

    def insert_category(self, category_name):
        self.cursor.execute('''
            INSERT INTO categories (name) VALUES (?)
        ''', (category_name,))
        self.connection.commit()

    def insert_dish(self, dish_name, category_id):
        self.cursor.execute('''
            INSERT INTO dishes (name, category_id) VALUES (?, ?)
        ''', (dish_name, category_id))
        self.connection.commit()

    def get_dishes_by_category(self, category_id):
        self.cursor.execute('''
            SELECT name FROM dishes WHERE category_id = ?
        ''', (category_id,))
        return self.cursor.fetchall()

    def add_warning(self, user_id):
        self.cursor.execute('''
            INSERT INTO warnings (user_id, warning_count) VALUES (?, 1)
            ON CONFLICT(user_id) DO UPDATE SET warning_count = warning_count + 1
        ''', (user_id,))
        self.connection.commit()

    def get_warnings(self, user_id):
        self.cursor.execute('SELECT warning_count FROM warnings WHERE user_id = ?', (user_id,))
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def clear_warnings(self, user_id):
        self.cursor.execute('DELETE FROM warnings WHERE user_id = ?', (user_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()
