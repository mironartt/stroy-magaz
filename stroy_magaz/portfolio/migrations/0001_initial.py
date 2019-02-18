# Generated by Django 2.1.5 on 2019-02-18 01:00

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import portfolio.models.images
import portfolio.models.portfolio


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=portfolio.models.images.generate_filename, verbose_name='Все изображения приложения услуги')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Наименование')),
                ('description', models.CharField(blank=True, max_length=800, null=True, verbose_name='Описаниее')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображения',
                'ordering': ('image',),
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('main_image', models.ImageField(upload_to=portfolio.models.portfolio.generate_filename, verbose_name='Главное изображение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('availability', models.BooleanField(default=True, verbose_name='Отображать на сайте')),
                ('images', models.ManyToManyField(blank=True, to='portfolio.Images', verbose_name='Галерея изображений')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Объекты портфолио',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PortfolioComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_object', models.IntegerField(blank=True, null=True, verbose_name='ID Объектa коментирования')),
                ('name_person', models.CharField(max_length=200, verbose_name='Имя того кто написал коментарий')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('comment_body', models.TextField(verbose_name='Тело коментария')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('moderation', models.BooleanField(default=False, verbose_name='Модерация')),
            ],
            options={
                'verbose_name': 'Коментарии объектов портфолио',
                'verbose_name_plural': 'Коментарии объектов портфолио',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Названи категории')),
                ('slug', models.SlugField()),
                ('descriprion', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AddField(
            model_name='portfolio',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='portfolio.Topic', verbose_name='Категория'),
        ),
        migrations.AlterIndexTogether(
            name='images',
            index_together={('id', 'slug')},
        ),
        migrations.AlterIndexTogether(
            name='portfolio',
            index_together={('id', 'slug')},
        ),
    ]