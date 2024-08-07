from config import bot,dp
from aiogram import types,Router,F
from aiogram.filters import Command
import random

recipe_router = Router()


@recipe_router.message(Command("random_recipe"))
async def send_recipe(message: types.Message):
    recipes = [
        "Рецепт 1: Смешайте муку, яйца и сахар. Выпекать при температуре 180°C 25 минут.",
        "Рецепт 2: Сварите макароны, затем добавьте томатный соус и сыр.",
        "Рецепт 3: Курицу гриль с солью и перцем.",
        "Рецепт 4: Приготовьте салат из салата, помидоров и огурцов.",
        "Рецепт 5: Обжарьте лук и чеснок, затем добавьте говядину и готовьте до готовности."
    ]
    recipe = random.choice(recipes)
    await message.answer(recipe)