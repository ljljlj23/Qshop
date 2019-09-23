from django.contrib import admin
from django.urls import path,re_path,include
from Saller.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^$',hello),
    path('register/', register),
    path('login/', login),
    path('index/', index),
    path('logout/',logout),
    path('base/',base),
    # path('add_goods/',add_goods),
    re_path('goods_list/(?P<status>[01])/(?P<page>\d+)/',goods_list),
    re_path('setStatus/(?P<status>\w+)/(?P<id>\d+)/',setStatus),
    path('personal_info/',personal_info),
]