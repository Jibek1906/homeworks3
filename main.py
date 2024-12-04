import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
from random import choice

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(Command("myinfo"))
async def info(message: types.Message):
    await message.answer(f'Ваше имя: {message.from_user.first_name},'
                         f'\nВаш id: {message.from_user.id},'
                         f'\nВаш username: {message.from_user.username}')

@dp.message(Command("random"))
async def random(message: types.Message):
    await message.answer(choice(('Арина','Даша','Атай')))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())