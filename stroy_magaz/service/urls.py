from django.urls import path, include
from .views import *

app_name = 'service'

urlpatterns = [
    path('kind-works/service/<slug>', ServiceDetail.as_view(), name='service_detail_url'),
    path('kind-works/<slug>', DetailKindWork.as_view(), name='kind_works_detail_url'),
    path('kind-works/', ListKindWork.as_view(), name='kind_works_list_url'),
    # path('', HomeList.as_view(), name='home_url'),
]