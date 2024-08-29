from aiogram import Router, types
from aiogram.filters import Command
from crawler.parser import crawl_house_kg

crawler_router = Router()


@crawler_router.message(Command("crawl_houses"))
async def send_house_links(message: types.Message):
    await message.answer("Начинаю кравлинг...")
    links = crawl_house_kg()

    if links:
        for link in links:
            await message.answer(link)
    else:
        await message.answer("Не удалось найти объявления.")
