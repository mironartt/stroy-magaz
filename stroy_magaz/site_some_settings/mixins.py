from django.views.generic.list import MultipleObjectMixin
from django.views.generic import View
from service.models.kindworks import KindWorks
from others.models.about_us import AboutUs
from others.models.documentation import Documentation
from site_some_settings.models import SiteSettings

class KindWorkMixin(MultipleObjectMixin):

    def get_context_data(self, *args, **kwargs):
        data = {}
        data['site_settings'] = SiteSettings.objects.first()
        data['kindworks'] = KindWorks.objects.all()
        data['about_us'] = AboutUs.objects.first()
        data['documentations'] = Documentation.objects.all()

        return data

    def get(self):
        site_settings = SiteSettings.objects.first()
        kindworks = KindWorks.objects.all()
        about_us = AboutUs.objects.first()
        documentations = Documentation.objects.all()

        context = {
            'documentations':documentations,
            'about_us':about_us,
            'site_settings':site_settings,
            'kindworks':kindworks,
        }
        return context