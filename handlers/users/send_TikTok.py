from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text
from TikTok import tiktok_downloader
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery


@dp.message_handler(Text(startswith='https://vt.tiktok.com/'))
async def send_media(message:types.Message):
    result = tiktok_downloader(message.text)
    music = result['music']

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Скачать музыку",url="{}".format(music))]
        ]
    )
    await message.answer_audio(result['video'],reply_markup=btn)


