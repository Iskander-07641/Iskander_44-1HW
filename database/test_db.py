import sqlite3
import os

# Убедитесь, что директория существует
db_dir = 'database'
db_path = os.path.join(db_dir, 'reviews.db')

if not os.path.exists(db_dir):
    os.makedirs(db_dir)

try:
    # Создание новой базы данных
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Создание таблицы для проверки
    cursor.execute('''
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

    # Добавление тестовых данных
    cursor.execute("INSERT INTO reviews (name, phone_number, visit_date, food_rating, cleanliness_rating, extra_comments) VALUES ('Test User', '1234567890', '2024-01-01', 5, 5, 'Great!')")
    conn.commit()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the new database:", tables)

    conn.close()

except sqlite3.DatabaseError as e:
    print(f"Ошибка базы данных: {e}")
