# Generated by Django 3.1 on 2020-10-19 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_auto_20201019_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('vata', 'Вата'), ('namotki', 'Намотки'), ('isparitel', 'Испарители'), ('mundshtuki', 'Мундштуки'), ('kartridzh', 'Картриджи')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='salt',
            field=models.CharField(choices=[('YES', 'Да'), ('NO', 'Нет')], max_length=255, null=True, verbose_name='SALT'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 19, 16, 15, 4, 303593), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 19, 16, 15, 4, 298207), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение-2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение-3'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 19, 16, 15, 4, 302417), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='table',
            field=models.CharField(choices=[('Liquid', 'Liquid'), ('Accessory', 'Accessory')], max_length=255, null=True, verbose_name='Категория'),
        ),
    ]
