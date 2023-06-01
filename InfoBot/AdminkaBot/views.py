from django.shortcuts import render
import  json
from django.core import serializers
# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import BotDataBase


def index(request):
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


