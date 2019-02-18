from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .home_views import HomeList
from others.views import add_coll_back, add_comment, create_order, AboutUsPage, Contact, MainCommentsView, CollBackView, CollBackSuccessView, OrderCreateView, OrderCreateSuccessView, DocumentationsView
from portfolio.views import ListAllPortfolio
from site_some_settings.views import SearchView

#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', AboutUsPage.as_view(), name='about_us_url'),
    path('documentations/', DocumentationsView.as_view(), name='documentations_url'),
    path('portfolioobject/', ListAllPortfolio.as_view(), name='dfghfgds'),

    path('add-comment/', add_comment, name='add_comment_url'),
    path('create-order/', create_order, name='create_order_url'),

    path('search/', SearchView.as_view(), name='search_url'),

    path('coll-back/', CollBackView.as_view(), name='coll_bacl_form_url'),
    path('add-coll-back/', add_coll_back, name='add_coll_bacl_url'),
    path('coll-back/success/', CollBackSuccessView.as_view(), name='coll_bacl_success_url'),

    path('order-create/', OrderCreateView.as_view(), name='order_create_form_url'),
    path('order-create/success/', OrderCreateSuccessView.as_view(), name='order_create_success_url'),

    path('contacts/', Contact.as_view(), name='contacts_url'),


    path('comments/', MainCommentsView.as_view(), name='main_comments_url'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('test/', include('ticket.urls')),
    path('faq/', include('others.urls', namespace='faq')),
    re_path(r'^$', HomeList.as_view(), name='home_url'),
    path('', include('service.urls', namespace='service')),

    path('portfolio', include('portfolio.urls', namespace='portfolio'))
#
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

