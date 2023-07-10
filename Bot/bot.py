from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor
import requests
import conf
from keyboards.keyboadrs import keyb_main, keyb_foot, keyb_kz, keyboard_prev_next_about,keyboard_prev_next, keyb_organizations
from loguru import logger
from aiogram.utils.executor import start_webhook

TEST_MODE = True

if conf.VPS:
    TEST_MODE = False

##------------------Блок ініціалізації-----------------##
if TEST_MODE:
    API_Token = conf.API_TOKEN_Test
else:
    API_Token = conf.TOKEN

ADMIN_ID = conf.ADMIN_ID
bot = Bot(token=API_Token)

logger.add("debug.txt")
# webhook settings
WEBHOOK_HOST = 'https://vmi957205.contaboserver.net'
WEBHOOK_PATH = '/prod_terinfobot'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '0.0.0.0'  # or ip 127.0.0.1
WEBAPP_PORT = 3007
bot = Bot(token=API_Token)
dp = Dispatcher(bot)

main_list = []
listindex = 0

def getstring(li :list)->str:
#str = f"<strong>Назва:</strong> {li['Name']}\n<strong>Опис:</strong> {li['About']}\n<strong>Адреса:</strong> {li['address']}\n"
    str = f"Назва: {li['Name']}\nОпис: {li['About']}\nАдреса: {li['address']}\n"
    if li['tel']!= "":
      #  str+=f"<strong>Тел.:</strong> {li['tel']}\n"
        str += f"Тел.: {li['tel']}\n"
    if li['work_schedule']!="":
        grafik = f"{li['work_schedule']}".split('#')
        tempstr=""
        for i in grafik:
            tempstr+=f"{i}\n"
       # str += f"<strong>Графік:</strong> {tempstr}"
        str += f"Графік: {tempstr}"
    if li['SiteURL']!="":
        #str += f"<a href='{li['SiteURL']}'>Сайт</a> "
        str += f"Сайт: {li['SiteURL']}\n"
    if li['FaсebookURL']!="":
        str += f"Facebook: {li['FaсebookURL']}\n"
     #   str += f"<a href='{li['FaсebookURL']}'>Facebook</a> "
    if li['InstagramURL']!="":
        str += f"Instagram: {li['InstagramURL']}\n"
        #str += f"<a href='{li['InstagramURL']}'>Instagram</a> "

    return str


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Вітаємо! Оберіть, будь ласка, категорію👇", reply_markup=keyb_main)


@dp.message_handler(filters.Text(startswith="Заклади харчування"))
async def foots(message: types.Message):
    global main_list, listindex
    main_list = []
    listindex = 0
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://media.acc.cv.ua/news/article/2020/08/16/62182/TGAyxyaM5Bh1c6pSizF2.w575.jpg",
                         caption="", reply_markup=keyb_foot)

@dp.message_handler(filters.Text(startswith="Магаз"))
async def foots(message: types.Message):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Продуктові', callback_data='команда_МагПродуктові')
    but_2 = types.InlineKeyboardButton(text='Дитячі', callback_data='команда_МагДитячі')
    but_3 = types.InlineKeyboardButton(text='Господарські', callback_data='команда_МагГосподарські')
    but_4 = types.InlineKeyboardButton(text='Одяг та взуття', callback_data='команда_МагОдягТаВзуття')
    but_5 = types.InlineKeyboardButton(text='Ветиринарні', callback_data='команда_МагВетиринарні')
    but_6 = types.InlineKeyboardButton(text='Посуд', callback_data='команда_МагПосуд')
    but_7 = types.InlineKeyboardButton(text='Квіти', callback_data='команда_МагКвіти')
    but_8 = types.InlineKeyboardButton(text='Господарські магазини', callback_data='команда_ГосподарськіМагазини')
    but_9 = types.InlineKeyboardButton(text='Книги та канцелярія', callback_data='команда_Канцелярія')
    but_10 = types.InlineKeyboardButton(text='Телефони та оргтехніка', callback_data='команда_Телефони_оргтехніка')
    keyb.add(but_1,but_2).add(but_3,but_4).add(but_5,but_6).add(but_7,but_9).add(but_8).add(but_10)
   # await message.answer("Даний функціонал ще в розробці!",reply_markup=keyb)
    Url = 'https://ceha.com.ua/wp-content/uploads/2016/02/kompleksnoe-reklamnoe-oformlenie-magazinov-supermarketov.jpg'
    await bot.send_photo(chat_id=message.chat.id,photo=Url,caption="", reply_markup=keyb)

