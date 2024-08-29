from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os
from db import Database
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

db = Database()

BANNED_WORDS = [
    # Английский
    "fuck", "shit", "bitch", "asshole", "cunt", "dick", "piss", "slut", "motherfucker", "twat",
    # Русский
    "блядь", "сука", "хуй", "пидор", "ебать", "гандон", "жопа", "мразь", "пизда", "урод",
    # Испанский
    "puta", "mierda", "cono", "gilipollas", "cabron", "polla", "chingar", "hijoputa", "zorra", "maricn",
    # Французский
    "putain", "merde", "con", "salop", "bordel", "encule", "fils de pute", "trou du cul", "salope", "cul",
    # Немецкий
    "ScheiBe", "Arschloch", "Fick", "Schlampe", "Hurensohn", "Wichser", "Kotzbrocken", "Schwanz", "Kacke", "Dreck",
    # Итальянский
    "cazzo", "merda", "stronzo", "puttana", "figlio di puttana", "bastardo", "vaffanculo", "coglione", "porca", "pazzo",
    # Португальский
    "merda", "caralho", "puta", "filho da puta", "bosta", "idiota", "porra", "desgracado", "cabrao", "vaca",
]


@dp.message_handler()
async def on_message(message: types.Message):
    if message.chat.type == types.ChatType.GROUP:
        user_id = message.from_user.id
        text = message.text.lower()

        # Проверка на наличие запрещенных слов
        if any(banned_word in text for banned_word in BANNED_WORDS):
            warnings = db.get_warnings(user_id)
            if warnings >= 3:
                await message.chat.ban_member(user_id)
                db.clear_warnings(user_id)
                await message.reply("Вы были забанены за нарушение правил.")
            else:
                db.add_warning(user_id)
                await message.reply(f"Вы получили предупреждение. Всего предупреждений: {warnings + 1}")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)
