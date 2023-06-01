from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests, json
import config


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

keyboard = types.InlineKeyboardMarkup()
button_prev = types.InlineKeyboardButton(text='Назад', callback_data='prev')
button_next = types.InlineKeyboardButton(text='Далі', callback_data='next')
keyboard.add(button_prev, button_next)

imagesList = ['https://www.belta.by/images/storage/news/with_archive/2022/000467_1646837834_489198_big.jpg',
              'https://www.belta.by/uploads/images/beltaplus/2022/003_mar/009/001_orange.jpg',
              'https://www.belta.by/uploads/images/beltaplus/2022/003_mar/009/002_orange.jpg',
              'https://www.belta.by/uploads/images/beltaplus/2022/003_mar/009/003_orange.jpg',
              'https://www.belta.by/uploads/images/beltaplus/2022/003_mar/009/004_orange.jpg']
#imUrl = (i for i in imagesList)
# def imU(li):
#     for i in li:
#         yield i
# imUrl = imU(imagesList)
listindex = 0

@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    await bot.send_photo(chat_id=message.chat.id, photo=imagesList[0], caption='Початкове повідомлення', reply_markup=keyboard)

@dp.message_handler(commands=['ep'])
async def start(message: types.Message):
    x = requests.get('http://127.0.0.1:8000/ep/')
    await message.answer(x.text)

@dp.message_handler(commands=['ep2'])
async def start(message: types.Message):
    resp = requests.get('http://127.0.0.1:8000/ep/2')
    data = resp.json()
    for i in data:
        res = f"Company: {i['Name']}\nCategory {i['category']}\nAddress: {i['address']}\nTel {['tel']}\nSite {i['SiteURL']}\n\n"
       # await message.answer(res)
        await bot.send_photo(chat_id=message.chat.id, photo=i['PhotoURL'], caption=res,
                             reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == 'next')
async def change_image_callback(query: types.CallbackQuery):
    global listindex

    listindex = listindex + 1
    if listindex == 5:
        listindex = 0
    URLimage = imagesList[listindex]
    await bot.edit_message_media(chat_id=query.message.chat.id, message_id=query.message.message_id, media=types.InputMediaPhoto(media=URLimage, caption='Змінена картинка'),reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == 'prev')
async def change_image_callback(query: types.CallbackQuery):
    global listindex

    listindex = listindex - 1
    if listindex == 0:
        listindex = 4
    URLimage = imagesList[listindex]
    await bot.edit_message_media(chat_id=query.message.chat.id, message_id=query.message.message_id, media=types.InputMediaPhoto(media=URLimage, caption='Змінена картинка'),reply_markup=keyboard)


print("Bot start")
executor.start_polling(dp)
