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
    # ����������
    "fuck", "shit", "bitch", "asshole", "cunt", "dick", "piss", "slut", "motherfucker", "twat",
    # �������
    "�����", "����", "���", "�����", "�����", "������", "����", "�����", "�����", "����",
    # ���������
    "puta", "mierda", "cono", "gilipollas", "cabron", "polla", "chingar", "hijoputa", "zorra", "maricn",
    # �����������
    "putain", "merde", "con", "salop", "bordel", "encule", "fils de pute", "trou du cul", "salope", "cul",
    # ��������
    "ScheiBe", "Arschloch", "Fick", "Schlampe", "Hurensohn", "Wichser", "Kotzbrocken", "Schwanz", "Kacke", "Dreck",
    # �����������
    "cazzo", "merda", "stronzo", "puttana", "figlio di puttana", "bastardo", "vaffanculo", "coglione", "porca", "pazzo",
    # �������������
    "merda", "caralho", "puta", "filho da puta", "bosta", "idiota", "porra", "desgracado", "cabrao", "vaca",
]


@dp.message_handler()
async def on_message(message: types.Message):
    if message.chat.type == types.ChatType.GROUP:
        user_id = message.from_user.id
        text = message.text.lower()

        # �������� �� ������� ����������� ����
        if any(banned_word in text for banned_word in BANNED_WORDS):
            warnings = db.get_warnings(user_id)
            if warnings >= 3:
                await message.chat.ban_member(user_id)
                db.clear_warnings(user_id)
                await message.reply("�� ���� �������� �� ��������� ������.")
            else:
                db.add_warning(user_id)
                await message.reply(f"�� �������� ��������������. ����� ��������������: {warnings + 1}")

# ������ ����
if __name__ == '__main__':
    executor.start_polling(dp)
