from django.contrib.auth.models import User, Group

# Register your models here.
from django.contrib import admin

from .models import BotDataBase


class BotDataBaseAdmin(admin.ModelAdmin):
    exclude = ('PhotoURL',)
    readonly_fields = ["img_preview"]
    list_display = ("Name", "category", "town")

admin.site.register(BotDataBase, BotDataBaseAdmin)

admin.site.site_header = "Адміністрування Теребовля Інфо"
admin.site.site_title = "TerInfoBot адміністрування"
admin.site.index_title = "Вітаємо в адмінці чат бота"

admin.site.unregister(User)
admin.site.unregister(Group)