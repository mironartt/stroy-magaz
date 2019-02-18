from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView

from .models.portfolio import Portfolio, Topic
from .models.comments import PortfolioComments

from service.models.kindworks import KindWorks
from others.models.about_us import AboutUs
from others.models.documentation import Documentation
from site_some_settings.models import SiteSettings

from .models.images import Images
from site_some_settings.mixins import KindWorkMixin
from .forms import PortfolioCommentsForm

class ListAllPortfolio(ListView, KindWorkMixin):
    """
    Отображение всех объектов портфолио
    """
    model = Portfolio
    template_name = 'portfolio/list_all_portfolio.html'

    def get_context_data(self, *args, **kwargs):
        data = super(ListAllPortfolio, self).get_context_data(*args, **kwargs)
        data['p_objects'] = self.model.objects.all()
        data['topics'] = Topic.objects.all()


        return data




class ListTopcDetail(DetailView, KindWorkMixin):
    """
    Отображение объектов портфолио относящихся к выбранной категории
    """

    model = Topic
    template_name = 'portfolio/list_topic_portfolio.html'

    def get_context_data(self, *args, **kwargs):
        data = super(ListTopcDetail, self).get_context_data(*args, **kwargs)
        data['topic'] = self.get_object()
        data['topics'] = Topic.objects.all()
        data['p_objects'] = Portfolio.objects.filter(topic_id=data['topic'].id)

        # data['sdf'] = Images.objects.all()

        return data



class DetailPortfolioObj(DetailView, KindWorkMixin):

    """
    Отображает конкретный объект портфолио и обрабатывает коментарии к нему
    """

    model = Portfolio
    template_name = 'portfolio/p_obj_detail.html'

    def get_context_data(self, *args, **kwargs):
        data = super(DetailPortfolioObj, self).get_context_data(*args, **kwargs)
        data['p_obj'] = self.get_object()
        data['topics'] = Topic.objects.all()

        #получаю категорию к коткоторой относиться объект
        data['topic'] = Topic.objects.get(id=self.get_object().topic_id)

        # получаю queryset коментариев относящихся к этому объекту
        data['comments'] = PortfolioComments.objects.filter(parent_object=self.get_object().id)

        data['comment_form'] = PortfolioCommentsForm()


        return data


    def post(self, request, *args, **kwargs):



        p_obj = self.get_object()

        if request.method == 'POST':
            comment_form = PortfolioCommentsForm(request.POST)
            if comment_form.is_valid():
                comment_form.save(commit=False)
                instance = comment_form.instance
                instance.parent_object = p_obj.id


                comment_form.save()

                return redirect('/portfolioobject/'+ str(p_obj.slug)+'#form-wrapper')
        else:
            comment_form = PortfolioCommentsForm()

        site_settings = SiteSettings.objects.first()
        kindworks = KindWorks.objects.all()
        about_us = AboutUs.objects.first()
        documentations = Documentation.objects.all()

        context = {
            'comment_form':comment_form,
            'documentations': documentations,
            'about_us': about_us,
            'site_settings': site_settings,
            'kindworks': kindworks,
                   }

        return render(request, 'portfolio/p_obj_detail.html', context=context)









































# def add_comment(request):
#
    # if request.method == 'POST':
    #     comment_form = PortfolioCommentsForm(request.POST)
    #     if comment_form.is_valid():
    #         order = comment_form.save()
    #         # clear the cart
    #         # cart.clear()
    #         # launch asynchronous task
    #         # order_created.delay(order.id)
    #         return redirect('/')
    # else:
    #     comment_form = PortfolioCommentsForm()
    # return render(request, 'portfolio/p_obj_detail.html', {'comment_form': comment_form, })





# class AddComment(FormView):
#     form_class = PortfolioCommentsForm
#     # template_name = 'portfolio/p_obj_detail.html'  # Replace with your template.
#     success_url = '/'  # Replace with your URL or reverse().
#
#     # def post(self, request, *args, **kwargs):
#     #     form_class = self.get_form_class()
#     #     form = self.get_form(form_class)
#     #
#     #     if form.is_valid():
#     #         # f = form.save()    ...  # Do something with each file.
#     #         return self.form_valid(form)
#     #     else:
#     #         return self.form_invalid(form)
    #
#
#
# from django.views.generic.edit import CreateView
#
# class CreateComment(CreateView):
#     form_class = PortfolioCommentsForm
#     # template_name = 'portfolio/p_obj_detail.html'
#     succes_url = '/'
#
#     def form_valid(self, form):
#         Post.objects.create(**form.cleaned_data)
#         return redirect(self.get_success_url())




