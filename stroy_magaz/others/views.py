from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Sum
from .models.faq import Faq
from service.models.kindworks import KindWorks
from service.models.service import Service
from site_some_settings.mixins import KindWorkMixin
from .models.about_us import AboutUs
from .models.main_comments import MainComments
from .forms import MainCommentsForm, CollBackClientForm
from .models.coll_back import CollBack, CollBackClient
from .models.order import Order
from .forms import OrderCreateForm
from .models.documentation import Documentation
from site_some_settings.models import SiteSettings


class ListFaq(ListView, KindWorkMixin):
    """
    Страница FAQ
    """
    model = Faq
    template_name = 'faq/faq_list.html'

    def get_context_data(self, *args, **kwargs):
        data = super(ListFaq, self).get_context_data(*args, **kwargs)
        data['faq'] = self.model.objects.all()
        # data['topics'] = Topic.objects.all()

        return data





class AboutUsPage(ListView, KindWorkMixin):
    """
    Страница о нас
    """
    model = AboutUs
    template_name = 'about_us/about_us.html'

    def get_context_data(self, *args, **kwargs):
        data = super(AboutUsPage, self).get_context_data(*args, **kwargs)
        data['aboutus'] = self.model.objects.first()
        # data['topics'] = Topic.objects.all()

        return data



class Contact(ListView, KindWorkMixin):
    """
    Страница контакты
    """
    model = AboutUs
    template_name = 'contacts/contacts.html'

    def get_context_data(self, *args, **kwargs):
        data = super(Contact, self).get_context_data(*args, **kwargs)
        data['contacts'] = self.model.objects.first()
        # data['topics'] = Topic.objects.all()

        return data








class MainCommentsView(ListView, KindWorkMixin):
    """
    Оботражения и создание отзывов
    """
    model = MainComments
    template_name = 'main_comments/main_comments.html'

    def get_context_data(self, *args, **kwargs):
        data = super(MainCommentsView, self).get_context_data(*args, **kwargs)
        data['comments'] = self.model.objects.all().order_by('-created')

        if MainComments.objects.filter(moderation=True).count()!= 0:
            data['average_mark'] = MainComments.objects.filter(moderation=True).aggregate(Sum('job_satisfaction'))[
                               'job_satisfaction__sum'] / MainComments.objects.filter(moderation=True).count()
        else:
            data['average_mark'] = None

        data['comment_form'] = MainCommentsForm()

        return data


                                            # def post(self, request, *args, **kwargs):
                                            #
                                            #     site_settings = SiteSettings.objects.first()
                                            #     kindworks = KindWorks.objects.all()
                                            #     about_us = AboutUs.objects.first()
                                            #     documentations = Documentation.objects.all()
                                            #
                                            #
                                            #
                                            #     if request.method == 'POST':
                                            #         comment_form = MainCommentsForm(request.POST)
                                            #         if comment_form.is_valid():
                                            #
                                            #             comment_form.save()
                                            #
                                            #             return redirect('/comments/')
                                            #     else:
                                            #         comment_form = MainCommentsForm()
                                            #
                                            #     context = {
                                            #         'comment_form': comment_form,
                                            #         'documentations': documentations,
                                            #         'about_us': about_us,
                                            #         'site_settings': site_settings,
                                            #         'kindworks': kindworks,
                                            #     }
                                            #
                                            #     return render(request, 'main_comments/main_comments.html', context=context)







class CollBackView(ListView, KindWorkMixin):
    """
    Заказ обратного звонка
    """
    model = CollBack
    template_name = 'coll_back/coll_back_form.html'

    def get_context_data(self, *args, **kwargs):
        data = super(CollBackView, self).get_context_data(*args, **kwargs)

        data['сoll_back'] = CollBack.objects.first()
        data['сoll_back_form'] = CollBackClientForm()

        return data


def add_coll_back(request,):

    сoll_back = CollBack.objects.first()
    comment_form = CollBackClientForm(request.POST)


    if request.method == 'POST':
        comment_form = CollBackClientForm(request.POST)
        if comment_form.is_valid():

            comment_form.save()

            return redirect('/coll-back/success/')
    else:
        comment_form = CollBackClientForm()

    site_settings = SiteSettings.objects.first()
    kindworks = KindWorks.objects.all()
    about_us = AboutUs.objects.first()
    documentations = Documentation.objects.all()

    context = {
        'сoll_back_form': comment_form,
        'сoll_back': сoll_back,
        'documentations': documentations,
        'about_us': about_us,
        'site_settings': site_settings,
        'kindworks': kindworks,
    }

    return render(request, 'coll_back/coll_back_form.html', context=context)












