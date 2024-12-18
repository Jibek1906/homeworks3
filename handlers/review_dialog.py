from aiogram import Router, F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot_config import database
from datetime import datetime

review_dialog_router = Router()

class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()
    date = State()

@review_dialog_router.callback_query(F.data == "review")
async def start_process(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Как вас зовут?")
    await state.set_state(RestaurantReview.name)

@review_dialog_router.message(RestaurantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    if not name.isalpha():
        await message.answer("Пишите имя буквами")
        return
    if len(name) < 3 or len(name) > 15:
        await message.answer("Количество символов должно быть от 3 до 15")
        return
    await state.update_data(name=message.text)
    await message.answer("Ваш номер телефона")
    await state.set_state(RestaurantReview.phone_number)

@review_dialog_router.message(RestaurantReview.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    if not phone_number.isdigit():
        await message.answer("Пожалуйста, вводите только цифры")
        return
    if len(phone_number) != 10:
        await message.answer("Номер телефона должен состоять из 10 цифр")
        return
    await state.update_data(phone_number=message.text)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='1', callback_data='1'),
                types.InlineKeyboardButton(text='2', callback_data='2'),
                types.InlineKeyboardButton(text='3', callback_data='3'),
                types.InlineKeyboardButton(text='4', callback_data='4'),
                types.InlineKeyboardButton(text='5', callback_data='5')
            ]
        ]
    )
    await message.answer("Как оцениваете качество еды?", reply_markup=kb)
    await state.set_state(RestaurantReview.food_rating)

@review_dialog_router.callback_query(RestaurantReview.food_rating)
async def process_food_rating(callback: types.CallbackQuery, state: FSMContext):
    if callback.data in ['1', '2', '3', '4', '5']:
        rating = int(callback.data)
        if rating >= 1 and rating <= 3:
            await callback.message.answer(
                f"Вы поставили {callback.data}. Спасибо за честный отзыв, мы постараемся улучшить нашу кухню.")
        elif rating >= 4 and rating <= 5:
            await callback.message.answer(
                f"Вы поставили {callback.data}. Спасибо за положительный отзыв. Будем стараться удерживать данный уровень кухни.")
        await state.update_data(food_rating=callback.data)

        await state.update_data(food_rating=callback.data)
        cleanliness_rating_kb = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(text='Плохо', callback_data='bad')
                ],
                [
                    types.InlineKeyboardButton(text='Не очень', callback_data='not_good')
                ],
                [
                    types.InlineKeyboardButton(text='Хорошо', callback_data='good')
                ],
                [
                    types.InlineKeyboardButton(text='Прекрасно', callback_data='perfect')
                ],
                [
                    types.InlineKeyboardButton(text='Превосходно', callback_data='amazing')
                ]
            ]
        )
        await callback.answer()
        await callback.message.answer("Как оцениваете чистоту заведения?", reply_markup=cleanliness_rating_kb)
        await state.set_state(RestaurantReview.cleanliness_rating)

@review_dialog_router.callback_query(RestaurantReview.cleanliness_rating)
async def process_cleanliness_rating(callback: types.CallbackQuery, state: FSMContext):
    if callback.data in ['bad', 'not_good', 'good', 'perfect', 'amazing']:
        food_rating = callback.data
        if food_rating in ['bad', 'not_good']:
            await callback.message.answer("Сожалеем, что вам не понравилась чистота нашего заведения.")
        elif food_rating == 'good':
            await callback.message.answer("Будем стараться сделать наше заведение чище.")
        elif food_rating in ['perfect', 'amazing']:
            await callback.message.answer("Очень рады, что вам понравилась чистота нашего заведения.")
        await state.update_data(cleanliness_rating=callback.data)
        await callback.message.answer("Дополнительные комментарии/жалоба")
        await state.set_state(RestaurantReview.extra_comments)

@review_dialog_router.message(RestaurantReview.extra_comments)
async def process_extra_comments(message: types.Message,state: FSMContext):
    extra_comments = message.text
    if len(extra_comments) > 500:
        await message.answer("Ваши текст слишком длинный. Пожалуйста, ограничьтесь 500 символами.")
        return
    await state.update_data(extra_comments=message.text)
    await message.answer("Дата посещения?"
                         "\nВведите дату без пробелов, в формате ДД.ММ.ГГГГ (например, 19.06.2004)")
    await state.set_state(RestaurantReview.date)

@review_dialog_router.message(RestaurantReview.date)
async def process_date(message: types.Message, state: FSMContext):
    date = message.text
    if " " in date or "\t" in date:
        await message.answer("Введите дату без пробелов, в формате ДД.ММ.ГГГГ (например, 19.06.2004)")
        return
    try:
        visit_date = datetime.strptime(date, "%d.%m.%Y")
    except ValueError:
        await message.answer("Введите дату в формате ДД.ММ.ГГГГ (например, 19.06.2004)")
        return
    await state.update_data(date=visit_date.strftime("%d.%m.%Y"))
    await message.answer(f"Спасибо за ваш отзыв, {message.from_user.first_name}")
    data = await state.get_data()
    print(data)
    database.save_reviews(data)
    await state.clear()