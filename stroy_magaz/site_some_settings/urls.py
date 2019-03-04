
from django.urls import path, include, re_path
from .views import Statistics, Documentations

app_name = 'admin_detail'

urlpatterns = [
    path('statistics/', Statistics.as_view(), name='am_statistics_url'),
    path('documentations/', Documentations.as_view(), name='am_statistics_url'),
]