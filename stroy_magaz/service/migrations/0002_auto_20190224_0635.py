# Generated by Django 2.1.5 on 2019-02-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kindworkscomments',
            name='watched',
            field=models.BooleanField(default=False, verbose_name='Просмотрено'),
        ),
        migrations.AddField(
            model_name='servicecomments',
            name='watched',
            field=models.BooleanField(default=False, verbose_name='Просмотрено'),
        ),
    ]
