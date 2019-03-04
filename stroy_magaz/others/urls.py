from django.urls import path, include
from .views import *

app_name = 'faq'

urlpatterns = [
    path('', ListFaq.as_view(), name='list_faq_url'),
]