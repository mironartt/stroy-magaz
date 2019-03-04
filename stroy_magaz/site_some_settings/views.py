from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from .mixins import KindWorkMixin
from django.db.models import Q
from service.models.kindworks import KindWorks #desctiption, name
from service.models.service import Service #desctiptions, name
from others.models.documentation import Documentation #title, description
from portfolio.models.portfolio import Portfolio  #name, descriprion
from portfolio.models.portfolio import Topic #name, descriprion
from others.models.about_us import AboutUs #text_about_us_page, text_about_us_page_2, notes,
from others.models.faq import Faq #question, answer
from datetime import datetime, timedelta
from django.utils.dateformat import DateFormat, TimeFormat
from .models import SiteSettings


class SearchView(TemplateView, KindWorkMixin):

    template_name = 'search/search.html'

    def get_context_data(self, *args, **kwargs):
        data = super(SearchView, self).get_context_data(*args, **kwargs)

        query = self.request.GET.get('q')
        # data['founded_kindworks'] = KindWorks.objects.filter((Q(desctiption__icontains=query)) | (Q(name__icontains=query)))
        data['founded_kindworks'] = KindWorks.objects.filter(
            (Q(name__icontains=query)))
        query_sets = []  # Общий QuerySet

        data['query_request'] = query

        if KindWorks.objects.filter((Q(desctiption__icontains=query)) | (Q(name__icontains=query))):
            query_sets.append(KindWorks.objects.filter((Q(desctiption__icontains=query)) | (Q(name__icontains=query)))  )
        if Service.objects.filter((Q(desctiptions__icontains=query)) | (Q(name__icontains=query))):
            query_sets.append(Service.objects.filter((Q(desctiptions__icontains=query)) | (Q(name__icontains=query))))
        if Documentation.objects.filter((Q(description__icontains=query)) | (Q(title__icontains=query))):
            query_sets.append(Documentation.objects.filter((Q(description__icontains=query)) | (Q(title__icontains=query))))
        if Portfolio.objects.filter((Q(description__icontains=query)) | (Q(name__icontains=query))):
            query_sets.append(Portfolio.objects.filter((Q(description__icontains=query)) | (Q(name__icontains=query))))
        if Topic.objects.filter((Q(descriprion__icontains=query)) | (Q(name__icontains=query))):
            query_sets.append(Topic.objects.filter((Q(descriprion__icontains=query)) | (Q(name__icontains=query))))
        if AboutUs.objects.filter((Q(text_about_us_page__icontains=query)) | (Q(text_about_us_page_2__icontains=query)) | (Q(notes__icontains=query))):
            query_sets.append(AboutUs.objects.filter((Q(text_about_us_page__icontains=query)) | (Q(text_about_us_page_2__icontains=query)) | (Q(notes__icontains=query))))

        if Faq.objects.filter((Q(question__icontains=query)) | (Q(answer__icontains=query))):
            query_sets.append(Faq.objects.filter((Q(question__icontains=query)) | (Q(answer__icontains=query))))

        query_set_count = 0
        for i in query_sets:
            for j in i:
                query_set_count += 1

        data['query_sets'] = query_sets
        data['query_set_count'] = query_set_count


        return data



class Statistics(TemplateView, KindWorkMixin):

    template_name = 'site_documentations/statistics.html'

    def get_context_data(self, *args, **kwargs):
        data = super(Statistics, self).get_context_data(*args, **kwargs)
        site_settings = SiteSettings.objects.first()

        data['number_visits_day'] = site_settings.number_visits_day
        data['number_visits_month'] = site_settings.number_visits_month
        data['number_visits_all_time'] = site_settings.number_visits_all_time

        return data



class Documentations(TemplateView, KindWorkMixin):

    template_name = 'site_documentations/documentations.html'

    def get_context_data(self, *args, **kwargs):
        data = super(Documentations, self).get_context_data(*args, **kwargs)

        return data

