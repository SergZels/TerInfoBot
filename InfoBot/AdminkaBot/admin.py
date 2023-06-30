

# Register your models here.
from django.contrib import admin

from .models import BotDataBase


class BotDataBaseAdmin(admin.ModelAdmin):
    exclude = ('PhotoURL',)

admin.site.register(BotDataBase, BotDataBaseAdmin)