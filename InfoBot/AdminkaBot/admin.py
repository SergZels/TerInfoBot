from django.contrib.auth.models import User, Group
from django.contrib import admin
from .models import BotDataBase, UsersStatistic


class BotDataBaseAdmin(admin.ModelAdmin):
    exclude = ('PhotoURL',)
    readonly_fields = ["img_preview"]
    list_display = ("Name", "category","sequence", "town","work_schedule","tel",'heshTeg')
    search_fields = ['Name',"town", "category"]
    list_editable = ('sequence','heshTeg')


class UsersStatisticAdmin(admin.ModelAdmin):
    list_display = ("userName", "dateOfRegistration")
    list_filter = ("dateOfRegistration",)

admin.site.register(BotDataBase, BotDataBaseAdmin)
admin.site.register(UsersStatistic, UsersStatisticAdmin)

admin.site.site_header = "Адміністрування Теребовля Інфо"
admin.site.site_title = "TerInfoBot адміністрування"
admin.site.index_title = "Вітаємо в адмінці чат бота"

admin.site.unregister(User)
admin.site.unregister(Group)