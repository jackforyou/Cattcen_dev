from django.conf.urls import url
import os
from . import views

app_name = 'caterlist'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^Project/chinesetable_list/$', views.CateringList.as_view(), name="chinesetable_list"),
    url(r'^Project/search/$', views.search),
    url(r'^Project/chinesetable/(?P<pk>[0-9]+)/$', views.ChineseDetailView.as_view(), name='chinesetable'),
]
