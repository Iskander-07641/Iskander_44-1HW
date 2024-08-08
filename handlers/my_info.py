from config import bot,dp
from aiogram import types,Router,F
from aiogram.filters import Command


my_info_router = Router()


@my_info_router.message(Command("my_info"))
async def send_info(message: types.Message):
    user = message.from_user
    await message.answer(
        f"Ваш id: {user.id}\n"
        f"Ваше имя: {user.first_name}\n"
        f"Ваше имя пользователя: {user.username}"
    )