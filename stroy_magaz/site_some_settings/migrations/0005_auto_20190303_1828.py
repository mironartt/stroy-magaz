# Generated by Django 2.1.5 on 2019-03-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_some_settings', '0004_auto_20190303_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='last_day',
            field=models.DateTimeField(blank=True, null=True, verbose_name='День от которого идет счет 24 часов'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='last_month',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Месяц от которого идет счет'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='number_visits_all_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Число посещений за все время'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='number_visits_day',
            field=models.IntegerField(blank=True, null=True, verbose_name='Число посещений за день'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='number_visits_month',
            field=models.IntegerField(blank=True, null=True, verbose_name='Число посещений за месяц'),
        ),
    ]