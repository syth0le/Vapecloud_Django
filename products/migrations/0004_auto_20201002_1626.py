# Generated by Django 3.1 on 2020-10-02 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201002_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 2, 16, 26, 25, 566023), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('NMK', 'Намотки'), ('MND', 'Мундштуки'), ('CRT', 'Картриджи'), ('IS', 'Испарители')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='crate',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 2, 16, 26, 25, 566023), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 2, 16, 26, 25, 566023), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='salt',
            field=models.CharField(choices=[('YES', 'Да'), ('NO', 'Нет')], max_length=255, verbose_name='SALT'),
        ),
        migrations.AlterField(
            model_name='newproduct',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 2, 16, 26, 25, 568018), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 2, 16, 26, 25, 569015), verbose_name='Время добавления'),
        ),
    ]
