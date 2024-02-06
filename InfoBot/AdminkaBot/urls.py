from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("2/", views.index2, name="index2"),
    path("1/", views.index1, name="index1"),
    path("broadcast/", views.broadcast, name="bro"),
    path("addlocation/", views.clientForm, name="addlocation"),
    path("us/", views.userstatistic, name="us"),
    path("location/<str:id>", views.location, name="location"),
    path("fhesh/", views.foohash, name="fhash"),
    path('allid/', views.get_all_users_telegram_id, name='id'),
    path('statistics/', views.statistic, name='statistic'),
    path("company/", views.findForm, name="company"),


]