from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import BotDataBase, UsersStatistic
from .forms import ClientForm
from django.contrib.auth.decorators import login_required
import subprocess
import requests
from django.db import connection
import csv
@login_required
def export_to_csv(request):
   # table_name = BotDataBase._meta.db_table
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM \"AdminkaBot_botdatabase2\"')
        rows = cursor.fetchall()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    writer.writerow([i[0] for i in cursor.description])  # Write column headers
    writer.writerows(rows)

    return response



def clientForm(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "InfoBot/ClientFormSucsses.html")
    else:
        form = ClientForm()
    return render(request, "InfoBot/ClientForm.html",{'form':form})

def index1(request):
    db = BotDataBase.objects.all()

    response = ""
    for user in db:
        response += f"Company: {user.Name}\nCategory {user.category}\nAddress: {user.address}\nTel {user.tel}\nSite {user.SiteURL}\n\n"
    print(response)

    return HttpResponse(response)

# def temp(request):
#     db = BotDataBase.objects.all()
#     response=''
#     for obj in db:
#         if obj.PhotoURL=='https://orxid.in.ua/TerInfBotPhoto/TM.jpg':
#             response+=f'Photo {obj.Name}<br>'
#             obj.PhotoURL = 'https://orxid.in.ua/TerInfBotPhoto/Standart.jpg'
#             obj.save()
#
#     return HttpResponse(response)


def index2(request):
    queryset = BotDataBase.objects.all()
    data = list(queryset.values())
    #json_data = json.dumps(data)
    #serialized_data = serializers.serialize('json', queryset)
    return JsonResponse(data, safe=False)


def index(request):
    param_value = request.GET.get('category')
    queryset = BotDataBase.objects.filter(category=param_value,isPublished = True).order_by('sequence')
    data = list(queryset.values())
    return JsonResponse(data, safe=False)

def userstatistic(request):
    subs = False
    userName = request.GET.get('userName')
    userID = request.GET.get('userID')
    try:
        existing_user = UsersStatistic.objects.get(userTelegramID=userID)
    except UsersStatistic.DoesNotExist:
        # Якщо такого користувача з таким userID ще немає, то додайте його в базу
        obj = UsersStatistic(userName=userName, userTelegramID=userID)
        obj.save()
        subs = "Subs"
    return HttpResponse(subs)

def foohash(request):
    param_value = request.GET.get('hash')
    queryset = BotDataBase.objects.filter(heshTeg__icontains=param_value,isPublished = True)
    data = list(queryset.values())
    return JsonResponse(data, safe=False)

def get_all_users_telegram_id(request):
    queryset = UsersStatistic.objects.all()
    data = list(queryset.values())
    return JsonResponse(data, safe=False)

def statistic(request):
    queryset = UsersStatistic.objects.all()
    records = BotDataBase.objects.all()
    data = list((len(queryset),len(records)))
    return JsonResponse(data, safe=False)

def findForm(request):
    param_value = request.POST.get('text')
    if param_value == None: param_value = "Орхід"
    records = BotDataBase.objects.filter(heshTeg__icontains=param_value,isPublished = True)
    return render(request, "InfoBot/index.html", {'DB': records})

def location(request,id):
    records = BotDataBase.objects.filter(pk=id,isPublished = True).last()
    records.work_schedule=records.work_schedule.replace("#", " ")
    return render(request, "InfoBot/locationBootstrap.html", {'Loc': records})

def locationHextegs(request,id):
    records = BotDataBase.objects.filter(pk=id).last()
    if records:
        return HttpResponse(f'{records.heshTeg}')
    else:
        return HttpResponse('Локація відсутня')

@login_required
def broadcast(request):
    text = request.POST.get('text')

    message = "Напишіть текст повідомлення!"
    if text:
        try:
            msg = {"update_id": 443776903, "message": {"message_id": 7852, "from": {"id": 1080587853, "is_bot": False,
                                                                                    "first_name": "Sergey",
                                                                                    "language_code": "uk"},
                                                       "chat": {"id": 1080587853, "first_name": "Sergey",
                                                                "type": "private"}, "date": 1693751446,
                                                       "text": f"broadcast#{text}"}}

            URL = "https://zelse.asuscomm.com/prod_terinfobot"
            resp = requests.post(url=URL, json=msg)

            message= f"Повідомлення надіслано. Відповідь сервера -{resp} "
        except subprocess.CalledProcessError as e:
            message= f"Помилка {str(e)}"
    return render(request, "InfoBot/broadcast.html", {'message': message})