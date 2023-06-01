from django.db import models

# Create your models here.
class BotDataBase(models.Model):
    PhotoURL = models.URLField(verbose_name="Url зсилка фото",max_length=200)
    Name = models.CharField(verbose_name="Назва організації",max_length=200)
    category = models.CharField(verbose_name="Категорія",max_length=200)
    address = models.CharField(verbose_name="Адреса",max_length=300)
    tel = models.CharField(verbose_name="Телефон",max_length=200)
    work_schedule = models.CharField(verbose_name="Робочий графік",max_length=200)
    SiteURL = models.URLField(verbose_name="Сайт",max_length=200)

    class Meta:
        verbose_name_plural = 'Компанії'
        verbose_name = 'Компанії'

    def __str__(self):
        return self.Name