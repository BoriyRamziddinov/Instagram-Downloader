from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp,bot


admin_id = 622321207

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}я помогаю скачивать видео из Инстаграма.Отправь мне ссылку!")
    await bot.send_message(admin_id,f"{message.from_user.first_name}\n {message.from_user.username} нажал на кнопку")
