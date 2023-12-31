from aiogram import types
from loader import dp,bot
from aiogram.dispatcher.filters import Text
from insta import insta_downloader

@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media(message:types.Message):
    link = message.text
    data = insta_downloader(link = link)

    if data == 'Пока что эта ссылка не работает':
        await message.answer('Простите но пока что по данной ссылке мы не можем работат')
    else:
        if data['type'] == 'image':
            await message.answer_photo(photo=data['media'])
        elif data['type'] == 'video':
            await message.answer_video(video=data['media'])
        elif data['type'] == 'carousel':
            for i in data['media']:
                await message.answer_document(document=i)
        else:
            await message.answer('Через эту ссылку мы не нашли ничего!')