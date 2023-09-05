from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("2/", views.index2, name="index2"),
    path("1/", views.index1, name="index1"),
    path("us/", views.userstatistic, name="us"),
    path("fhesh/", views.foohash, name="fhash"),
    path('allid/', views.get_all_users_telegram_id, name='id'),
    path('statistics/', views.statistic, name='statistic'),
    path("company/", views.findForm, name="company"),
    path("bro/", views.broadcast, name="bro"),

]