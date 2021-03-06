# Generated by Django 3.1 on 2020-10-03 09:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20201003_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('new', models.BooleanField(default=False, verbose_name='Добавить в категорию новые?')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True)),
                ('image', models.ImageField(upload_to='images', verbose_name='Изображение')),
                ('brand', models.CharField(default='другие', max_length=255, verbose_name='Бренд')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('sale', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Скидка')),
                ('add_time', models.TimeField(default=datetime.datetime(2020, 10, 3, 12, 26, 4, 248107), verbose_name='Время добавления')),
                ('add_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата добавления')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Категория')),
            ],
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='producted_ptr',
        ),
        migrations.RemoveField(
            model_name='producted',
            name='category',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='add_time',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='description',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='image',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='new',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='price',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='sale',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='title',
        ),
        migrations.RemoveField(
            model_name='crate',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='crate',
            name='add_time',
        ),
        migrations.RemoveField(
            model_name='crate',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='crate',
            name='category',
        ),
        migrations.RemoveField(
            model_name='crate',
            name='description',
        ),
        migrations.RemoveField(
            model_name='crate',
            name='id',
        ),
        migrations.RemoveField(
            model_name='crate',
            name='image',
        ),
        migrations.RemoveField(
            model_name='crate',
            name='new',
        ),
        migrations.RemoveField(
            model_name='crate',
            name='price',
        ),
        migrations.RemoveField(
            model_name='crate',
            name='sale',
        ),
        migrations.RemoveField(
            model_name='crate',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='crate',
            name='title',
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='add_time',
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='category',
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='description',
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='id',
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='image',
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='new',
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='price',
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='sale',
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='title',
        ),
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('VTA', 'Вата'), ('NMK', 'Намотки'), ('IS', 'Испарители'), ('CRT', 'Картриджи'), ('MND', 'Мундштуки')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='salt',
            field=models.CharField(choices=[('NO', 'Нет'), ('YES', 'Да')], max_length=255, null=True, verbose_name='SALT'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 3, 12, 26, 4, 250174), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 3, 12, 26, 4, 249104), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='table',
            field=models.CharField(choices=[('Accessory', 'Accessory'), ('Liquid', 'Liquid')], max_length=255, null=True, verbose_name='Категория'),
        ),
        migrations.DeleteModel(
            name='Desktop',
        ),
        migrations.DeleteModel(
            name='Monitor',
        ),
        migrations.DeleteModel(
            name='Producted',
        ),
        migrations.AddField(
            model_name='accessory',
            name='product_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crate',
            name='product_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='liquid',
            name='product_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product'),
            preserve_default=False,
        ),
    ]
