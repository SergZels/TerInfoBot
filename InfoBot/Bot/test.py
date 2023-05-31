from ..models import BotDataBase

db = BotDataBase.objects.all()

response = ""
for user in db:
    response += f"ID: {user.address}, Ім'я: {user.tel}\n"

print(response)