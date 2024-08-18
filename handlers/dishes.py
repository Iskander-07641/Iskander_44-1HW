# dishes.py
from aiogram import types, Router, F
from aiogram.types import FSInputFile

dishes_router = Router()


@dishes_router.message(F.text == "напитки")
async def drinks(message: types.Message):
    photos = [
        ('photo/maxito.jpg', 'maxito'),
        ('photo/milk_shake.jpg', 'milk shake'),
        ('photo/ice_tee.jpeg', 'ice tee'),
        ('photo/kofe.webp', 'kofe')
    ]

    for photo_path, caption in photos:
        await message.answer_photo(
            photo=FSInputFile(photo_path),
            caption=caption
        )


@dishes_router.message(F.text == "еда")
async def food(message: types.Message):
    photos = [
        ('photo/burger.jpg', 'Бургер из свежей говядины'),
        ('photo/salat.jpeg', 'Крабовый салат облитый лимонным соком'),
        ('photo/susi.jpg', 'Суши из акулы')
    ]

    for photo_path, caption in photos:
        await message.answer_photo(
            photo=FSInputFile(photo_path),
            caption=caption
        )
