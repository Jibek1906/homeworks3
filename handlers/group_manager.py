from aiogram import Router, F, types

group_router = Router()
group_router.message.filter(F.chat.type != "private")

banned_words = ("скучно", "грустно", "зря", "отстой", "плохо")

@group_router.message(F.text)
async def check_bad_words_handler(message: types.Message):
    for word in banned_words:
        if word in message.text.lower():
            await message.answer("Данные слова не приветствуются в нашей группе")
            await message.delete()
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id
            )
            await message.answer(f"Пользователь {message.from_user.first_name} был забанен за использование запрещенных слов")
            break