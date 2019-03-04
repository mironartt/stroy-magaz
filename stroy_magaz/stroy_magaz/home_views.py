from django.shortcuts import render
from django.views import View
from service.models.service import Service
from service.models.images import Images
from service.models.kindworks import KindWorks
from others.models.home import HomePageText
from others.models.main_slider import MainSlider
from others.models.about_us import AboutUs
from portfolio.models.portfolio import Portfolio
from others.models.partners import Partners
from others.models.coll_back import CollBack
from others.models.documentation import Documentation
from site_some_settings.models import SiteSettings
from datetime import datetime, timedelta

class HomeList(View):
    """Отображает главную страницу"""

    def get(self, request, *args, **kwargs):

        if not SiteSettings.objects.first():
            SiteSettings.objects.create(site_name='Название сайта')

        request.session.set_expiry(0)

        site_settings = SiteSettings.objects.first()
        if not site_settings.last_day:
            site_settings.last_day = datetime.now()
            site_settings.save()

        if not site_settings.last_month:
            site_settings.last_month = datetime.now()
            site_settings.save()

        if site_settings.number_visits_month == None:
            site_settings.number_visits_month = 0
            site_settings.save()

        if site_settings.number_visits_all_time == None:
            site_settings.number_visits_all_time = 0
            site_settings.save()

        if site_settings.number_visits_day == None:
            site_settings.number_visits_day = 0
            site_settings.save()

        """Получаю числовое значение дня отсчета с временной поправкой + 3 часа."""
        last_day = (str(site_settings.last_day + timedelta(hours=3))).split()
        last_day = last_day[0].split('-')
        last_day = int(last_day[2])


        """Проверка, закончился ли день. Если до то обнулить счетчик посещений за день и обновить дату отсчета и сбросить все сессии"""
        if ((last_day - int(datetime.now().day)) != 0) or ((site_settings.last_month.month - datetime.now().month) != 0):
            """Проверяю не прошел ли месяц с точки отсчета месяца"""
            if (site_settings.last_month.month - datetime.now().month) != 0:
                """Обнуляю дату отсчета месяца"""
                site_settings.last_month = datetime.now()
                """Обнуляю дату отсчета дней"""
                site_settings.last_day = datetime.now()
                """Обнуляю число посещений за месяц"""
                site_settings.number_visits_month = 0
                # site_settings.save()
                """Обнуляю число посещений за день"""
                site_settings.number_visits_day = 0
                """Сохраняю изменения"""
                site_settings.save()
                """Обнуляю сессии"""
                request.session.flush()
            else:
                """Меняю дату дня отсчета дней на сейчас"""
                site_settings.last_day = datetime.now()
                """Обнуляю число посещений за день"""
                site_settings.number_visits_day = 0
                """Сохраняю изменения в модели"""
                site_settings.save()
                """Обнуляю сессии"""
                request.session.flush()


        """Проврить есть ли его ключ сесии в базе & проверить прошел не прошел ли день (24 часа). Если да то добавить в счетчик посещений 1"""
        if (not request.session.session_key):

            site_settings.number_visits_day += 1
            site_settings.number_visits_month += 1
            site_settings.number_visits_all_time += 1
            site_settings.save()



        kindworks = KindWorks.objects.all()
        images = None
        list = Service.objects.all()
        home_page_text = HomePageText.objects.first()
        main_sliders = MainSlider.objects.all()
        about_us = AboutUs.objects.first()
        p_objects = Portfolio.objects.all()
        partners = Partners.objects.all()
        coll_back = CollBack.objects.first()
        documentations = Documentation.objects.all()
        site_settings = SiteSettings.objects.first()

        context = {
            'site_settings':site_settings,
            'kindworks':kindworks,
            'images':images,
            'list':list,
            'home_page_text':home_page_text,
            'main_sliders':main_sliders,
            'about_us':about_us,
            'p_objects':p_objects,
            'partners':partners,
            'coll_back':coll_back,
            'documentations':documentations,

        }

        return render(request, 'base.html', context=context)


