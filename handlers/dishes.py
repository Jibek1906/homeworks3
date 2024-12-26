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

    for dish in dishes:
        photo = dish[2]
        dish_text = (f"Блюдо: {dish[1]} "
                     f"\nЦена: {dish[3]} сом"
                     f"\nВес: {dish[8]} {dish[7]} "
                     f"\nОписание: {dish[4]} "
                     f"\nКатегория: {dish[5]} "
                     f"\nПринадлежит кухне: {dish[6]}")
        await message.answer_photo(photo=photo, caption=dish_text)


