# Generated by Django 3.1 on 2020-10-19 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20201019_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('namotki', 'Намотки'), ('vata', 'Вата'), ('isparitel', 'Испарители'), ('mundshtuki', 'Мундштуки'), ('kartridzh', 'Картриджи')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='salt',
            field=models.CharField(choices=[('NO', 'Нет'), ('YES', 'Да')], max_length=255, null=True, verbose_name='SALT'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 19, 17, 20, 46, 302572), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 19, 17, 20, 46, 298231), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 19, 17, 20, 46, 301839), verbose_name='Время добавления'),
        ),
    ]
