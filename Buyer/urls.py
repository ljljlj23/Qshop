from django.contrib import admin
from django.urls import path,include
from Buyer.views import *

urlpatterns = [
    path('login/',login),
    path('index/',index),
    path('register/',register),
    path('logout/',logout),
    path('goods_list/',goods_list),

    # path('Saller/',include('Saller.urls')),
]