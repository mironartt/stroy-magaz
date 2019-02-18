from django.urls import path, include
from .views import *

app_name = 'faq'

urlpatterns = [
    # path('object/<slug>', DetailPortfolioObj.as_view(), name='p_obj_detail_url'),
    # path('topic/<slug>', ListTopcDetail.as_view(), name='list_p_obj_topic_url'),
    path('', ListFaq.as_view(), name='list_faq_url'),
    # path('', HomeList.as_view(), name='home_url'),
]