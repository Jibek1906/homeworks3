from aiogram import Router, types
from aiogram.filters import Command

myinfo_router = Router()

@myinfo_router.message(Command("myinfo"))
async def info(message: types.Message):
    await message.answer(f'Ваше имя: {message.from_user.first_name},'
                         f'\nВаш id: {message.from_user.id},'
                         f'\nВаш username: {message.from_user.username}')