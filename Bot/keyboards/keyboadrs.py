from aiogram import types

keyb_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
#keyb_main.add("Організації🏘 і установи","Підприємства").add("Заклади харчування🍽","Краса і здоровя👗","Послуги🔧").add("Магазини🛍","Для ВПО👨‍👩‍👦","Військовим🪖")
#keyb_main.add("Заклади харчування🍽","Краса і здоровя👗").add("Організації🏘 та установи","Підприємства").add("Послуги🔧","Магазини🛍").add("Для ВПО👨‍👩‍👦","Військовим🪖")
keyb_main.add("Організації та установи 🏘",'Жителю👨').add("Магазини🛍","Заклади харчування🍽").add("Послуги✂️🪡","Краса і здоров'я👗").add("Пошук🔎","Хочеш бути тут❓")

keyb_organizations = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyb_organizations.add("Міська рада🏢","Освіта👩‍🎓").add("Культура","Охорона здоров’я🏥").add("Важливі установи",'Фінансові та кредитні установи').add("⬅️ На головну","Інші установи⛪️")

keyb_piple = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyb_piple.add("Різні служби, послуги🚒","Зв'язок і транспорт🚘").add("Комуналка","Запис до лікаря👩‍⚕️").add("Звернення, новини",'ВПО👨‍👩‍👦').add("⬅️ На головну","Підключити оператора👩‍💻")

keyb_shops = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyb_shops.add("Продуктові🧀","Господарські🧴").add("Одяг та інше👠","Квіти, декор, золото️💐").add("Техніка, канцелярія🗂",'Авто, вело🚴').add("⬅️ На головну","Універсальні магазини🛍")


#------------------------------------------------------------------------------------------------
keyb_foot = types.InlineKeyboardMarkup()
but_kafe = types.InlineKeyboardButton(text='Кафе 🎂', callback_data='команда_Кафе')
#but_bars = types.InlineKeyboardButton(text='Бари', callback_data='команда_Бари')
but_restorans = types.InlineKeyboardButton(text='Ресторани 🥂', callback_data='команда_Ресторани')
but_fastfoods = types.InlineKeyboardButton(text='Фастфуди 🍿', callback_data='команда_Фастфуди')
but_4  = types.InlineKeyboardButton(text='Піцерії🍕', callback_data='команда_Піцерії')
keyb_foot.add(but_kafe).add(but_restorans).add(but_fastfoods).add(but_4)

keyb_kz = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text='Клініки, лабораторії 🏥', callback_data='команда_КлінікиЛабораторії')
but_2 = types.InlineKeyboardButton(text='Салони краси💇‍♂️', callback_data='команда_СалониКраси')
but_3  = types.InlineKeyboardButton(text='Спортивні зали, фітнес🏋️‍♀️', callback_data='команда_СпортивніЗалиФітнес')
but_4 = types.InlineKeyboardButton(text='Аптеки💊', callback_data='команда_Аптеки')
but_6 = types.InlineKeyboardButton(text='Індивідуальні послуги краси', callback_data='команда_ІндивідПослугиКраси')
but_5 = types.InlineKeyboardButton(text='Стоматологічні послуги🦷', callback_data='команда_Стоматології')
keyb_kz.add(but_4).add(but_5).add(but_2).add(but_6).add(but_1).add(but_3)

keyboard_prev_next_about = types.InlineKeyboardMarkup()
button_prev = types.InlineKeyboardButton(text='⬅️ Назад', callback_data='prev')
button_next = types.InlineKeyboardButton(text='Далі ➡️', callback_data='next')
button_about = types.InlineKeyboardButton(text='Детальніше', callback_data='about')
keyboard_prev_next_about.add(button_about).add(button_prev, button_next)

keyboard_prev_next = types.InlineKeyboardMarkup()
button_prev2 = types.InlineKeyboardButton(text='⬅️ Назад', callback_data='prev')
button_next2 = types.InlineKeyboardButton(text='Далі ➡️', callback_data='next')
keyboard_prev_next.add(button_prev2, button_next2)