# Generated by Django 3.1 on 2020-10-19 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20201019_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('kartridzh', 'Картриджи'), ('isparitel', 'Испарители'), ('vata', 'Вата'), ('mundshtuki', 'Мундштуки'), ('namotki', 'Намотки')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 19, 16, 32, 15, 130665), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 19, 16, 32, 15, 126408), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='images/no-img.jpg', upload_to='images', verbose_name='Изображение-2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='images/no-img.jpg', upload_to='images', verbose_name='Изображение-3'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 19, 16, 32, 15, 129930), verbose_name='Время добавления'),
        ),
    ]
