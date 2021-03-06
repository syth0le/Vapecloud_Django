# Generated by Django 3.1 on 2020-10-11 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20201010_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('kartridzh', 'Картриджи'), ('mundshtuki', 'Мундштуки'), ('isparitel', 'Испарители'), ('namotki', 'Намотки'), ('vata', 'Вата')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 11, 13, 40, 20, 455252), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 11, 13, 40, 20, 451223), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 11, 13, 40, 20, 455252), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='table',
            field=models.CharField(choices=[('Liquid', 'Liquid'), ('Accessory', 'Accessory')], max_length=255, null=True, verbose_name='Категория'),
        ),
    ]
