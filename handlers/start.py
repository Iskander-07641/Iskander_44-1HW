from aiogram import types, Router, F
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def send_welcome(message: types.Message):
    buttons = [
        [types.InlineKeyboardButton(text="Инстаграм профиль", url="https://instagram.com/geeks.kg"),
         types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")],
        [types.InlineKeyboardButton(text="Наш адрес", callback_data="address"),
         types.InlineKeyboardButton(text="Контакты", callback_data="contacts")],
        [types.InlineKeyboardButton(text="Оставить отзыв", callback_data="feedback"),
         types.InlineKeyboardButton(text="О нас", callback_data="about_us")],
        [types.InlineKeyboardButton(text="Наши вакансии", callback_data="vacancies")],
        [types.InlineKeyboardButton(text="Салаты", callback_data="salads"),
         types.InlineKeyboardButton(text="Основные блюда", callback_data="main_courses"),
         types.InlineKeyboardButton(text="Десерты", callback_data="desserts")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer("Привет! Какую информацию вы хотите получить?", reply_markup=keyboard)


@start_router.callback_query(F.data == "about_us")
async def about_us(call:types.CallbackQuery): await call.answer("ничего🤷")


@start_router.callback_query(F.data == "vacancies")
async def vacancies(call:types.CallbackQuery): await call.answer("ничего🤷")


@start_router.callback_query(F.data.in_(['salads', 'main_courses', 'desserts']))
async def handle_dish_category(call: types.CallbackQuery):
    category = call.data
    if category == 'salads':
        dishes = "Цезарь"
    elif category == 'main_courses':
        dishes = "Стейк"
    elif category == 'desserts':
        dishes = "Тирамису"
    else:
        dishes = "Нет блюд в этой категории."

    await call.message.answer(f"Блюда в категории '{category.capitalize()}':\n{dishes}")
