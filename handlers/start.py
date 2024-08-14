# handlers/start.py

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import re
from database.db import Database

start_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@start_router.message(Command("start"))
async def send_welcome(message: types.Message):
    buttons = [
        [types.InlineKeyboardButton(text="Инстаграм профиль", url="https://instagram.com/geeks.kg"),
         types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")],
        [types.InlineKeyboardButton(text="Наш адрес", callback_data="address"),
         types.InlineKeyboardButton(text="Контакты", callback_data="contacts")],
        [types.InlineKeyboardButton(text="Оставить отзыв", callback_data="feedback"),
         types.InlineKeyboardButton(text="О нас", callback_data="about_us")],
        [types.InlineKeyboardButton(text="Наши вакансии", callback_data="vacancies")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer("Привет! Какую информацию вы хотите получить?", reply_markup=keyboard)


@start_router.callback_query(F.data == "about_us")
async def about_us(call: types.CallbackQuery):
    await call.answer("ничего🤷")


@start_router.callback_query(F.data == "vacancies")
async def vacancies(call: types.CallbackQuery):
    await call.answer("ничего🤷")


@start_router.callback_query(F.data == "feedback")
async def feedback(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await call.message.answer("Как вас зовут?")


@start_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RestourantReview.phone_number)
    await message.answer("Ваш номер телефона или инстаграм?")


@start_router.message(RestourantReview.phone_number)
async def process_phone_or_instagram(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Дата вашего посещения нашего заведения (введите в формате ДД.ММ.ГГГГ):")


@start_router.message(RestourantReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    if re.match(r"\d{2}\.\d{2}\.\d{4}", message.text):
        await state.update_data(visit_date=message.text)
        await state.set_state(RestourantReview.food_rating)
        await message.answer("Как оцениваете качество еды?", reply_markup=food_rating_keyboard())
    else:
        await message.answer("Пожалуйста, введите дату в правильном формате (ДД.ММ.ГГГГ).")


@start_router.message(RestourantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    if message.text.isdigit() and 1 <= int(message.text) <= 5:
        await state.update_data(food_rating=int(message.text))
        await state.set_state(RestourantReview.cleanliness_rating)
        await message.answer("Как оцениваете чистоту заведения?", reply_markup=cleanliness_rating_keyboard())
    else:
        await message.answer("Пожалуйста, введите число от 1 до 5.")


@start_router.message(RestourantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    if message.text.isdigit() and 1 <= int(message.text) <= 5:
        await state.update_data(cleanliness_rating=int(message.text))
        await state.set_state(RestourantReview.extra_comments)
        await message.answer("Дополнительные комментарии?")
    else:
        await message.answer("Пожалуйста, введите число от 1 до 5.")


@start_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    data = await state.get_data()

    review_summary = (
        f"Ваш отзыв:\n"
        f"Имя: {data['name']}\n"
        f"Телефон/Instagram: {data['phone_number']}\n"
        f"Дата посещения: {data['visit_date']}\n"
        f"Оценка еды: {data['food_rating']}\n"
        f"Оценка чистоты: {data['cleanliness_rating']}\n"
        f"Дополнительные комментарии: {data['extra_comments']}"
    )

    await message.answer(f"Спасибо за ваш отзыв, {data['name']}!\n\n{review_summary}")

    db = Database('database/reviews.db')  # Убедитесь, что путь к базе данных правильный
    db.add_review(
        name=data['name'],
        phone_number=data['phone_number'],
        visit_date=data['visit_date'],
        food_rating=data['food_rating'],
        cleanliness_rating=data['cleanliness_rating'],
        extra_comments=data['extra_comments']
    )
    db.close()

    await state.clear()


def food_rating_keyboard():
    buttons = [KeyboardButton(text=str(i)) for i in range(1, 6)]
    return ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)


def cleanliness_rating_keyboard():
    buttons = [KeyboardButton(text=str(i)) for i in range(1, 6)]
    return ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)
