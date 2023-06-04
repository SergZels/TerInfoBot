from aiogram import types

keyb_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyb_main.add("Заклади харчування🍽","Краса і здоровя👗💄").add("Магазини🛍","Послуги🔧").add("Організації🏘","Цікаві місця🏞")


keyb_foot = types.InlineKeyboardMarkup()
but_kafe = types.InlineKeyboardButton(text='Кафе 🎂', callback_data='команда_Кафе')
but_bars = types.InlineKeyboardButton(text='Бари', callback_data='команда_Бари')
but_clubs = types.InlineKeyboardButton(text='Клуби', callback_data='команда_Клуби')
but_restorans = types.InlineKeyboardButton(text='Ресторани 🥂', callback_data='команда_Ресторани')
but_fastfoods = types.InlineKeyboardButton(text='Фастфуди 🍿', callback_data='команда_Фастфуди')
keyb_foot.add(but_kafe).add(but_bars).add(but_clubs).add(but_restorans).add(but_fastfoods)

keyb_kz = types.InlineKeyboardMarkup()
butkz1 = types.InlineKeyboardButton(text='Аптеки 💊', callback_data='команда_Аптеки')
butkz2 = types.InlineKeyboardButton(text='Ательє ✂ ', callback_data='команда_Ательє')
butkz3 = types.InlineKeyboardButton(text='Клініки 🏥', callback_data='команда_Клініки')
butkz4 = types.InlineKeyboardButton(text='Салони краси', callback_data='команда_Салони_краси')
butkz5 = types.InlineKeyboardButton(text='Спортзали', callback_data='команда_Спортзали')
keyb_kz.add(butkz1).add(butkz2).add(butkz3).add(butkz4).add(butkz5)

keyboard_prev_next = types.InlineKeyboardMarkup()
button_prev = types.InlineKeyboardButton(text='⬅️ Назад', callback_data='prev')
button_next = types.InlineKeyboardButton(text='Далі ➡️', callback_data='next')
keyboard_prev_next.add(button_prev, button_next)