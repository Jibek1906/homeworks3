from aiogram import Router, F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

review_dialog_router = Router()

class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()

@review_dialog_router.callback_query(F.data == "review")
async def review(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Как вас зовут?")
    await state.set_state(RestaurantReview.name)

@review_dialog_router.message(RestaurantReview.name)
async def review2(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Ваш номер телефона")
    await state.set_state(RestaurantReview.phone_number)

@review_dialog_router.message(RestaurantReview.phone_number)
async def review3(message: types.Message, state: FSMContext):
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
        await state.update_data(cleanliness_rating=callback.data)
        await callback.message.answer("Дополнительные комментарии/жалоба")
        await state.set_state(RestaurantReview.extra_comments)

@review_dialog_router.message(RestaurantReview.extra_comments)
async def review6(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    await message.answer(f"Спасибо за ваш отзыв, {message.from_user.first_name}")
    data = await state.get_data()
    print(data)
    await state.clear()