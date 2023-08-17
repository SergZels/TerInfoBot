from aiogram import types

keyb_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
#keyb_main.add("Організації🏘 і установи","Підприємства").add("Заклади харчування🍽","Краса і здоровя👗","Послуги🔧").add("Магазини🛍","Для ВПО👨‍👩‍👦","Військовим🪖")
#keyb_main.add("Заклади харчування🍽","Краса і здоровя👗").add("Організації🏘 та установи","Підприємства").add("Послуги🔧","Магазини🛍").add("Для ВПО👨‍👩‍👦","Військовим🪖")
keyb_main.add("Організації та установи 🏘","Магазини🛍").add("Заклади харчування🍽","Послуги🔧").add("Підприємства🏭","Краса і здоров'я👗").add("Фінансові та кредитні установи🏦","Хочеш бути тут❓")

keyb_organizations = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyb_organizations.add("Міська рада🏢","Освіта👩‍🎓").add("Культура","Охорона здоров’я🏥").add("Жителю👨","Інші установи⛪️").add("⬅️ На головну",'ВПО👨‍👩‍👧‍👦')

#------------------------------------------------------------------------------------------------
keyb_foot = types.InlineKeyboardMarkup()
but_kafe = types.InlineKeyboardButton(text='Кафе 🎂', callback_data='команда_Кафе')
#but_bars = types.InlineKeyboardButton(text='Бари', callback_data='команда_Бари')
but_restorans = types.InlineKeyboardButton(text='Ресторани 🥂', callback_data='команда_Ресторани')
but_fastfoods = types.InlineKeyboardButton(text='Фастфуди 🍿', callback_data='команда_Фастфуди')
but_4  = types.InlineKeyboardButton(text='Піцерії', callback_data='команда_Піцерії')
keyb_foot.add(but_kafe).add(but_restorans).add(but_fastfoods).add(but_4)

keyb_kz = types.InlineKeyboardMarkup()
butkz1 = types.InlineKeyboardButton(text='Клініки 🏥', callback_data='команда_Клініки')
butkz2 = types.InlineKeyboardButton(text='Салони краси💇‍♂️', callback_data='команда_СалониКраси')
butkz3 = types.InlineKeyboardButton(text='Спортивні зали, фітнес🏋️‍♀️', callback_data='команда_СпортивніЗалиФітнес')
keyb_kz.add(butkz2).add(butkz1).add(butkz3)

keyboard_prev_next_about = types.InlineKeyboardMarkup()
button_prev = types.InlineKeyboardButton(text='⬅️ Назад', callback_data='prev')
button_next = types.InlineKeyboardButton(text='Далі ➡️', callback_data='next')
button_about = types.InlineKeyboardButton(text='Детальніше', callback_data='about')
keyboard_prev_next_about.add(button_about).add(button_prev, button_next)

keyboard_prev_next = types.InlineKeyboardMarkup()
button_prev2 = types.InlineKeyboardButton(text='⬅️ Назад', callback_data='prev')
button_next2 = types.InlineKeyboardButton(text='Далі ➡️', callback_data='next')
keyboard_prev_next.add(button_prev2, button_next2)