from django.contrib.auth.models import User, Group
from django.contrib import admin
from .models import BotDataBase, UsersStatistic


class BotDataBaseAdmin(admin.ModelAdmin):
    change_list_template = "InfoBot/locationsLINK.html"
    save_on_top = True
    #exclude = ('PhotoURL',)
    readonly_fields = ["img_preview",'location']
    list_display = ("Name","category","sequence", "town","work_schedule","tel",'heshTeg','isPublished')
    search_fields = ['Name',"town", "category"]
    list_editable = ( 'sequence','heshTeg')


class UsersStatisticAdmin(admin.ModelAdmin):
    list_display = ("userName", "dateOfRegistration")
    list_filter = ("dateOfRegistration",)
    date_hierarchy = 'dateOfRegistration'

admin.site.register(BotDataBase, BotDataBaseAdmin)
admin.site.register(UsersStatistic, UsersStatisticAdmin)

admin.site.site_header = "Адміністрування Теребовля Інфо"
admin.site.site_title = "TerInfoBot адміністрування"
admin.site.index_title = "Вітаємо в адмінці чат бота"

#admin.site.unregister(User)
#admin.site.unregister(Group)