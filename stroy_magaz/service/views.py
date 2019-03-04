from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models.service import Service
from service.models.kindworks import KindWorks
from others.models.about_us import AboutUs
from others.models.documentation import Documentation
from site_some_settings.models import SiteSettings
from site_some_settings.mixins import KindWorkMixin
from .forms import KindWorksCommentsForm, ServiceCommentsForm
from .models.comments import KindWorksComments, ServiceComments
from .tasks import mail_sent_create_kind_work_comment, mail_sent_create_services_comment


class DetailKindWork(DetailView, KindWorkMixin):
    """
        Оботражает конкретную тематику работ и обрабатывает коментарии к ней
    """

    model = KindWorks
    template_name = 'kind_works&service/kind_works_detail.html'

    def get_context_data(self, *args, **kwargs):
        data = super(DetailKindWork, self).get_context_data(*args, **kwargs)
        data['kind_work'] = self.get_object()
        data['service_kind_works'] = self.get_object().service_set.all()

        # получаю queryset коментариев относящихся к этому объекту
        data['comments'] = KindWorksComments.objects.filter(parent_object=self.get_object().id)
        data['comment_form'] = KindWorksCommentsForm()

        return data



    def post(self, request, *args, **kwargs):

        site_settings = SiteSettings.objects.first()
        kindworks = KindWorks.objects.all()
        about_us = AboutUs.objects.first()
        documentations = Documentation.objects.all()

        p_obj = self.get_object()

        if request.method == 'POST':
            comment_form = KindWorksCommentsForm(request.POST)
            if comment_form.is_valid():
                comment_form.save(commit=False)
                instance = comment_form.instance
                instance.parent_object = p_obj.id

                comment = comment_form.save()

                """Подготовка данных к отправке и отправка емейла клиенту и админу"""
                info = []
                info.extend((comment.parent_object, comment.name_person, comment.email, comment.comment_body))
                info.append((HttpRequest.get_host(request) + '/kind-works/'+ str(p_obj.slug)  + '#form-wrapper'))
                info.append((HttpRequest.get_host(request) + '/admin/service/kindworkscomments/' + str(comment.id) + '/change/'))
                # print(info)
                mail_sent_create_kind_work_comment.delay(info)

                return redirect('/kind-works/'+ str(p_obj.slug) + '#form-wrapper')
        else:
            comment_form = KindWorksCommentsForm()

        context = {
            'comment_form':comment_form,
            'documentations': documentations,
            'about_us': about_us,
            'site_settings': site_settings,
            'kindworks': kindworks,
        }

        return render(request, 'kind_works&service/kind_works_detail.html', context=context)

class ListKindWork(ListView, KindWorkMixin):
    """
        Отображает все типы работ
    """

    model = KindWorks
    template_name = 'kind_works&service/list_kind_works.html'

    def get_context_data(self, *args, **kwargs):
        data = super(ListKindWork, self).get_context_data(*args, **kwargs)
        data['kind_works'] = self.model.objects.all()



        return data




class ServiceDetail(DetailView, KindWorkMixin):
    """
        Отображает конкретную услугу и обрабатывает коментарии связынные с ней
    """

    model = Service
    template_name = 'kind_works&service/service_deail.html'

    def get_context_data(self, *args, **kwargs):
        data = super(ServiceDetail, self).get_context_data(*args, **kwargs)
        data['service'] = self.get_object()
        data['kind_work'] = KindWorks.objects.get(id=data['service'].kindworks_id)

        # получаю queryset коментариев относящихся к этому объекту
        data['comments'] = ServiceComments.objects.filter(parent_object=self.get_object().id)
        data['comment_form'] = ServiceCommentsForm()

        return data

    def post(self, request, *args, **kwargs):

        site_settings = SiteSettings.objects.first()
        kindworks = KindWorks.objects.all()
        about_us = AboutUs.objects.first()
        documentations = Documentation.objects.all()
        comment_form = ServiceCommentsForm()
        p_obj = self.get_object()

        if request.method == 'POST':
            comment_form = ServiceCommentsForm(request.POST)
            if comment_form.is_valid():
                comment_form.save(commit=False)
                instance = comment_form.instance
                instance.parent_object = p_obj.id

                comment = comment_form.save()

                """Подготовка данных к отправке и отправка емейла клиенту и админу"""
                info = []
                info.extend((comment.parent_object, comment.name_person, comment.email, comment.comment_body))
                info.append((HttpRequest.get_host(request) + '/kind-works/service/' + str(p_obj.slug)  + '#form-wrapper'))
                info.append((HttpRequest.get_host(request) + '/admin/service/servicecomments/' + str(comment.id) + '/change/'))
                print(info)
                mail_sent_create_services_comment.delay(info)

                return redirect('/kind-works/service/' + str(p_obj.slug) + '#form-wrapper')
        else:
            comment_form = ServiceCommentsForm()

        context = {'comment_form': comment_form,
                   'documentations': documentations,
                   'about_us': about_us,
                   'site_settings': site_settings,
                   'kindworks': kindworks,
                   }

        return render(request, 'kind_works&service/service_deail.html', context=context)


