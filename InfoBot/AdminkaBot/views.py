from django.shortcuts import render
import  json
from django.core import serializers
# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import BotDataBase, UsersStatistic


def index1(request):
    db = BotDataBase.objects.all()

    response = ""
    for user in db:
        response += f"Company: {user.Name}\nCategory {user.category}\nAddress: {user.address}\nTel {user.tel}\nSite {user.SiteURL}\n\n"
    print(response)

    return HttpResponse(response)

def index2(request):
    queryset = BotDataBase.objects.all()
    data = list(queryset.values())
    #json_data = json.dumps(data)
    #serialized_data = serializers.serialize('json', queryset)
    return JsonResponse(data, safe=False)


def index(request):
    param_value = request.GET.get('category')
    queryset = BotDataBase.objects.filter(category=param_value).order_by('sequence')
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