from aiogram import Router, types
from aiogram.filters import Command
from random import choice

random_router = Router()

@random_router.message(Command("random"))
async def random(message: types.Message):
    random_recipe = choice([cinnamon_roll_recipe, cheesecake_recipe, lemon_pie_recipe, croissant_recipe, chocolate_muffin_recipe])
    await random_recipe(message)

async def cheesecake_recipe(message: types.Message):
    photo = types.FSInputFile("images/cheesecake.jpg")
    await message.reply_photo(
        photo=photo,
        caption="Рецепт Cheesecake:"
                "\n1.Измельчите 200 г печенья, смешайте с 100 г масла, утрамбуйте в форму."
                "\n2.Взбейте 500 г сыра, 150 г сахара, 3 яйца, 150 мл сливок, добавьте ваниль."
                "\n3.Выпекайте 50 мин при 160°C, охладите."
                "\n4.Украсьте и подавайте!"
    )

async def cinnamon_roll_recipe(message: types.Message):
    photo = types.FSInputFile("images/cinnamon_roll.jpg")
    await message.reply_photo(
        photo=photo,
        caption="Рецепт Cinnamon Roll:"
                "\n1.Замесите тесто из 500 г муки, 200 мл молока, 1 яйца, 50 г масла, 50 г сахара и 7 г дрожжей."
                "\n2.Раскатайте, смажьте 50 г масла, посыпьте смесью 100 г сахара и 2 ч. л. корицы."
                "\n3.Сверните рулет, нарежьте, дайте подойти 30 мин."
                "\n4.Выпекайте 20 мин при 180°C."
    )

async def lemon_pie_recipe(message: types.Message):
    photo = types.FSInputFile("images/lemon_pie.jpg")
    await message.reply_photo(
        photo=photo,
        caption="Рецепт Lemon Pie:"
                "\n1.Приготовьте основу: смешайте 200 г муки, 100 г сливочного масла, 50 г сахара, 1 яйцо. Раскатайте, выложите в форму, выпекайте 15 мин при 180°C."
                "\n2.	Для начинки: смешайте 3 яйца, 150 г сахара, сок и цедру 2 лимонов, 50 г сливочного масла."
                "\n3.	Вылейте начинку на основу, выпекайте 20-25 мин при 180°C."
                "\n4.	Охладите, украсьте взбитыми сливками и кусочком лимона."
    )

async def croissant_recipe(message: types.Message):
    photo = types.FSInputFile("images/croissant.jpg")
    await message.reply_photo(
        photo=photo,
        caption="Рецепт Croissant:	"
                "\n1.Тесто: Смешайте 500 г муки, 60 г сахара, 10 г соли, 7 г дрожжей, 250 мл молока, 50 г масла. Оставьте на 1 час."
                "\n2.Слоение: Раскатайте тесто, уложите 250 г холодного масла, сложите конвертом."
                "\n3.Раскатка: Раскатайте и сложите тесто трижды, охлаждая 30 минут между раскатками."
                "\n4.Формовка: Нарежьте треугольники, сверните в круассаны, оставьте на 1 час."
                "\n5.Выпечка: Смажьте яйцом, выпекайте 20 мин при 200°C."
    )

async def chocolate_muffin_recipe(message: types.Message):
    photo = types.FSInputFile("images/chocolate_muffin.jpg")
    await message.reply_photo(
        photo=photo,
        caption="Рецепт Chocolate Muffin:"
                "\n1.Смешайте 200 г муки, 100 г сахара, 2 ч. л. разрыхлителя, 1 ч. л. какао-порошка."
                "\n2.В отдельной миске взбейте 1 яйцо, 150 мл молока, 100 г растопленного масла."
                "\n3.Соедините сухие и жидкие ингредиенты, добавьте 100 г шоколадных капель."
                "\n4.Разложите тесто по формочкам и выпекайте 20-25 минут при 180°C."
    )