@dp.message_handler(filters.Text(startswith="Краса і здоровя"))
async def foots(message: types.Message):
    global main_list, listindex
    main_list = []
    listindex = 0
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://inventure.com.ua/img/thumb.990.660/upload/pic2020-1q/HairSalon-girl-pic.jpg",
                         caption="", reply_markup=keyb_kz)


@dp.message_handler(filters.Text(startswith="Магазини"))
async def foots(message: types.Message):
    global main_list, listindex
    main_list = []
    listindex = 0
    await message.answer("Даний функціонал ще в розробці.")

@dp.message_handler(filters.Text(startswith="Послуги"))
async def foots(message: types.Message):
    global main_list, listindex
    main_list = []
    listindex = 0
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Ательє✂️', callback_data='команда_Ательє')
    but_2 = types.InlineKeyboardButton(text='Ремонт авто🚗', callback_data='команда_РемонтАвто')
    but_3 = types.InlineKeyboardButton(text='Ремонт техніки🪛', callback_data='команда_РемонтТехніки')
    but_4 = types.InlineKeyboardButton(text='Нотаріуси', callback_data='команда_Нотаріуси')
    but_5 = types.InlineKeyboardButton(text='Дитяче дозвілля', callback_data='команда_ДитячеДозвілля')
    but_6 = types.InlineKeyboardButton(text='Інтернет-провайдери', callback_data='команда_ІнтернетПровайдери')
    but_7 = types.InlineKeyboardButton(text='Поліграфія та студія дизайну', callback_data='команда_СтудіїДизайну')
    but_8 = types.InlineKeyboardButton(text='Доставка', callback_data='команда_Доставка')
    keyb.add(but_2,but_4).add(but_1).add(but_3,but_8).add(but_5).add(but_6).add(but_7)
   # await message.answer("Даний функціонал ще в розробці", reply_markup=keyb)
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://orxid.in.ua/orx/wp-content/uploads/2021/04/20200430_104000-768x576-1.jpg",
                         caption="", reply_markup=keyb)

@dp.message_handler(filters.Text(startswith="ВПО+військові"))
async def foots(message: types.Message):
    global main_list, listindex
    main_list = []
    listindex = 0
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Дорожня карта ВПО', callback_data='команда_ДорожняКартаВПО')
    but_2 = types.InlineKeyboardButton(text='Корисні локації', callback_data='команда_КорисніЛокації')
    but_3 = types.InlineKeyboardButton(text='Допомога військовим🪖', callback_data='команда_ДопомогаВійськовим')
    but_4 = types.InlineKeyboardButton(text='Реабілітаційні центри', callback_data='команда_РеабілітаційніЦентри')
    but_5 = types.InlineKeyboardButton(text='Психологічна підтримка', callback_data='команда_ПсихологічнаПідтримка')
    but_6 = types.InlineKeyboardButton(text='Пошук роботи', callback_data='команда_ПошукРоботи')
    keyb.add(but_1).add(but_2).add(but_3).add(but_4).add(but_5).add(but_6)
   # await message.answer("Даний функціонал ще в розробці", reply_markup=keyb)
    url = 'https://upravbud.info/content/uploads/2022/04/016-980x620.png'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb)

@dp.message_handler(filters.Text(startswith="Організації"))
async def foots(message: types.Message):
    await message.answer("Оберіть, будь ласка, категорію організацій👇",reply_markup=keyb_organizations)

@dp.message_handler(filters.Text(startswith="Фінансові та кредитні установи"))
async def foots(message: types.Message):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Банки', callback_data='команда_Банки')
    but_2 = types.InlineKeyboardButton(text='Казначейство', callback_data='команда_Казначейство')
    but_3 = types.InlineKeyboardButton(text='Кредитні спілки', callback_data='команда_КредитніСпілки')
    keyb.add(but_1).add(but_2).add(but_3)
   # await message.answer("Даний функціонал ще в розробці",reply_markup=keyb)
    url = 'https://minfin.com.ua/img/2022/85137707/0988d5c75c8fe6ca4b45d900175db854.jpeg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb)
@dp.message_handler(filters.Text(startswith="Міська рада"))
async def foots(message: types.Message):
    keyb_mr = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Голова громади', callback_data='команда_ГоловаГромади')
    but_2 = types.InlineKeyboardButton(text='Заступники голови', callback_data='команда_ЗаступникиГолови')
    but_3 = types.InlineKeyboardButton(text='Старостати', callback_data='команда_Старости')
    but_4 = types.InlineKeyboardButton(text='Відділи', callback_data='команда_Відділи')
    keyb_mr.add(but_1).add(but_2).add(but_3).add(but_4)
    await message.answer("Даний функціонал ще в розробці",reply_markup=keyb_mr)

@dp.message_handler(filters.Text(startswith="Освіта"))
async def foots(message: types.Message):
    keyb_os = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Школи І ступенів', callback_data='команда_Школи_І_ступенів')
    but_2 = types.InlineKeyboardButton(text='Школи ІІ ступенів', callback_data='команда_Школи_ІІ_ступенів')
    but_3 = types.InlineKeyboardButton(text='Школи ІІІ ступенів', callback_data='команда_Школи_ІІІ_ступенів')
    but_4 = types.InlineKeyboardButton(text='Садочки', callback_data='команда_Садочки')
    but_5 = types.InlineKeyboardButton(text='Позашкільна освіта', callback_data='команда_Позашкільна освіта')
    keyb_os.add(but_1).add(but_2).add(but_3).add(but_4).add(but_5)
   # await message.answer("Даний функціонал ще в розробці",reply_markup=keyb_os)
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://images.unian.net/photos/2022_09/thumb_files/400_0_1664111474-8193.jpg?r=616244",
                         caption="", reply_markup=keyb_os)

@dp.message_handler(filters.Text(startswith="Культура"))
async def foots(message: types.Message):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='ЦКіДи', callback_data='команда_ЦКіДи')
    but_2 = types.InlineKeyboardButton(text='Музеї, садиби', callback_data='команда_МузеїСадиби')
    but_3 = types.InlineKeyboardButton(text='Бібліотеки', callback_data='команда_Бібліотеки')
    but_4 = types.InlineKeyboardButton(text='Туризм', callback_data='команда_Туризм')
    keyb.add(but_1).add(but_2).add(but_3).add(but_4)
    await message.answer("Даний функціонал ще в розробці",reply_markup=keyb)

@dp.message_handler(filters.Text(startswith="Охорона здоров"))
async def foots(message: types.Message):
    keyb_oxz = types.InlineKeyboardMarkup()
    but_1= types.InlineKeyboardButton(text='КНП ТМР "Теребовлянська міська лікарня"', callback_data='команда_міськаЛікарня')
    but_2 = types.InlineKeyboardButton(text='Сімейна медицина', callback_data='команда_Сімейна_медицина')
    but_3 = types.InlineKeyboardButton(text='Ветеринарія', callback_data='команда_Ветеринарія')
    but_4 = types.InlineKeyboardButton(text='Аптеки', callback_data='команда_Аптеки')
    but_5 = types.InlineKeyboardButton(text='Стоматології', callback_data='команда_Стоматології')
    but_6 = types.InlineKeyboardButton(text='Лабораторії', callback_data='команда_Лабораторії')
    keyb_oxz.add(but_1).add(but_2).add(but_3).add(but_4).add(but_5).add(but_6)
    await message.answer("Даний функціонал ще в розробці",reply_markup=keyb_oxz)

@dp.message_handler(filters.Text(startswith="Інші установи"))
async def foots(message: types.Message):
    keyb_ii = types.InlineKeyboardMarkup()
    but_1= types.InlineKeyboardButton(text='Укрпошта', callback_data='команда_Укрпошта')
    but_2 = types.InlineKeyboardButton(text='Центр зайнятості', callback_data='команда_ЦентрЗайнятості')
    but_3 = types.InlineKeyboardButton(text='Суд', callback_data='команда_Суд')
    but_4 = types.InlineKeyboardButton(text='РЕС', callback_data='команда_РЕС')
    but_5 = types.InlineKeyboardButton(text='Газова служба', callback_data='команда_Газова_служба')
    but_6 = types.InlineKeyboardButton(text='Поліція', callback_data='команда_Поліція')
    but_7 = types.InlineKeyboardButton(text='Пожежна', callback_data='команда_Пожежна')
    but_8 = types.InlineKeyboardButton(text='Газета “Воля”', callback_data='команда_Газета_Воля')
    keyb_ii.add(but_1).add(but_2).add(but_3,but_4).add(but_5).add(but_6,but_7).add(but_8)
    await message.answer("Даний функціонал ще в розробці",reply_markup=keyb_ii)



@dp.message_handler(filters.Text(startswith="⬅️ На головну"))
async def foots(message: types.Message):
   await message.answer("Головне меню",reply_markup=keyb_main)

@dp.message_handler(filters.Text(startswith="Підприємства"))
async def foots(message: types.Message):
    await message.answer("Даний функціонал ще в розробці")

@dp.message_handler(filters.Text(startswith="Військовим"))
async def foots(message: types.Message):
    await message.answer("Даний функціонал ще в розробці")

@dp.message_handler()
async def foots(message: types.Message):
    await message.answer("Даний функціонал ще в розробці. ")
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

        try:
            i = main_list[listindex]
           # res = f"Назва: {i['Name']}\nОпис: {i['About']}\nАдреса: {i['address']}\nТел.: {i['tel']}\nГрафік: {i['work_schedule']}\nСайт:{i['SiteURL']}\n{listindex+1} із {len(main_list)}\n"
            res = f"{getstring(i)}{listindex + 1} із {len(main_list)}\n"
            await bot.edit_message_media(chat_id=query.message.chat.id, message_id=query.message.message_id,
                                     media=types.InputMediaPhoto(media=i['PhotoURL'], caption=res),
                                     reply_markup=keyboard_prev_next)
        except IndexError:
            print(f"IndexError listindex - {listindex}")
            logger.debug(f"IndexError listindex - {listindex} mainlist -{main_list}")


@dp.callback_query_handler(lambda c: c.data == 'prev')
async def change_image_callback(query: types.CallbackQuery):
    global main_list, listindex
    if len(main_list) > 1:
        listindex = listindex - 1
        if listindex == -1:
            listindex = len(main_list)-1

        try:
            i = main_list[listindex]
           # res = f"Назва: {i['Name']}\nОпис: {i['About']}\nАдреса: {i['address']}\nТел.: {i['tel']}\nГрафік: {i['work_schedule']}\nСайт:{i['SiteURL']}\n                    {listindex+1} із {len(main_list)}\n"
            res = f"{getstring(i)}{listindex + 1} із {len(main_list)}\n"

            await bot.edit_message_media(chat_id=query.message.chat.id, message_id=query.message.message_id,
                                         media=types.InputMediaPhoto(media=i['PhotoURL'], caption=res),
                                         reply_markup=keyboard_prev_next)
        except IndexError:
            print(f"IndexError listindex - {listindex}")
            logger.debug(f"IndexError listindex - {listindex} mainlist -{main_list}")


@dp.callback_query_handler(lambda c: c.data == 'about')
async def change_image_callback(query: types.CallbackQuery):
    global main_list, listindex
    i = main_list[listindex]
    res = f"Назва: {i['Name']}\nКатегорія: {i['category']}\nАдреса: {i['address']}\nТел.: {i['tel']}\nГрафік: {i['work_schedule']}\nСайт:{i['SiteURL']}\n               {listindex+1} із {len(main_list)}\n"
    await bot.edit_message_media(chat_id=query.message.chat.id, message_id=query.message.message_id,
                                     media=types.InputMediaPhoto(media=i['PhotoURL'], caption=res),
                                     reply_markup=keyboard_prev_next)


#-----------------------------------------------------------------------
@dp.callback_query_handler()
async def change_image_callback(query: types.CallbackQuery):
    global main_list
    category = query.data.split("_")[1] # берем стрічку типу "команда_клініки" та витягуємо із неї клініки
    URL = "https://vmi957205.contaboserver.net/terinfobot/ep/"
    resp = requests.get(URL, params={'category': category})

    if len(resp.text) > 2:
        main_list = resp.json()
        i = main_list[0]
       # res = f"Назва: {i['Name']}\nОпис: {i['About']}\nАдреса: {i['address']}\n\nТел.: {i['tel']}\nГрафік: {i['work_schedule']}\nСайт:{i['SiteURL']}\n                    1 із {len(main_list)}\n"
        res= f"{getstring(i)}\n1 із {len(main_list)}\n"
        try:
         await bot.send_photo(chat_id=query.message.chat.id, photo=i['PhotoURL'],caption=res,reply_markup=keyboard_prev_next)
        #await bot.send_message(chat_id=query.message.chat.id,text=res, reply_markup=keyboard_prev_next,parse_mode="HTML")
        except:
            print("aiogram.utils.exceptions.BadRequest: Wrong type of the web page content")
            await bot.send_message(chat_id=query.message.chat.id, text="помилка - aiogram.utils.exceptions.BadRequest", reply_markup=keyb_main)

    else:
        await bot.send_message(chat_id=query.message.chat.id,text="Нажаль ці дані відсутні, бот ще в розробці 🔧",reply_markup=keyb_main)


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


