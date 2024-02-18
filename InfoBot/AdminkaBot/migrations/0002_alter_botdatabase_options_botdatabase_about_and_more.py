# Generated by Django 4.2.1 on 2023-06-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminkaBot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='botdatabase',
            options={'verbose_name': 'Компанії', 'verbose_name_plural': 'Компанії'},
        ),
        migrations.AddField(
            model_name='botdatabase',
            name='About',
            field=models.CharField(default='', max_length=400, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='botdatabase',
            name='FaсebookURL',
            field=models.URLField(default='', max_length=300, verbose_name='Фейсбук'),
        ),
        migrations.AddField(
            model_name='botdatabase',
            name='InstagramURL',
            field=models.URLField(default='', max_length=300, verbose_name='Інстаграм'),
        ),
        migrations.AddField(
            model_name='botdatabase',
            name='coordinates',
            field=models.CharField(default='', max_length=300, verbose_name='Кординати'),
        ),
        migrations.AlterField(
            model_name='botdatabase',
            name='Name',
            field=models.CharField(max_length=200, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='botdatabase',
            name='PhotoURL',
            field=models.URLField(verbose_name='Url зсилка фото'),
        ),
        migrations.AlterField(
            model_name='botdatabase',
            name='SiteURL',
            field=models.URLField(max_length=300, verbose_name='Сайт'),
        ),
        migrations.AlterField(
            model_name='botdatabase',
            name='address',
            field=models.CharField(max_length=300, verbose_name='Адреса'),
        ),
        migrations.AlterField(
            model_name='botdatabase',
            name='category',
            field=models.CharField(choices=[('Ательє', 'Ательє'), ('Аптеки', 'Аптеки'), ('Кафе', 'Кафе'), ('Бари', 'Бари'), ('Клуби', 'Клуби'), ('Ресторани', 'Ресторани'), ('Фастфуди', 'Фастфуди'), ('Клініки', 'Клініки'), ('Салони_краси', 'Салони_краси'), ('Спортзали', 'Спортзали')], max_length=300, verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='botdatabase',
            name='tel',
            field=models.CharField(max_length=100, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='botdatabase',
            name='work_schedule',
            field=models.CharField(max_length=100, verbose_name='Робочий графік'),
        ),
    ]