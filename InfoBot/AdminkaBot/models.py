from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class BotDataBase(models.Model):
    catlist = [('ГоловаГромади','ГоловаГромади'),('ЗаступникиГолови','ЗаступникиГолови'),
               ('Старости','Старости'),('Відділи','Відділи'),
               ('Ательє', 'Ательє'), ('Аптеки', 'Аптеки'),
               ('Кафе','Кафе'),('Клуби','Клуби'),('Ресторани','Ресторани'),
               ('Фастфуди','Фастфуди'),('Клініки','Клініки'),('Салони_краси','Салони_краси'),('Спортзали','Спортзали'),
               ('Банки','Банки'),('Казначейство','Казначейство'),('КредитніСпілки','КредитніСпілки'),
               ('РемонтАвто','РемонтАвто'),('РемонтТехніки','РемонтТехніки'),
               ('Нотаріуси','Нотаріуси'),('ДитячеДозвілля','ДитячеДозвілля'),
               ('МагПродуктові','МагПродуктові'),('МагДитячі','МагДитячі'),('МагГосподарські','МагГосподарські'),
               ('МагОдягТаВзуття','МагОдягТаВзуття'),('МагВетиринарні','МагВетиринарні'),
               ('МагПосуд','МагПосуд'),('Телефони_оргтехніка','Телефони_оргтехніка'),('МагКвіти','МагКвіти'),('ГосподарськіМагазини','ГосподарськіМагазини'),
               ('Канцелярія','Канцелярія'),('Клініки','Клініки'),('Салони_краси','Салони_краси'),
               ('СпортивніЗалиФітнес','СпортивніЗалиФітнес'),
               ('Старости','Старости'),('Відділи','Відділи'),
               ('Школи_І_ступенів','Школи_І_ступенів'),('Школи_ІІ_ступенів','Школи_ІІ_ступенів'),
               ('Школи_ІІІ_ступенів','Школи_ІІІ_ступенів'),('Садочки','Садочки'),('Позашкільна освіта','Позашкільна освіта'),
               ('ЦКіДи','ЦКіДи'),('МузеїСадиби','МузеїСадиби'),('Бібліотеки','Бібліотеки'),('Туризм','Туризм'),
               ('міськаЛікарня','міськаЛікарня'),('Сімейна_медицина','Сімейна_медицина'),('Ветеринарія','Ветеринарія'),
               ('Аптеки','Аптеки'),('Стоматології','Стоматології'),('Лабораторії','Лабораторії'),('Укрпошта','Укрпошта'),('Суд','Суд'),
               ('РЕС','РЕС'),('Газова_служба','Газова_служба'),('Поліція','Поліція'),
               ('Пожежна','Пожежна'),('Газета_Воля','Газета_Воля'),('ЦентрЗайнятості','ЦентрЗайнятості'),
               ('Громадські_організації','Громадські_організації'),('Благодійні_організації','Благодійні_організації'),
               ('Спілки','Спілки'),('Релігійні_організації','Релігійні_організації')]

    Photo = models.ImageField(verbose_name="Фото", upload_to="photo/", default="")
    PhotoURL = models.URLField(verbose_name="Url зсилка фото", max_length=200)
    Name = models.CharField(verbose_name="Назва", max_length=200)
    About = models.CharField(verbose_name="Опис", max_length=400, default="")
    town = models.CharField(verbose_name="Місто", max_length=200, default="Теребовля")
    category = models.CharField(verbose_name="Категорія", max_length=300, choices=catlist)
    address = models.CharField(verbose_name="Адреса", max_length=300)
    tel = models.CharField(verbose_name="Телефон", max_length=100, blank=True)
    work_schedule = models.CharField(verbose_name="Робочий графік", max_length=100, blank=True)
    email = models.EmailField(verbose_name="e-mail", max_length= 250, default="",blank=True)
    SiteURL = models.URLField(verbose_name="Сайт", max_length=300, blank=True)
    FaсebookURL = models.URLField(verbose_name="Фейсбук", max_length=300, default="", blank=True)
    InstagramURL = models.URLField(verbose_name="Інстаграм", max_length=300, default="", blank=True)
    coordinates = models.CharField(verbose_name="Кординати", max_length=300, default="", blank=True)

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