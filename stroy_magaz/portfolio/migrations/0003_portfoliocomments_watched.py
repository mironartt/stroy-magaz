# Generated by Django 2.1.5 on 2019-02-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190225_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliocomments',
            name='watched',
            field=models.BooleanField(default=False, verbose_name='Просмотрено'),
        ),
    ]