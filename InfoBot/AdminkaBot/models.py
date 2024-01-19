from django.db import models
from django.utils.html import mark_safe
from django.utils import timezone

# Create your models here.
class BotDataBase(models.Model):
    catlist = [('ГоловаГромади','ГоловаГромади'),('ЗаступникиГолови','ЗаступникиГолови'),
               ('Старости','Старости'),('Відділи','Відділи'),('Державніустанови','Державніустанови'),
               ('Ательє', 'Ательє'),
               ('Кафе','Кафе'),('Ресторани','Ресторани'),
               ('Фастфуди','Фастфуди'),('Піцерії','Піцерії'),
               ('Банки','Банки'),('ОбмінВалют','ОбмінВалют'),('Страхові','Страхові'),
               ('КредитніСпілки','КредитніСпілки'),('РемонтАвто','РемонтАвто'),('РемонтТехніки','РемонтТехніки'),
               ('Нотаріуси','Нотаріуси'),('ДитячеДозвілля','ДитячеДозвілля'),('ЗаправкиАвтомийки','ЗаправкиАвтомийки'),('Доставка','Доставка'),('БудівельніРоботи','БудівельніРоботи'),
               ('Супермаркети','Супермаркети'),('Різне','Різне'),('ОсвітніПослуги','ОсвітніПослуги'),('РитуальніПослуги','РитуальніПослуги'),('ФотоВідео','ФотоВідео'),
               ('МагВетиринарні','МагВетиринарні'),
               ('МагПосуд','МагПосуд'),('УніверсальніМагазини','УніверсальніМагазини'),('МагРізні','МагРізні'),
               ('Автомагазини','Автомагазини'),('Канцелярія','Канцелярія'),('КлінікиЛабораторії','КлінікиЛабораторії'),
               ('СалониКраси','СалониКраси'),('СпортивніЗалиФітнес','СпортивніЗалиФітнес'),('ІндивідПослугиКраси','ІндивідПослугиКраси'),
               ('ШколиІступенів','ШколиІступенів'),
               ('ШколиІІступенів','ШколиІІступенів'),
               ('ШколиІІІступенів','ШколиІІІступенів'),('Садочки','Садочки'),('ПозашкільнаОсвіта','ПозашкільнаОсвіта'),
               ('ЦКіДи','ЦКіДи'),('МузеїСадиби','МузеїСадиби'),('Бібліотеки','Бібліотеки'),('Туризм','Туризм'),
               ('міськаЛікарня','міськаЛікарня'),('СімейнаМедицина','СімейнаМедицина'),('Ветеринарія','Ветеринарія'),
               ('Аптеки','Аптеки'),('Стоматології','Стоматології'),('Лабораторії','Лабораторії'),('ГромадськіОбєднання','ГромадськіОбєднання'),('Церкви','Церкви'),
               ('Інші','Інші'),('ЕкстреніСлужби','ЕкстреніСлужби'),('Вокзали','Вокзали'),('Таксі','Таксі'),('ДоставкаЖителю','ДоставкаЖителю'),('ГрафікТранспорту','ГрафікТранспорту'),
               ("Світло","Світло"),("Газ","Газ"),("Вода","Вода"),("Сміття","Сміття"),("ЗаписСімейні","ЗаписСімейні"),("ЗаписЛікарня","ЗаписЛікарня"),
               ('ЗверенняМР','ЗверенняМР'),('ЗверненняКП','ЗверненняКП'),('ПодатиНовину','ПодатиНовину'),('МагЗвичайні','МагЗвичайні'),('ОвочіФрукти','ОвочіФрукти'),
               ('ДитячеХарчування','ДитячеХарчування'),('ДляРемонту','ДляРемонту'),('ПобутоваХімія','ПобутоваХімія'),('Меблі','Меблі'),('Сантехніка','Сантехніка'),('ДімСадГород','ДімСадГород'),
               ('ВікнаДвері','ВікнаДвері'),('МагВетеринарні','МагВетеринарні'),
               ('МагОдягТаВзуття','МагОдягТаВзуття'),('СумкиАксесуари','СумкиАксесуари'),('МагДитячі','МагДитячі'),('ШториТюлі','ШториТюлі'),('Оптика','Оптика'),
               ('МагКвітиДекор','МагКвітиДекор'),('Декор','Декор'),('Подарунки','Подарунки'),('Золото','Золото'),('Телефони','Телефони'),('ПобутоваТехніка','ПобутоваТехніка'),('ОргТехніка','ОргТехніка'),
               ('ПродажАвто','ПродажАвто'),('СільськаВелосипеди','СільськаВелосипеди'),('ТорговіЦентри','ТорговіЦентри'),
               ('АлкогольТютюн','АлкогольТютюн'),('Універсальнімагазини','Універсальнімагазини'),('ВживанийОдяг','ВживанийОдяг'),
               ('КомунальніСлужби','КомунальніСлужби'),('СоціальніПослуги','СоціальніПослуги'),('ДержавніУстанови','ДержавніУстанови'),
               ('ІнтернетПровайдери','ІнтернетПровайдери'),('ПоліграфіяДизайн','ПоліграфіяДизайн')
               ]

    Photo = models.ImageField(verbose_name="Фото", upload_to="photo/", default="")
    PhotoURL = models.URLField(verbose_name="Url зсилка фото", max_length=200, blank=True)
    Name = models.CharField(verbose_name="Назва", max_length=200)
    isStandartPicture = models.BooleanField(verbose_name="Встановити стандартне зображення",default=False)
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
        if self.isStandartPicture:
            self.PhotoURL = f"https://orxid.in.ua/TerInfBotPhoto/TM.jpg"
            print("standart picture")
        else:
            if self.Photo:
                # Зберігаємо фото
                super().save(*args, **kwargs)
                # Отримуємо ім'я файлу
                filename = str(self.Photo.name)
                filename = filename.split("/")[1]
                # Оновлюємо поле PhotoURL
                self.PhotoURL = f"https://orxid.in.ua/TerInfBotPhoto/{filename}"
                # Зберігаємо модель з оновленим PhotoURL


        super(BotDataBase,self).save(*args, **kwargs)
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

