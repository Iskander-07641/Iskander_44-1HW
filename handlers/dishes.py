from config import bot,dp
from aiogram import types,Router,F
from aiogram.filters import Command
import random
from aiogram.types import FSInputFile
dishes_router = Router()

@dishes_router.message(F.text=="напитки")
async def drinks(message: types.Message):
    photo=FSInputFile('photo/maxito.jpg')
    await bot.send_photo(
         chat_id= message.from_user.id,
        photo =photo,
        caption = 'maxito'
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=FSInputFile('photo/milk_shake.jpg'),
    caption = 'milk shake'
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=FSInputFile('photo/ice_tee.jpeg'),
        caption='ice tee'
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=FSInputFile('photo/kofe.webp'),
        caption='kofe'
    )

@dishes_router.message(F.text=="еда")
async def food(message: types.Message):
    await bot.send_photo(
         chat_id= message.from_user.id,
        photo=FSInputFile('photo/burger.jpg'),
        caption = 'Бургер из свежей говядены'
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=FSInputFile('photo/salat.jpeg'),
        caption='Крабавай салат облитый лимоным сокам '
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=FSInputFile('photo/susi.jpg'),
        caption='Суши из акуллы'
    )