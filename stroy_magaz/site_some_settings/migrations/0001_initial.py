# Generated by Django 2.1.5 on 2019-02-18 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название сайта отобраается в название вкладки')),
                ('confirm_main_comments', models.BooleanField(default=False, verbose_name='Публикация отзывов в разделе "отзывы" без модерации')),
                ('confirm_portfolio_comments', models.BooleanField(default=False, verbose_name='Публикация коментариев в разделе портфолио без модерации')),
                ('confirm_services_comments', models.BooleanField(default=False, verbose_name='Публикация коментариев в разделе "типы работ и усуи" без модерации')),
                ('avalible_load_files_order', models.BooleanField(default=True, verbose_name='Разрешить клиентам загружать файлы на сервер')),
                ('social_link_vk', models.URLField(blank=True, null=True, verbose_name='Сылка на профиль ВК')),
                ('social_link_youtube', models.URLField(blank=True, null=True, verbose_name='Сылка на профиль YouTube')),
                ('social_link_linkedin', models.URLField(blank=True, null=True, verbose_name='Сылка на профиль LinkedIn')),
                ('social_link_twitter', models.URLField(blank=True, null=True, verbose_name='Сылка на профиль Twitter')),
                ('social_link_facebook', models.URLField(blank=True, null=True, verbose_name='Сылка на профиль FaceBook')),
                ('social_link_other_1', models.URLField(blank=True, null=True, verbose_name='Сылка на профиль 1')),
                ('social_link_other_2', models.URLField(blank=True, null=True, verbose_name='Сылка на профиль 2')),
            ],
            options={
                'verbose_name': 'Настройки сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
    ]
