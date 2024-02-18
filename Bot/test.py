import requests, json
#
# resp = requests.get('http://127.0.0.1:8000/ep', params={'category': 'shop1'})
# data = resp.json()
# print(resp.text)
# print(len(resp.text)>2)
#
# for i in data:
#     res = f"Company: {i['Name']}\nAddress: {i['address']}\nTel {['tel']}\nSite {i['SiteURL']}\n\n"
#     print(res)
# '''''''
# {"id": "4641089489170786537",
#  "from":
#      {"id": 1080587853,
#       "is_bot": false,
#       "first_name": "Sergey",
#       "language_code": "uk"},
# "message":
#      {"message_id": 2910,
#       "from": {"id": 5569216235,
#                "is_bot": true,
#                "first_name": "Айограм тест бот",
#                "username": "orxid_aio_test_bot"},
#       "chat": {"id": 1080587853, "first_name": "Sergey",
#                "type": "private"},
#       "date": 1685703618,
#       "text": "Ось заклади.....",
#       "reply_markup":
#           {"inline_keyboard":
#                [[{"text": "Аптеки💊", "callback_data": "команда_аптеки"}],
#                 [{"text": "Ательє✂️", "callback_data": "команда_ательє"}],
#                 [{"text": "Клініки🏥", "callback_data": "команда_клініки"}],
#                 [{"text": "Салони краси", "callback_data": "команда_салони_краси"}],
#                 [{"text": "Спортзали", "callback_data": "команда_спортзали"}]]}},
#  "chat_instance": "4829572988527275952",
#  "data": "команда_ательє"}
#
# ''''''''
# lis = [3,0,6,1,5]
# lis.sort(reverse=True)
#
# lenght = len(lis)
# print(lis)
# num = lenght
# for i in range(lenght):
#     for k in range(i+1):
#         for j in lis:
#             if j>i:
#                 index = j
#                 break
# URL = "https://orxid.in.ua/InfoBot/ep/statistics/"
# resp = requests.get(URL).json()
# print(f"Локацій🏡 в боті - {resp[1]}, користувачів боту🙋 - {resp[0]}")

URL = "https://orxid.in.ua/InfoBot/ep/"
resp = requests.get(URL, params={'category': 'ДорожняКартаВПО'})
print(resp.text)