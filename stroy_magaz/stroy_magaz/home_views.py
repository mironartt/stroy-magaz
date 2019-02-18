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


class HomeList(View):

    def get(self, request, *args, **kwargs):


        if not SiteSettings.objects.first():
            SiteSettings.objects.create(site_name='Название сайта')





        kindworks = KindWorks.objects.all()
        # if Images.objects.first():
        #     images = Images.objects.get(id=1)
        # else:
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

