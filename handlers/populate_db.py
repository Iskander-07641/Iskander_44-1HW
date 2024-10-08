# -*- coding: utf-8 -*-
from db import Database


def populate_database():
    db = Database()

    db.insert_category('Салаты')
    db.insert_category('Основные блюда')
    db.insert_category('Десерты')

    db.insert_dish('Цезарь', 'Салаты')
    db.insert_dish('Стейк', 'Основные блюда')
    db.insert_dish('Тирамису', 'Десерты')

    dishes = db.get_dishes_by_category('Салаты')
    print(f"Блюда в категории 'Салаты': {dishes}")

    db.close()


if __name__ == '__main__':
    populate_database()
