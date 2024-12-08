from aiogram import Router, types
from aiogram.filters import Command

greeting_router = Router()

@greeting_router.message(Command("hello"))
async def greeting(message: types.Message):
    await message.reply(f"Добро пожаловать в наше уютное кафе! Здесь вас ждёт ароматный кофе, свежая выпечка и тёплая атмосфера. "
                        f"\nЧтобы ознакомиться с меню напишите /menu")