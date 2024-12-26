from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot_config import database
from pprint import pprint

admin_router = Router()
admin_router.message.filter(F.from_user.id == 661832598)
admin_router.callback_query.filter(F.from_user.id == 661832598)

class DishAdding(StatesGroup):
    name = State()
    dish_photo = State()
    price = State()
    description = State()
    category = State()
    kitchen_type = State()
    weight_unit = State()
    weight = State()

@admin_router.message(Command("stop"))
@admin_router.message(F.text == "стоп")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Вы вышли из диалога")


@admin_router.message(Command("new_dish"), default_state)
async def start(message: types.Message, state: FSMContext):
    await message.answer("Если хотите выйти из диалога введите слово 'стоп'")
    await message.answer("Название блюда или напитка:")
    await state.set_state(DishAdding.name)

@admin_router.message(DishAdding.name)
async def dish_name(message: types.Message, state: FSMContext):
    name = message.text
    if not name.isalpha():
        await message.answer("Вводите название буквами")
        return
    await state.update_data(name=message.text)
    await message.answer("Загрузите фото блюда")
    await state.set_state(DishAdding.dish_photo)

@admin_router.message(DishAdding.dish_photo, F.photo)
async def dish_photo_process(message: types.Message, state: FSMContext):
    dish_photo = message.photo
    pprint(dish_photo)
    biggest_photo = dish_photo[-1]
    biggest_photo_id = biggest_photo.file_id
    await state.update_data(dish_photo=biggest_photo_id)
    await message.answer("Цена:")
    await state.set_state(DishAdding.price)

@admin_router.message(DishAdding.price)
async def dish_price(message: types.Message, state: FSMContext):
    price = message.text
    if not price.isdigit():
        await message.answer("Вводите только числа")
        return
    else:
        price = float(price)
    if price <= 100:
        await message.answer("Цена слишком низкая")
        photo = types.FSInputFile("images/no_money.jpg")
        await message.answer_photo(
            photo=photo
        )
        return
    elif price >= 800:
        await message.answer("Блюдо слишком дорогое")
        second_photo = types.FSInputFile("images/no.jpg")
        await message.answer_photo(
            photo=second_photo
        )
        return
    await state.update_data(price=price)
    await message.answer("Описание:")
    await state.set_state(DishAdding.description)

@admin_router.message(DishAdding.description)
async def dish_description(message: types.Message, state: FSMContext):
    description = message.text
    if len(description) < 30 or len(description) > 300:
        await message.answer("Описание должно быть в диапазоне 30-300 символов")
        return
    await state.update_data(description=description)
    categories_kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='салаты', callback_data='салаты')
            ],
            [
                types.InlineKeyboardButton(text='супы', callback_data='супы')
            ],
            [
                types.InlineKeyboardButton(text='первое блюдо', callback_data='первое блюдо')
            ],
            [
                types.InlineKeyboardButton(text='второе блюдо', callback_data='второе блюдо')
            ],
            [
                types.InlineKeyboardButton(text='горячие напитки', callback_data='горячие напитки')
            ],
            [
                types.InlineKeyboardButton(text='холодные напитки', callback_data='холодные напитки')
            ]
        ]
    )
    await message.answer("Категория:", reply_markup=categories_kb)
    await state.set_state(DishAdding.category)

@admin_router.callback_query(DishAdding.category)
async def dish_category(callback: types.CallbackQuery, state: FSMContext):
    if callback.data in ['салаты', 'супы', 'первое блюдо', 'второе блюдо', 'горячие напитки', 'холодные напитки']:
        category = callback.data
        await callback.message.answer(f"Ваше блюдо добавлено в категорию {callback.data}")
        await state.update_data(category=category)
        await callback.message.answer("К какой кухне принадлежит блюдо или напиток?")
        await state.set_state(DishAdding.kitchen_type)

@admin_router.message(DishAdding.kitchen_type)
async def dish_kitchen_type(message: types.Message, state: FSMContext):
    kitchen_type = message.text
    if kitchen_type.isdigit():
        await message.answer("Вводите только буквы")
        return
    await state.update_data(kitchen_type=kitchen_type)
    weight_kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='граммы', callback_data='грамм'),
                types.InlineKeyboardButton(text='литры', callback_data='литров'),
            ]
        ]
    )
    await message.answer("Выберите единицу измерения:", reply_markup=weight_kb)
    await state.set_state(DishAdding.weight_unit)

@admin_router.callback_query(DishAdding.weight_unit)
async def dish_weight_unit(callback: CallbackQuery, state: FSMContext):
    unit = callback.data
    await state.update_data(weight_unit=unit)
    await callback.message.answer("Введите вес блюда:")
    await state.set_state(DishAdding.weight)

@admin_router.message(DishAdding.weight)
async def dish_weight(message: types.Message, state: FSMContext):
    weight = message.text
    if not weight.isdigit():
        await message.answer("Вес блюда должен быть указан цифрами")
        return
    await state.update_data(weight=weight)
    data = await state.get_data()
    if data['weight_unit'] == "грамм":
        unit = "граммов"
    else:
        unit = "литров"
    await message.answer(f"Блюдо весит {data['weight']} {unit}")
    await message.answer("Блюдо успешно добавлено")
    print(data)
    database.save_dishes(data)
    await state.clear()






