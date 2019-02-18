from django.urls import path, include
from .views import *

app_name = 'portfolio'

urlpatterns = [
    path('object/<slug>', DetailPortfolioObj.as_view(), name='p_obj_detail_url'),
    # path('object/<slug>', detailportfoliobj, name='p_obj_detail_url'),
    # path('portfolioobject/', add_comment, name='add_comment_url'),
    path('topic/<slug>', ListTopcDetail.as_view(), name='list_p_obj_topic_url'),
    path('', ListAllPortfolio.as_view(), name='list_all_portfolio'),
    # path('', HomeList.as_view(), name='home_url'),
]