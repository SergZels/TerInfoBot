from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor
import requests
import conf
from keyboards.keyboadrs import keyb_main, keyb_foot, keyb_kz, keyboard_prev_next
from loguru import logger
from aiogram.utils.executor import start_webhook

TEST_MODE = True
##------------------Блок ініціалізації-----------------##
if TEST_MODE:
    API_Token = conf.API_TOKEN_Test
else:
    API_Token = conf.TOKEN

ADMIN_ID = conf.ADMIN_ID
bot = Bot(token=API_Token)#os.getenv('TOKEN'))

logger.add("debug.txt")
# webhook settings
WEBHOOK_HOST = 'https://vmi957205.contaboserver.net'
WEBHOOK_PATH = '/prod_terinfobot'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '0.0.0.0'  # or ip 127.0.0.1
WEBAPP_PORT = 3010
bot = Bot(token=API_Token)
dp = Dispatcher(bot)

main_list = []
listindex = 0


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Вітаю!", reply_markup=keyb_main)


@dp.message_handler(filters.Text(startswith="Заклади харчування"))
async def foots(message: types.Message):
    global main_list, listindex
    main_list = []
    listindex = 0
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://media.acc.cv.ua/news/article/2020/08/16/62182/TGAyxyaM5Bh1c6pSizF2.w575.jpg",
                         caption="", reply_markup=keyb_foot)


@dp.message_handler(filters.Text(startswith="Краса і здоровя"))
async def foots(message: types.Message):
    global main_list, listindex
    main_list = []
    listindex = 0
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://orxid.in.ua/orx/wp-content/uploads/2021/04/20200430_104000-768x576-1.jpg",
                         caption="", reply_markup=keyb_kz)


@dp.message_handler(filters.Text(startswith="Магазини"))
async def foots(message: types.Message):
    global main_list, listindex
    main_list = []
    listindex = 0
    await message.answer("Даний функціонал ще в розробці")

@dp.message_handler(filters.Text(startswith="Послуги"))
async def foots(message: types.Message):
    global main_list, listindex
    main_list = []
    listindex = 0
    await message.answer("Даний функціонал ще в розробці")

@dp.message_handler(filters.Text(startswith="Оргацізації"))
async def foots(message: types.Message):
    global main_list, listindex
    main_list = []
    listindex = 0
    await message.answer("Даний функціонал ще в розробці")

@dp.message_handler(filters.Text(startswith="Цікаві місця"))
async def foots(message: types.Message):
    await message.answer("Даний функціонал ще в розробці")
# @dp.message_handler(commands=['ep'])
# async def start(message: types.Message):
#     x = requests.get('http://127.0.0.1:8000/ep/1')
#     await message.answer(x.text)


#---------------------------------------------------------------------------------
@dp.callback_query_handler(lambda c: c.data == 'next')
async def change_image_callback(query: types.CallbackQuery):
    global main_list, listindex
    if len(main_list) > 1:
        listindex = listindex + 1
        if listindex == len(main_list):
            listindex = 0
        i = main_list[listindex]
        res = f"Назва: {i['Name']}\nКатегорія: {i['category']}\nАдреса: {i['address']}\nТел.: {i['tel']}\nГрафік: {i['work_schedule']} \nСайт: {i['SiteURL']}\n\n"
        #await bot.send_photo(chat_id=query.message.chat.id, photo=i['PhotoURL'], caption=res,reply_markup=keyboard_prev_next)
        await bot.edit_message_media(chat_id=query.message.chat.id, message_id=query.message.message_id,
                                 media=types.InputMediaPhoto(media=i['PhotoURL'], caption=res),
                                 reply_markup=keyboard_prev_next)


@dp.callback_query_handler(lambda c: c.data == 'prev')
async def change_image_callback(query: types.CallbackQuery):
    global main_list, listindex
    if len(main_list) > 1:
        listindex = listindex - 1
        if listindex == -1:
            listindex = len(main_list)-1
        i = main_list[listindex]
        res = f"Назва: {i['Name']}\nКатегорія: {i['category']}\nАдреса: {i['address']}\nТел.: {i['tel']}\nГрафік: {i['work_schedule']}\nСайт: {i['SiteURL']}\n\n"
        await bot.edit_message_media(chat_id=query.message.chat.id, message_id=query.message.message_id,
                                 media=types.InputMediaPhoto(media=i['PhotoURL'], caption=res),
                                 reply_markup=keyboard_prev_next)


#-----------------------------------------------------------------------
@dp.callback_query_handler()
async def change_image_callback(query: types.CallbackQuery):
    global main_list
    category = query.data.split("_")[1]
    if TEST_MODE: URL = "http://localhost:8000/ep"
    else: URL = "http://localhost:8000/ep"
    resp = requests.get(URL, params={'category': category})
    if len(resp.text)>2:
        main_list = resp.json()
        i = main_list[0]

        res = f"Назва: {i['Name']}\nАдреса: {i['address']}\nТел.: {i['tel']}\nГрафік: {i['work_schedule']}\nСайт: {i['SiteURL']}\n\n"
        await bot.send_photo(chat_id=query.message.chat.id, photo=i['PhotoURL'], caption=res,
                             reply_markup=keyboard_prev_next)


##-------------------Запуск бота-------------------------##
if TEST_MODE:
    print("Bot running")
    #dp.middleware.setup(MidlWare())
    executor.start_polling(dp, skip_updates=True)
else:
    async def on_startup(dp):
        await bot.set_webhook(WEBHOOK_URL)
        logger.debug("Бот запущено")

    async def on_shutdown(dp):
        logger.debug('Зупиняюся..')
        await bot.delete_webhook()
        await dp.storage.close()
        await dp.storage.wait_closed()

    if __name__ == '__main__':
       # dp.middleware.setup(MidlWare())
        start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )


