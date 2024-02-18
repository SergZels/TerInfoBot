from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters, FSMContext
from aiogram.utils import executor
import requests
import conf
from keyboards.keyboadrs import keyb_shops,keyb_piple,keyb_main, keyb_foot, keyb_kz, keyboard_prev_next_about, keyboard_prev_next, \
    keyb_organizations
from loguru import logger
from aiogram.utils.executor import start_webhook
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram_broadcaster import MessageBroadcaster

TEST_MODE = True

if conf.VPS:
    TEST_MODE = False

##------------------Блок ініціалізації-----------------##
if TEST_MODE:
    API_Token = conf.API_TOKEN_Test
else:
    API_Token = conf.TOKEN

#API_Token = '6296017322:AAHDZeFHr7738MRPMPcmMrgR34ywu_WWZaE'
ADMIN_ID = conf.ADMIN_ID
bot = Bot(token=API_Token)

logger.add("debug.txt")
# webhook settings
WEBHOOK_HOST = conf.WEBHOOK_HOST
WEBHOOK_PATH = conf.WEBHOOK_PATH
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '0.0.0.0'  # or ip 127.0.0.1
WEBAPP_PORT = 3007
bot = Bot(token=API_Token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def getstring(li: list) -> str:
    # str = f"<strong>Назва:</strong> {li['Name']}\n<strong>Опис:</strong> {li['About']}\n<strong>Адреса:</strong> {li['address']}\n"
    str = f"Назва: {li['Name']}\nОпис: {li['About']}\nАдреса: {li['address']}\n"
    if li['tel'] != "":
        #  str+=f"<strong>Тел.:</strong> {li['tel']}\n"
        str += f"Тел.: {li['tel']}\n"
    if li['work_schedule'] != "":
        grafik = f"{li['work_schedule']}".split('#')
        tempstr = ""
        for i in grafik:
            tempstr += f"{i}\n"
        # str += f"<strong>Графік:</strong> {tempstr}"
        str += f"Графік: {tempstr}"
    if li['email'] != "":
        # str += f"<a href='{li['SiteURL']}'>Сайт</a> "
        str += f"email: {li['email']}\n"
    if li['SiteURL'] != "":
        # str += f"<a href='{li['SiteURL']}'>Сайт</a> "
        str += f"Сайт: {li['SiteURL']}\n"
    if li['facebookURL'] != "":
        str += f"Facebook: {li['facebookURL']}\n"
    #   str += f"<a href='{li['FaсebookURL']}'>Facebook</a> "
    if li['InstagramURL'] != "":
        str += f"Instagram: {li['InstagramURL']}\n"
        # str += f"<a href='{li['InstagramURL']}'>Instagram</a> "

    return str

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    welcomeMessageText = '''Вас вітає ТеребовляІнфоБот.\n\nЦифровий продукт створений громадською організацією Центр цифрового розвитку громади.\n\nНаші контакти:\nngozzrg@gmail.com\n098 151 0 251\nngozzrg.terebovlia.info\n<a href='https://www.facebook.com/ngozzrg'>Facebook</a>
    '''
    await message.answer(welcomeMessageText, parse_mode="HTML")
    await message.answer('Оберіть, будь ласка, категорію👇', reply_markup=keyb_main)
    URL = "https://orxid.in.ua/InfoBot/ep/us/"
    resp = requests.get(URL, params={'userName': message.from_user.first_name, 'userID': message.from_user.id})
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")
    if resp.text == "Subs":
        await bot.send_message(1080587853, f"Новенький підписався {message.from_user.first_name}")
        logger.info(f"Новенький підписався - {message.from_user.first_name} {message.from_user.id}")

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    welcomeMessageText = '''Вас вітає ТеребовляІнфоБот.\nЦе багатофункціональний чат-бот, який відображає усі локації та об’єкти Теребовлянської громади з різноманітними функціями, які будуть удосконалюватися разом з розвитком продукту.\nДетальніше про проєкт https://orxid.in.ua/TerInfoBot/\nПроєкт соціальний, та фінансується методом спільнокошту, тобто кожен може внести кошти на розвиток ініціативи.\nЯкщо ви хочете відобразити себе у боті, заповнюйте форму https://forms.gle/wq3JqVqze5YtdMTH7 і ми надішлемо деталі.\nЯкщо вам знадобиться допомога у заповненні локації, звертайтеся:\nГО ЦЦРГ
098 151 0 251
ngozzrg@gmail.com 
ngozzrg.terebovlia.info  
@Irynamifm
Бажаємо успіхів! Разом ми сформуємо цифрову громаду!
    '''
    await message.answer(welcomeMessageText, parse_mode="HTML")

@dp.message_handler(filters.Text(startswith="Заклади харчування"))
async def foots(message: types.Message, state: FSMContext):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://media.acc.cv.ua/news/article/2020/08/16/62182/TGAyxyaM5Bh1c6pSizF2.w575.jpg",
                         caption="", reply_markup=keyb_foot)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


#@dp.message_handler(filters.Text(startswith="2Господарські"))
# async def foots(message: types.Message, state: FSMContext):
#     keyb = types.InlineKeyboardMarkup()
#
#     but_2 = types.InlineKeyboardButton(text='Господарські🧴', callback_data='команда_МагГосподарські')
#     but_3 = types.InlineKeyboardButton(text='Дитячі👧', callback_data='команда_МагДитячі')
#     but_4 = types.InlineKeyboardButton(text='Посуд🫖', callback_data='команда_МагПосуд')
#     but_5 = types.InlineKeyboardButton(text='Книги та канцелярія📚', callback_data='команда_Канцелярія')
#     but_6 = types.InlineKeyboardButton(text='Автомагазини⚙️', callback_data='команда_Автомагазини')
#     but_7 = types.InlineKeyboardButton(text='Продуктові🧀', callback_data='команда_МагПродуктові')
#     but_8 = types.InlineKeyboardButton(text='Ветеринарні🦮', callback_data='команда_МагВетиринарні')
#     but_9 = types.InlineKeyboardButton(text='Одяг та взуття👠', callback_data='команда_МагОдягТаВзуття')
#     but_10 = types.InlineKeyboardButton(text='Квіти та декор🌹', callback_data='команда_МагКвітиДекор')
#     but_11 = types.InlineKeyboardButton(text='Телефони та оргтехніка📱', callback_data='команда_ТелефониОргтехніка')
#     but_12 = types.InlineKeyboardButton(text='Універсальні магазини🛍', callback_data='команда_УніверсальніМагазини')
#     keyb.add(but_1, but_7).add(but_2, but_8).add(but_3, but_9).add(but_4, but_10).add(but_5, but_11).add(but_6, but_12)
#     # await message.answer("Даний функціонал ще в розробці!",reply_markup=keyb)
#     Url = 'https://ceha.com.ua/wp-content/uploads/2016/02/kompleksnoe-reklamnoe-oformlenie-magazinov-supermarketov.jpg'
#     await bot.send_photo(chat_id=message.chat.id, photo=Url, caption="", reply_markup=keyb)
#     logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Господарські"))
async def foots(message: types.Message, state: FSMContext):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Для ремонту🛠', callback_data='команда_ДляРемонту')
    but_2 = types.InlineKeyboardButton(text='Побутова хімія, косметика💄', callback_data='команда_ПобутоваХімія')
    but_3 = types.InlineKeyboardButton(text='Меблі🛏', callback_data='команда_Меблі')
    but_4 = types.InlineKeyboardButton(text='Посуд, скло🫖', callback_data='команда_МагПосуд')
    but_5 = types.InlineKeyboardButton(text='Сантехніка🚿', callback_data='команда_Сантехніка')
    but_7 = types.InlineKeyboardButton(text='Дім, сад, город', callback_data='команда_ДімСадГород')
    but_8 = types.InlineKeyboardButton(text='Вікна, двері🚪', callback_data='команда_ВікнаДвері')
    but_9 = types.InlineKeyboardButton(text='Ветеринарні магазини🐶', callback_data='команда_МагВетеринарні')
    keyb.add(but_1, but_2).add(but_3, but_4).add(but_5, but_9).add(but_7, but_8)
    # await message.answer("Даний функціонал ще в розробці!",reply_markup=keyb)
    Url = 'https://profmarket.com.ua/wp-content/uploads/2021/08/Shopping-stores-Slide-3-Profmarket.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=Url, caption="", reply_markup=keyb)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Одяг та інше"))
async def foots(message: types.Message, state: FSMContext):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Одяг та взуття👖', callback_data='команда_МагОдягТаВзуття')
    but_2 = types.InlineKeyboardButton(text='Сумки та аксесуари👜', callback_data='команда_СумкиАксесуари')
    but_3 = types.InlineKeyboardButton(text='Дитячий одяг, іграшки', callback_data='команда_МагДитячі')
    but_4 = types.InlineKeyboardButton(text='Вживаний одяг', callback_data='команда_ВживанийОдяг')
    but_5 = types.InlineKeyboardButton(text='Штори, тюлі та інше', callback_data='команда_ШториТюлі')
    but_6 = types.InlineKeyboardButton(text='Оптика👓', callback_data='команда_Оптика')
    keyb.add(but_1).add(but_2).add(but_3).add(but_4).add(but_5).add(but_6)
    # await message.answer("Даний функціонал ще в розробці!",reply_markup=keyb)
    Url = 'https://109.te.ua/firms/photos/13754/3_1.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=Url, caption="", reply_markup=keyb)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")



@dp.message_handler(filters.Text(startswith="Продуктові"))
async def foots(message: types.Message):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Супермаркети🛒', callback_data='команда_Супермаркети')
    but_2 = types.InlineKeyboardButton(text='Звичайні', callback_data='команда_МагЗвичайні')
    but_3 = types.InlineKeyboardButton(text='Овочі, фрукти🍎', callback_data='команда_ОвочіФрукти')
    but_4 = types.InlineKeyboardButton(text='Дитяче харчування', callback_data='команда_ДитячеХарчування')
    keyb.add(but_1).add(but_2).add(but_3).add(but_4)
    # await message.answer("Даний функціонал ще в розробці",reply_markup=keyb)
    url = 'https://galas.te.ua/wp-content/uploads/2017/04/543.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Квіти, декор, золото"))
async def foots(message: types.Message):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Квіти та флористика🌷', callback_data='команда_МагКвітиДекор')
    but_2 = types.InlineKeyboardButton(text='Декор', callback_data='команда_Декор')
    but_3 = types.InlineKeyboardButton(text='Подарунки', callback_data='команда_Подарунки')
    but_4 = types.InlineKeyboardButton(text='Золото💍', callback_data='команда_Золото')
    keyb.add(but_1).add(but_2).add(but_3).add(but_4)
    # await message.answer("Даний функціонал ще в розробці",reply_markup=keyb)
    url = 'https://img.ukr.bio/data/articles/av/5222.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Техніка, канцелярія"))
async def foots(message: types.Message):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Телефони та аксесуари📱', callback_data='команда_Телефони')
    but_2 = types.InlineKeyboardButton(text='Побутова техніка📺', callback_data='команда_ПобутоваТехніка')
    but_3 = types.InlineKeyboardButton(text='Оргтехніка🖥', callback_data='команда_ОргТехніка')
    but_4 = types.InlineKeyboardButton(text='Канцелярія, книги📔', callback_data='команда_Канцелярія')
    keyb.add(but_1).add(but_2).add(but_3).add(but_4)
    # await message.answer("Даний функціонал ще в розробці",reply_markup=keyb)
    url = 'https://imex.kr.ua/wp-content/uploads/2017/03/shop.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Авто, вело"))
async def foots(message: types.Message):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Автозапчастини🛞', callback_data='команда_Автомагазини')
    but_2 = types.InlineKeyboardButton(text='Продаж авто🚗', callback_data='команда_ПродажАвто')
    but_3 = types.InlineKeyboardButton(text='Сільська техніка, велосипеди🚜', callback_data='команда_СільськаВелосипеди')
    keyb.add(but_1).add(but_2).add(but_3)
    # await message.answer("Даний функціонал ще в розробці",reply_markup=keyb)
    url = 'https://www.mukachevo.net/Content/img/news/870/p_870604_2_slidertop2.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Універсальні магазини"))
async def foots(message: types.Message):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Торгові центри🏢', callback_data='команда_ТорговіЦентри')
    but_2 = types.InlineKeyboardButton(text='Алкоголь, тютюн', callback_data='команда_АлкогольТютюн')
    but_3 = types.InlineKeyboardButton(text='Різні магазини', callback_data='команда_Універсальнімагазини')
    keyb.add(but_1).add(but_2).add(but_3)
    # await message.answer("Даний функціонал ще в розробці",reply_markup=keyb)
    url = 'https://gullivercenter.com/img/home-shop.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Краса і здоров'я👗"))
async def foots(message: types.Message, state: FSMContext):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://inventure.com.ua/img/thumb.990.660/upload/pic2020-1q/HairSalon-girl-pic.jpg",
                         caption="", reply_markup=keyb_kz)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


# @dp.message_handler(filters.Text(startswith="Магазини"))
# async def foots(message: types.Message):
#     await message.answer("Даний функціонал ще в розробці.")
#     logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="Послуги"))
async def foots(message: types.Message, state: FSMContext):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Ательє✂️', callback_data='команда_Ательє')
    but_2 = types.InlineKeyboardButton(text='Ремонт авто🔧', callback_data='команда_РемонтАвто')
    but_3 = types.InlineKeyboardButton(text='Ремонт техніки🪛', callback_data='команда_РемонтТехніки')
    but_4 = types.InlineKeyboardButton(text='Юридичні послуги', callback_data='команда_Нотаріуси')
    but_5 = types.InlineKeyboardButton(text='Відпочинок та дитяче дозвілля', callback_data='команда_ДитячеДозвілля')
    but_6 = types.InlineKeyboardButton(text='Інтернет-провайдери', callback_data='команда_ІнтернетПровайдери')
    but_7 = types.InlineKeyboardButton(text='Поліграфія та студія дизайну', callback_data='команда_ПоліграфіяДизайн')
    but_8 = types.InlineKeyboardButton(text='Доставка', callback_data='команда_Доставка')
    but_9 = types.InlineKeyboardButton(text='Заправки, автомийки🚗', callback_data='команда_ЗаправкиАвтомийки')
    but_10 = types.InlineKeyboardButton(text='Будівельні роботи👷‍♂️', callback_data='команда_БудівельніРоботи')
    but_11 = types.InlineKeyboardButton(text='Ритуальні послуги', callback_data='команда_РитуальніПослуги')
    but_12 = types.InlineKeyboardButton(text='Освітні послуги', callback_data='команда_ОсвітніПослуги')
    but_13 = types.InlineKeyboardButton(text='Фото, відео послуги📹', callback_data='команда_ФотоВідео')
    but_14 = types.InlineKeyboardButton(text='Різне', callback_data='команда_Різне')
    keyb.add(but_1).add(but_2, but_4).add(but_3, but_8).add(but_5).add(but_6, but_9).add(but_7).add(but_10).add(but_11,but_12).add(but_13,but_14)
    # await message.answer("Даний функціонал ще в розробці", reply_markup=keyb)
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://orxid.in.ua/TerInfBotPhoto/orx.jpg",
                         caption="", reply_markup=keyb)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="Хочеш бути тут"))
async def foots(message: types.Message, state: FSMContext):
    await message.answer("<a href='https://forms.gle/FNpJdhBPsPcQFc4c9'>Перейти за посиланням</a> щоб подати дані.\n", reply_markup=keyb_main, parse_mode="HTML")
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="ВПО"))
async def foots(message: types.Message, state: FSMContext):
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
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="Організації"))
async def foots(message: types.Message, state: FSMContext):
    await message.answer("Оберіть, будь ласка, категорію організацій👇", reply_markup=keyb_organizations)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Жителю"))
async def foots(message: types.Message, state: FSMContext):
    await message.answer("Оберіть, будь ласка, категорію👇", reply_markup=keyb_piple)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Магазини"))
async def foots(message: types.Message, state: FSMContext):
    await message.answer("Оберіть, будь ласка, категорію👇", reply_markup=keyb_shops)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="Фінансові та кредитні установи"))
async def foots(message: types.Message):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Банки💳', callback_data='команда_Банки')
    but_2 = types.InlineKeyboardButton(text='Обмін Валют💵', callback_data='команда_ОбмінВалют')
    but_3 = types.InlineKeyboardButton(text='Кредитні спілки💰', callback_data='команда_КредитніСпілки')
    but_4 = types.InlineKeyboardButton(text='Страхові', callback_data='команда_Страхові')
    keyb.add(but_1).add(but_2).add(but_3).add(but_4)
    # await message.answer("Даний функціонал ще в розробці",reply_markup=keyb)
    url = 'https://minfin.com.ua/img/2022/85137707/0988d5c75c8fe6ca4b45d900175db854.jpeg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="Громадські та благодійні організації"))
async def foots(message: types.Message, state: FSMContext):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Громадські організації🏫', callback_data='команда_Громадські_організації')
    but_2 = types.InlineKeyboardButton(text='Благодійні організації', callback_data='команда_Благодійні_організації')
    but_3 = types.InlineKeyboardButton(text='Спілки', callback_data='команда_Спілки')
    but_4 = types.InlineKeyboardButton(text='Релігійні організації', callback_data='команда_Релігійні_організації')
    keyb.add(but_1).add(but_2).add(but_3).add(but_4)
    # await message.answer("Даний функціонал ще в розробці",reply_markup=keyb)
    url = 'https://minfin.com.ua/img/2022/85137707/0988d5c75c8fe6ca4b45d900175db854.jpeg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="Міська рада"))
async def foots(message: types.Message, state: FSMContext):
    keyb_mr = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Голова громади', callback_data='команда_ГоловаГромади')
    but_2 = types.InlineKeyboardButton(text='Заступники голови', callback_data='команда_ЗаступникиГолови')
    but_3 = types.InlineKeyboardButton(text='Старостати', callback_data='команда_Старости')
    but_4 = types.InlineKeyboardButton(text='Відділи', callback_data='команда_Відділи')
    keyb_mr.add(but_1).add(but_2).add(but_3).add(but_4)
    url = 'https://orxid.in.ua/TerInfBotPhoto/RADA.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb_mr)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="Освіта"))
async def foots(message: types.Message, state: FSMContext):
    keyb_os = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Школи І ступенів', callback_data='команда_ШколиІступенів')
    but_2 = types.InlineKeyboardButton(text='Школи ІІ ступенів', callback_data='команда_ШколиІІступенів')
    but_3 = types.InlineKeyboardButton(text='Школи ІІІ ступенів', callback_data='команда_ШколиІІІступенів')
    but_4 = types.InlineKeyboardButton(text='Садочки', callback_data='команда_Садочки')
    but_5 = types.InlineKeyboardButton(text='Позашкільна освіта', callback_data='команда_ПозашкільнаОсвіта')
    keyb_os.add(but_4).add(but_1).add(but_2).add(but_3).add(but_5)
    # await message.answer("Даний функціонал ще в розробці",reply_markup=keyb_os)
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://images.unian.net/photos/2022_09/thumb_files/400_0_1664111474-8193.jpg?r=616244",
                         caption="", reply_markup=keyb_os)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="Культура"))
async def foots(message: types.Message, state: FSMContext):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='ЦКіДи', callback_data='команда_ЦКіДи')
    but_2 = types.InlineKeyboardButton(text='Музеї, садиби', callback_data='команда_МузеїСадиби')
    but_3 = types.InlineKeyboardButton(text='Бібліотеки📚', callback_data='команда_Бібліотеки')
    but_4 = types.InlineKeyboardButton(text='Туризм🏖', callback_data='команда_Туризм')
    keyb.add(but_1).add(but_2).add(but_3).add(but_4)
    url = 'https://orxid.in.ua/TerInfBotPhoto/cylture.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Важливі установи"))
async def foots(message: types.Message, state: FSMContext):
    keyb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Державні установи', callback_data='команда_Державніустанови')
    keyb.add(but_1)
    url = 'https://static.ukrinform.com/photos/2019_09/thumb_files/630_360_1567497060-680.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="Охорона здоров"))
async def foots(message: types.Message, state: FSMContext):
    keyb_oxz = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='КНП ТМР "Теребовлянська міська лікарня"🏥',
                                       callback_data='команда_міськаЛікарня')
    but_2 = types.InlineKeyboardButton(text='Сімейна медицина👨‍👩‍👧‍👦', callback_data='команда_СімейнаМедицина')
    but_3 = types.InlineKeyboardButton(text='Ветеринарія🦮', callback_data='команда_Ветеринарія')
    #   but_4 = types.InlineKeyboardButton(text='Аптеки💊', callback_data='команда_Аптеки')
    but_6 = types.InlineKeyboardButton(text='Лабораторії🩸', callback_data='команда_Лабораторії')
    keyb_oxz.add(but_2).add(but_1).add(but_3).add(but_6)
    url = 'https://orxid.in.ua/TerInfBotPhoto/ox_zd.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb_oxz)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="Інші установи"))
async def foots(message: types.Message, state: FSMContext):
    keyb_ii = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Громадські об'єднання", callback_data='команда_ГромадськіОбєднання')
    but_2 = types.InlineKeyboardButton(text='Церкви', callback_data='команда_Церкви')
    but_3 = types.InlineKeyboardButton(text='Інші', callback_data='команда_Інші')

    keyb_ii.add(but_1).add(but_2).add(but_3)
    url = 'https://orxid.in.ua/TerInfBotPhoto/inshiys.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb_ii)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


# @dp.message_handler(filters.Text(startswith="Жителю"))
# async def foots(message: types.Message, state: FSMContext):
#     keyb_ii = types.InlineKeyboardMarkup()
#     but_1 = types.InlineKeyboardButton(text='Екстрені служби🚒', callback_data='команда_ЕкстреніСлужби')
#     but_2 = types.InlineKeyboardButton(text="Зв'язок і транспорт", callback_data='команда_ЗвязокТранспорт')
#     but_3 = types.InlineKeyboardButton(text='Комунальні служби🚜', callback_data='команда_КомунальніСлужби')
#     but_4 = types.InlineKeyboardButton(text='Соціальні послуги', callback_data='команда_СоціальніПослуги')
#     but_5 = types.InlineKeyboardButton(text='Державні установи', callback_data='команда_ДержавніУстанови')
#     keyb_ii.add(but_1).add(but_2).add(but_3).add(but_4).add(but_5)
#     url = 'https://vmi957205.contaboserver.net/TerInfBotPhoto/%D0%B6%D0%B8%D1%82%D0%B5%D0%BB%D1%8E.jpg'
#     await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb_ii)
#     logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Різні служби, послуги"))
async def foot(message: types.Message, state: FSMContext):
    keyb_ii = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Екстрені служби🚒', callback_data='команда_ЕкстреніСлужби')
    #but_2 = types.InlineKeyboardButton(text="Зв'язок і транспорт", callback_data='команда_ЗвязокТранспорт')
    but_2 = types.InlineKeyboardButton(text='Комунальні служби🚜', callback_data='команда_КомунальніСлужби')
    but_3 = types.InlineKeyboardButton(text='Соціальні послуги', callback_data='команда_СоціальніПослуги')
   # but_5 = types.InlineKeyboardButton(text='Державні установи', callback_data='команда_ДержавніУстанови')
    keyb_ii.add(but_1).add(but_2).add(but_3)
    url = 'https://orxid.in.ua/TerInfBotPhoto/rizsly.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb_ii)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Зв'язок і транспорт"))
async def foots(message: types.Message, state: FSMContext):
    keyb_ii = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Вокзали', callback_data='команда_Вокзали')
    but_2 = types.InlineKeyboardButton(text='Таксі', callback_data='команда_Таксі')
    but_3 = types.InlineKeyboardButton(text='Доставка, поштові відділення', callback_data='команда_ДоставкаЖителю')
    but_4 = types.InlineKeyboardButton(text='Графік транспорту', callback_data='команда_ГрафікТранспорту')
    keyb_ii.add(but_1).add(but_2).add(but_3).add(but_4)
    url = 'https://nday.te.ua/wp-content/uploads/2018/11/46125873_1014320568769803_7150793194022633472_o.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb_ii)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Комуналка"))
async def foots(message: types.Message, state: FSMContext):
    keyb_ii = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Світло💡', callback_data='команда_Світло')
    but_2 = types.InlineKeyboardButton(text='Газ', callback_data='команда_Газ')
    but_3 = types.InlineKeyboardButton(text='Вода💦', callback_data='команда_Вода')
    but_4 = types.InlineKeyboardButton(text='Сміття', callback_data='команда_Сміття')
    keyb_ii.add(but_1).add(but_2).add(but_3).add(but_4)
    url = 'https://protocol.ua/img/news/55e31cf7fcea3943e159537e9faea609.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb_ii)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Запис до лікаря"))
async def foots(message: types.Message, state: FSMContext):
    keyb_ii = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Запис до сімейного лікаря', callback_data='команда_ЗаписСімейні')
    but_2 = types.InlineKeyboardButton(text='Запис до лікаря у лікарні', callback_data='команда_ЗаписЛікарня')
    keyb_ii.add(but_1).add(but_2)
    url = 'https://malyn-rada.gov.ua/sites/default/files/styles/social/public/catalog/66.jpg?itok=fDcBkgw0'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb_ii)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Звернення, новини"))
async def foots(message: types.Message, state: FSMContext):
    keyb_ii = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Подати звернення у міську раду', callback_data='команда_ЗверенняМР')
    but_2 = types.InlineKeyboardButton(text='Подати звернення у КП “Теребовля', callback_data='команда_ЗверненняКП')
    but_3 = types.InlineKeyboardButton(text='Подати НОВИНУ', callback_data='команда_ПодатиНовину')
    keyb_ii.add(but_1).add(but_2).add(but_3)
    url = 'https://cv.tax.gov.ua/data/material/000/387/487662/photo.png'
    await bot.send_photo(chat_id=message.chat.id, photo=url, caption="", reply_markup=keyb_ii)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")



@dp.message_handler(filters.Text(startswith="⬅️ На головну"))
async def foots(message: types.Message, state: FSMContext):
    await message.answer("Головне меню", reply_markup=keyb_main)
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="Підприємства"))
async def foots(message: types.Message, state: FSMContext):
    await message.answer("Даний функціонал ще в розробці")
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")

@dp.message_handler(filters.Text(startswith="Пошук"))
async def foots(message: types.Message, state: FSMContext):
    await message.answer("Введіть, будь ласка, у рядок повідомлення 👇 ключове слово пошуку, напр: школа, ательє, ремонт тощо")
    logger.info(f"Користувач - {message.from_user.first_name} натиснув кнопку -{message.text}")


@dp.message_handler(filters.Text(startswith="Військовим"))
async def foots(message: types.Message, state: FSMContext):
    await message.answer("Даний функціонал ще в розробці")


@dp.message_handler()
async def foots(message: types.Message, state: FSMContext):
    logger.info(f"Користувач - {message.from_user.first_name} написав -{message.text}")
    if message.text == "Файл12" and message.from_user.id in conf.ADMIN_IDS:
        doc = open('debug.txt', 'rb')
        await message.reply_document(doc)

    elif message.text == "Статистика":
        URL = "https://orxid.in.ua/InfoBot/ep/statistics/"
        resp = requests.get(URL).json()
        await message.answer(f"Локацій🏡 в боті - {resp[1]}, користувачів боту🙋 - {resp[0]}")

    elif message.text.startswith("broadcast#") and message.from_user.id in conf.ADMIN_IDS:
        req = requests.get('https://orxid.in.ua/InfoBot/ep/allid/').json()

        # for x in range(17, 499):
        #     item = req[x]
        #     await bot.send_message(chat_id=item['userTelegramID'], text="Ура! Нас уже 500🙋! І 270 локацій🏡! Запрошуємо локальний бізнес отримати місце у боті! Тисни: Хочеш бути тут?, заповнюй форму та  отримуй можливість залучити більше клієнтів! ")
        #     logger.info(f"Оповіщення надіслано користувачу {item['userTelegramID']} ")
        userLi = []

        for i in req:
            userLi.append(i['userTelegramID'])
        text = message.text.split("#")[1]
        message.text = text
       # message.text = "Ура! Нас уже більше 500🙋! Та майже 300 локацій🏡! Запрошуємо локальний бізнес отримати місце у боті! Тисни: Хочеш бути тут?, заповнюй форму та  отримуй можливість залучити більше клієнтів! "
        await MessageBroadcaster(chats=userLi, message=message, reply_markup=keyb_main).run()  # Run the broadcaster
        logger.info(f"Надіслано broadcast (повідомлення всім користувачам) - {message.text}")

    else:
        URL = "https://orxid.in.ua/InfoBot/ep/fhesh/"
        resp = requests.get(URL, params={'hash': message.text})

        if len(resp.text) > 2 and resp.status_code == requests.codes.ok:
            async with state.proxy() as data:
                data['main_list'] = resp.json()
                data['listindex'] = 0

            main_list = data['main_list']
            i = main_list[0]
            # res = f"Назва: {i['Name']}\nОпис: {i['About']}\nАдреса: {i['address']}\n\nТел.: {i['tel']}\nГрафік: {i['work_schedule']}\nСайт:{i['SiteURL']}\n                    1 із {len(main_list)}\n"
            res = f"{getstring(i)}\n1 із {len(main_list)}\n"
            try:
                await bot.send_photo(chat_id=message.chat.id, photo=i['PhotoURL'], caption=res,
                                     reply_markup=keyboard_prev_next)
            # await bot.send_message(chat_id=query.message.chat.id,text=res, reply_markup=keyboard_prev_next,parse_mode="HTML")
            except:
                print("aiogram.utils.exceptions.BadRequest: Wrong type of the web page content")
                await bot.send_message(chat_id=message.chat.id,
                                       text="помилка - aiogram.utils.exceptions.BadRequest", reply_markup=keyb_main)

        else:
            await bot.send_message(chat_id=message.chat.id, text="Нажаль ці дані відсутні, бот ще в розробці 🔧",
                                   reply_markup=keyb_main)
    # else:
    #     await message.answer("Нажаль ці дані відсутні, бот ще в розробці 🔧",reply_markup=keyb_main)


# ---------------------------------------------------------------------------------

@dp.callback_query_handler(lambda c: c.data == 'next')
async def change_image_callback(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['tmp'] = ""

    try:
        main_list = data['main_list']
        listindex = data['listindex']
    except:
        logger.debug(f"KeyErr in next listindex - {listindex} mainlist -{main_list}")

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
            async with state.proxy() as data:
                data['listindex'] = listindex
        except IndexError:
            async with state.proxy() as data:
                data['listindex'] = 0
            print(f"IndexError listindex - {listindex}")
            logger.debug(f"IndexError listindex in next- {listindex} mainlist -{main_list}")
    #     except UnboundLocalError:
    #         print(f"UnboundLocalError - {listindex}")
    #         logger.debug(f"UnboundLocalError Користувач - {query.from_user.first_name} listindex in next- {listindex}")
    # logger.info(f"Користувач - {query.from_user.first_name} перейшов далі на компанію -{i['Name']}")


@dp.callback_query_handler(lambda c: c.data == 'prev')
async def change_image_callback(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['tmp'] = ""

    try:
        main_list = data['main_list']
        listindex = data['listindex']
    except:
        logger.debug(f"KeyErr in prev listindex - {listindex} mainlist -{main_list}")

    if len(main_list) > 1:
        listindex = listindex - 1
        if listindex == -1:
            listindex = len(main_list) - 1

        try:
            i = main_list[listindex]
            # res = f"Назва: {i['Name']}\nОпис: {i['About']}\nАдреса: {i['address']}\nТел.: {i['tel']}\nГрафік: {i['work_schedule']}\nСайт:{i['SiteURL']}\n                    {listindex+1} із {len(main_list)}\n"
            res = f"{getstring(i)}{listindex + 1} із {len(main_list)}\n"

            await bot.edit_message_media(chat_id=query.message.chat.id, message_id=query.message.message_id,
                                         media=types.InputMediaPhoto(media=i['PhotoURL'], caption=res),
                                         reply_markup=keyboard_prev_next)
            async with state.proxy() as data:
                data['listindex'] = listindex
        except IndexError:
            async with state.proxy() as data:
                data['listindex'] = 0
            print(f"IndexError listindex - {listindex}")
            logger.debug(f"IndexError listindex in prev - {listindex} mainlist -{main_list}")

    logger.info(f"Користувач - {query.from_user.first_name} повернувся назад на компанію -{i['Name']}")


@dp.callback_query_handler(lambda c: c.data == 'about')
async def change_image_callback(query: types.CallbackQuery, state: FSMContext):
    global main_list, listindex
    i = main_list[listindex]
    res = f"Назва: {i['Name']}\nКатегорія: {i['category']}\nАдреса: {i['address']}\nТел.: {i['tel']}\nГрафік: {i['work_schedule']}\nСайт:{i['SiteURL']}\n               {listindex + 1} із {len(main_list)}\n"
    await bot.edit_message_media(chat_id=query.message.chat.id, message_id=query.message.message_id,
                                 media=types.InputMediaPhoto(media=i['PhotoURL'], caption=res),
                                 reply_markup=keyboard_prev_next)


# -----------------------------------------------------------------------
@dp.callback_query_handler()
async def change_image_callback(query: types.CallbackQuery, state: FSMContext):
    category = query.data.split("_")[1]  # берем стрічку типу "команда_клініки" та витягуємо із неї клініки
    print(category)
    URL = "https://orxid.in.ua/InfoBot/ep/"
    resp = requests.get(URL, params={'category': category})
    print(resp.text)
    if len(resp.text) > 2 and resp.status_code == requests.codes.ok:
        async with state.proxy() as data:
            data['main_list'] = resp.json()
            data['listindex'] = 0

        try:
            main_list = data['main_list']
            i = main_list[0]
            # res = f"Назва: {i['Name']}\nОпис: {i['About']}\nАдреса: {i['address']}\n\nТел.: {i['tel']}\nГрафік: {i['work_schedule']}\nСайт:{i['SiteURL']}\n                    1 із {len(main_list)}\n"
            res = f"{getstring(i)}\n1 із {len(main_list)}\n"
        except:
            logger.debug(f"помилка в  main_list = data['main_list'] i = main_list[0]")

        try:
            await bot.send_photo(chat_id=query.message.chat.id, photo=i['PhotoURL'], caption=res,
                                 reply_markup=keyboard_prev_next)
            # await bot.send_message(chat_id=query.message.chat.id,text=res, reply_markup=keyboard_prev_next,parse_mode="HTML")
            logger.info(f"Користувач - {query.from_user.first_name} переглянув компанію -{i['Name']}")
        except:
            logger.debug(f"помилка в користувача - {query.from_user.first_name} при перегляді компанії -{i['Name']}")


    else:
        await bot.send_message(chat_id=query.message.chat.id, text="Нажаль ці дані відсутні, бот ще в розробці 🔧",
                               reply_markup=keyb_main)


##-------------------Запуск бота-------------------------##
if TEST_MODE:
    print("Bot running")
    logger.info("Бот запущено в start_polling")
    # dp.middleware.setup(MidlWare())
    executor.start_polling(dp, skip_updates=True)
else:
    async def on_startup(dp):
        await bot.set_webhook(WEBHOOK_URL)
        logger.debug("Запуск бота")


    async def on_shutdown(dp):
        logger.debug('Зупинка бота')
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
