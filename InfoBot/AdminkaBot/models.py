from django.db import models
from django.utils.html import mark_safe
from django.utils import timezone

# Create your models here.
class BotDataBase(models.Model):
    catlist = [('ГоловаГромади','ГоловаГромади'),('ЗаступникиГолови','ЗаступникиГолови'),
               ('Старости','Старости'),('Відділи','Відділи'),
               ('Ательє', 'Ательє'),
               ('Кафе','Кафе'),('Клуби','Клуби'),('Ресторани','Ресторани'),
               ('Фастфуди','Фастфуди'),('Піцерії','Піцерії'),
               ('Спортзали','Спортзали'),('Банки','Банки'),('ОбмінВалют','ОбмінВалют'),(' Страхові',' Страхові'),
               ('КредитніСпілки','КредитніСпілки'),('РемонтАвто','РемонтАвто'),('РемонтТехніки','РемонтТехніки'),
               ('Нотаріуси','Нотаріуси'),('ДитячеДозвілля','ДитячеДозвілля'),('ЗаправкиАвтомийки','ЗаправкиАвтомийки'),('Доставка','Доставка'),('БудівельніРоботи','БудівельніРоботи'),
               ('МагПродуктові','МагПродуктові'),('Супермаркети','Супермаркети'),('МагДитячі','МагДитячі'),('МагГосподарські','МагГосподарські'),
               ('МагОдягТаВзуття','МагОдягТаВзуття'),('МагВетиринарні','МагВетиринарні'),
               ('МагПосуд','МагПосуд'),('ТелефониОргтехніка','ТелефониОргтехніка'),('УніверсальніМагазини','УніверсальніМагазини'),('МагКвітиДекор','МагКвітиДекор'),
               ('Автомагазини','Автомагазини'),('Канцелярія','Канцелярія'),('КлінікиЛабораторії','КлінікиЛабораторії'),
               ('СалониКраси','СалониКраси'),('СпортивніЗалиФітнес','СпортивніЗалиФітнес'),
               ('ШколиІступенів','ШколиІступенів'),
               ('ШколиІІступенів','ШколиІІступенів'),
               ('ШколиІІІступенів','ШколиІІІступенів'),('Садочки','Садочки'),('ПозашкільнаОсвіта','ПозашкільнаОсвіта'),
               ('ЦКіДи','ЦКіДи'),('МузеїСадиби','МузеїСадиби'),('Бібліотеки','Бібліотеки'),('Туризм','Туризм'),
               ('міськаЛікарня','міськаЛікарня'),('СімейнаМедицина','СімейнаМедицина'),('Ветеринарія','Ветеринарія'),
               ('Аптеки','Аптеки'),('Стоматології','Стоматології'),('Лабораторії','Лабораторії'),('ГромадськіОбєднання','ГромадськіОбєднання'),('Церкви','Церкви'),
               ('Інші','Інші'),('ЕкстреніСлужби','ЕкстреніСлужби'),
               ('ЗвязокТранспорт','ЗвязокТранспорт'),('КомунальніСлужби','КомунальніСлужби'),('СоціальніПослуги','СоціальніПослуги'),('ДержавніУстанови','ДержавніУстанови'),
               ('ІнтернетПровайдери','ІнтернетПровайдери'),('ПоліграфіяДизайн','ПоліграфіяДизайн')
               ]

    Photo = models.ImageField(verbose_name="Фото", upload_to="photo/", default="")
    PhotoURL = models.URLField(verbose_name="Url зсилка фото", max_length=200)
    Name = models.CharField(verbose_name="Назва", max_length=200)
    About = models.CharField(verbose_name="Опис", max_length=400, default="")
    town = models.CharField(verbose_name="Місто", max_length=200, default="Теребовля")
    category = models.CharField(verbose_name="Категорія", max_length=300, choices=catlist)
    #sequence = models.CharField(verbose_name="Послідовність", blank=True, default=0)# рейтинг
    sequence = models.IntegerField(verbose_name="Послідовність", blank=True, default=0)  # рейтинг
    address = models.CharField(verbose_name="Адреса", max_length=300)
    tel = models.CharField(verbose_name="Телефон", max_length=100, blank=True)
    work_schedule = models.CharField(verbose_name="Робочий графік", max_length=100, blank=True)
    email = models.EmailField(verbose_name="e-mail", max_length= 250, default="",blank=True)
    SiteURL = models.URLField(verbose_name="Сайт", max_length=300, blank=True)
    FaсebookURL = models.URLField(verbose_name="Фейсбук", max_length=300, default="", blank=True)
    InstagramURL = models.URLField(verbose_name="Інстаграм", max_length=300, default="", blank=True)
    coordinates = models.CharField(verbose_name="Кординати", max_length=300, default="", blank=True)
    heshTeg = models.CharField(verbose_name="Хештеги", max_length=500, default="", blank=True)

    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.PhotoURL}" width = "300"/>')

    def save(self, *args, **kwargs):
        # Перевіряємо, чи є фото
        if self.Photo:
            # Зберігаємо фото
            super().save(*args, **kwargs)
            # Отримуємо ім'я файлу
            filename = str(self.Photo.name)
            filename = filename.split("/")[1]
            # Оновлюємо поле PhotoURL
            self.PhotoURL = f"https://vmi957205.contaboserver.net/TerInfBotPhoto/{filename}"
            # Зберігаємо модель з оновленим PhotoURL
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Компанії'
        verbose_name = 'Компанії'

    def __str__(self):
        return self.Name


class UsersStatistic(models.Model):
    userName = models.CharField(verbose_name="Імя користувача", max_length=200)
    userTelegramID = models.CharField(verbose_name="Telegram ID", max_length=200)
    dateOfRegistration = models.DateField(verbose_name="Дата реестрації", default=timezone.now)

    def __str__(self):
        return self.userName

    class Meta:
        verbose_name_plural = 'Статистика користувачів'
        verbose_name = 'Статистика користувачів'

