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


class ChartDatabase:
    def __init__(self, db_name='chart.db'):
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), db_name)
        db_path = os.path.abspath(db_path)

        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dish_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dishes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES dish_categories (id)
            )
        ''')

        self.connection.commit()

    def insert_category(self, category_name):
        self.cursor.execute('''
            INSERT OR IGNORE INTO dish_categories (name) VALUES (?)
        ''', (category_name,))
        self.connection.commit()

    def insert_dish(self, dish_name, category_name):
        self.cursor.execute('''
            INSERT OR IGNORE INTO dishes (name, category_id) 
            VALUES (?, (SELECT id FROM dish_categories WHERE name = ?))
        ''', (dish_name, category_name))
        self.connection.commit()

    def get_dishes_by_category(self, category_name):
        self.cursor.execute('''
            SELECT name FROM dishes
            WHERE category_id = (SELECT id FROM dish_categories WHERE name = ?)
        ''', (category_name,))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
