from aiogram import Router, types
from aiogram.filters import Command
from bot_config import database

dishes_router = Router()

@dishes_router.message(Command("dishes"))
async def see_all_dishes(message: types.Message):
    dishes = database.get_dishes()
    if not dishes:
        await message.answer("Нет блюд в базе данных")
        return

    dishes_text = "\n".join(
        [f"{dish[0]}. {dish[1]} "
         f"\nВес: {dish[2]} {dish[6]} "
         f"\nОписание: {dish[3]},"
         f"\nКатегория: {dish[4]}, "
         f"\nПринадлежит кухне: {dish[5]}" for dish in dishes]
    )
    await message.answer(dishes_text)

