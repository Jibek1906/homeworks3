from aiogram import Router

from .start import start_router
from .greeting import greeting_router
from .menu import menu_router
from .description_of_drinks import description_router
from .random import random_router
from .review_dialog import review_dialog_router
from .dishes_manager import admin_router
from .dishes import dishes_router
from .group_manager import group_router

private_router = Router()

private_router.include_router(start_router)
private_router.include_router(greeting_router)
private_router.include_router(menu_router)
private_router.include_router(description_router)
private_router.include_router(random_router)
private_router.include_router(review_dialog_router)
private_router.include_router(admin_router)
private_router.include_router(dishes_router)
private_router.include_router(group_router)