class CollBackSuccessView(ListView, KindWorkMixin):
    """
    Если форма обратного звонка заполнено правильно, редирект сюда
    """
    model = CollBack
    template_name = 'coll_back/success.html'

    def get_context_data(self, *args, **kwargs):
        data = super(CollBackSuccessView, self).get_context_data(*args, **kwargs)

        data['сoll_back'] = CollBack.objects.first()
        data['сoll_back_form'] = CollBackClientForm()

        return data











class OrderCreateView(ListView, KindWorkMixin):
    """
    Форма создания заказа
    """
    model = Order
    template_name = 'order/order_create_form.html'

    def get_context_data(self, *args, **kwargs):
        data = super(OrderCreateView, self).get_context_data(*args, **kwargs)

        data['order_create_form'] = OrderCreateForm()

        return data


                                                            # def post(self, request, *args, **kwargs):
                                                            #
                                                            #     order_create_form = OrderCreateForm()
                                                            #
                                                            #
                                                            #     if request.method == 'POST':
                                                            #         comment_form = OrderCreateForm(request.POST, request.FILES)
                                                            #         if comment_form.is_valid():
                                                            #
                                                            #             comment_form.save()
                                                            #
                                                            #             return redirect('/order-create/success/')
                                                            #     else:
                                                            #         order_create_form = OrderCreateForm()
                                                            #     site_settings = SiteSettings.objects.first()
                                                            #     kindworks = KindWorks.objects.all()
                                                            #     about_us = AboutUs.objects.first()
                                                            #     documentations = Documentation.objects.all()
                                                            #
                                                            #     context = {
                                                            #         'order_create_form': order_create_form,
                                                            #         'documentations': documentations,
                                                            #         'about_us': about_us,
                                                            #         'site_settings': site_settings,
                                                            #         'kindworks': kindworks,
                                                            #     }
                                                            #
                                                            #     return render(request, 'order/order_create_form.html', context=context)


def create_order(request):

    order_create_form = OrderCreateForm()
    order_create_form = OrderCreateForm(request.POST, request.FILES)

    if request.method == 'POST':

        if order_create_form.is_valid():

            order_create_form.save()

            return redirect('/order-create/success/')
    else:
        order_create_form = OrderCreateForm()


    site_settings = SiteSettings.objects.first()
    kindworks = KindWorks.objects.all()
    about_us = AboutUs.objects.first()
    documentations = Documentation.objects.all()

    context = {
        'order_create_form': order_create_form,
        'documentations': documentations,
        'about_us': about_us,
        'site_settings': site_settings,
        'kindworks': kindworks,
    }

    return render(request, 'order/order_create_form.html', context=context)



class OrderCreateSuccessView(ListView, KindWorkMixin):
    """
    Если форма создания заказа была заполнена верно перенаправляет сюда
    """
    model = Order
    template_name = 'order/success.html'

    def get_context_data(self, *args, **kwargs):
        data = super(OrderCreateSuccessView, self).get_context_data(*args, **kwargs)


        return data







class DocumentationsView(ListView, KindWorkMixin):
    """
    Форма отображения докуменации
    """

    model = Documentation
    template_name = 'documentations/documentations.html'

    def get_context_data(self, *args, **kwargs):
        data = super(DocumentationsView, self).get_context_data(*args, **kwargs)
        data['documents'] = self.model.objects.all()
        # data['topics'] = Topic.objects.all()

        return data





















def add_comment(request):
    kindworks = KindWorks.objects.all()
    # if Images.objects.first():
    #     images = Images.objects.get(id=1)
    # else:
    images = None
    list = Service.objects.all()
    # home_page_text = HomePageText.objects.first()
    # main_sliders = MainSlider.objects.all()
    about_us = AboutUs.objects.first()
    # p_objects = Portfolio.objects.all()
    # partners = Partners.objects.all()
    # coll_back = CollBack.objects.first()
    # documentations = Documentation.objects.all()
    site_settings = SiteSettings.objects.first()



    if request.method == 'POST':
        comment_form = MainCommentsForm(request.POST)
        if comment_form.is_valid():

            comment_form.save()

            return redirect('/comments/')
    else:
        comment_form = MainCommentsForm()




    context = {
        'comment_form': comment_form,
        'site_settings': site_settings,
        'kindworks': kindworks,
        'images': images,
        'list': list,
        'about_us': about_us,

    }
    return render(request, 'main_comments/main_comments.html', context=context)

