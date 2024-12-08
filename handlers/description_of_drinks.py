from aiogram import Router, types
from aiogram.filters import Command

description_router = Router()

@description_router.message(Command("coffee"))
async def coffee_description(message: types.Message):
    await message.reply(f"Espresso: Крепкий концентрированный кофе, основа для большинства напитков."
                        f"\nDouble Espresso: Удвоенная порция эспрессо для более интенсивного вкуса."
                        f"\nLatte: Эспрессо с большим количеством вспененного молока."
                        f"\nAmericano: Разбавленный водой эспрессо, мягкий вкус."
                        f"\nMacchiato: Эспрессо с каплей молочной пены."
                        f"\nFlat White: Эспрессо с равномерно прогретым молоком."
                        f"\nCappuccino: Эспрессо с равными частями молока и пены.")

@description_router.message(Command("tea"))
async def tea_description(message: types.Message):
    await message.reply(f"Lemon Tea: Чай с добавлением лимона, освежающий и слегка кисловатый."
                        f"\nMango Tea: Чай с фруктовыми нотами манго, сладкий и ароматный."
                        f"\nJasmine: Чай с жасмином, нежный и цветочный вкус."
                        f"\nGreen Tea: Легкий и травяной чай с полезными антиоксидантами."
                        f"\nMint Tea: Освежающий чай с мятой, расслабляющий и бодрящий.")

@description_router.message(Command("desserts"))
async def desserts_description(message: types.Message):
    await message.reply(f"Strawberry Waffle: Вафли с клубничным топпингом, сладкие и нежные."
                        f"\nCinnamon Roll: Мягкая булочка с корицей, ароматная и пряная."
                        f"\nLemon Pie: Пирог с лимонной начинкой, сладкий с легкой кислинкой."
                        f"\nCroissant: Классический французский круассан, слоеный и масляный."
                        f"\nChocolate Waffle: Вафли с шоколадом, насыщенные и сладкие."
                        f"\nBrownies: Шоколадный десерт, влажный и насыщенный."
                        f"\nCheesecake: Классический чизкейк, сливочный и нежный."
                        f"\nChocolate Muffin: Маффин с шоколадом, сладкий и воздушный.")

@description_router.message(Command("noncoffee"))
async def non_coffee_description(message: types.Message):
    await message.reply(f"Hot Chocolate: Густой и насыщенный горячий шоколад, согревающий напиток."
                        f"\nMilkshake: Классический молочный коктейль, сладкий и освежающий."
                        f"\nSmoothie: Полезный напиток из свежих фруктов и ягод."
                        f"\nLemonade: Освежающий лимонад с легкой кислинкой."
                        f"\nVanilla Milkshake: Молочный коктейль с ароматом ванили, сладкий и нежный.")