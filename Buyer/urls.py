from django.contrib import admin
from django.urls import path,include,re_path
from Buyer.views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('login/',login),
    path('index/',index),
    path('register/',register),
    path('logout/',logout),
    # re_path('goods_list/(?P<page>\d+)',cache_page(60*15)(goods_list)),
    re_path('goods_list/(?P<page>\d+)',goods_list),
    path('goods_detail/',goods_detail),
    path('user_center_info/',user_center_info),
    path('place_order/',place_order),
    path('alipayview/',AlipayView),
    path('payresult/',payresult),
    path('add_cart/',add_cart),
    path('cart/',cart),
    path('place_order_more/',place_order_more),
    re_path('user_center_order/(?P<page>\d+)',user_center_order),
    path('reqtest/',reqtest),
    path('myprocess_tem_response/',myprocess_tem_response),
    path('cache_test/',cache_test),

    # path('Saller/',include('Saller.urls')),
]