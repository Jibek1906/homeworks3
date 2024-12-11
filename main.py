import asyncio

from bot_config import dp, bot

from handlers.start import start_router
from handlers.greeting import greeting_router
from handlers.menu import menu_router
from handlers.description_of_drinks import description_router
from handlers.random import random_router
from handlers.review_dialog import review_dialog_router

async def main():
    dp.include_router(start_router)
    dp.include_router(greeting_router)
    dp.include_router(menu_router)
    dp.include_router(description_router)
    dp.include_router(random_router)
    dp.include_router(review_dialog_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())