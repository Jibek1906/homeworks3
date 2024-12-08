from aiogram import Router, types
from aiogram.filters import Command

menu_router = Router()

@menu_router.message(Command("menu"))
async def menu(message: types.Message):
    photo = types.FSInputFile("images/menu.png")
    await message.reply_photo(
        photo=photo,
        caption="меню"
    )
    await message.reply(f"Если хотите получить описание напитков введите "
                        f"\n/coffee "
                        f"\n/tea "
                        f"\n/desserts "
                        f"\n/noncoffee")