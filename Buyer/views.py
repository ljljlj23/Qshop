from django.shortcuts import render
from django.http import HttpResponseRedirect
import hashlib
from Saller.models import *

def setPassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result

def loginValid(func):
    def inner(request,*args,**kwargs):
        email=request.COOKIES.get('email')
        pwd=request.COOKIES.get('pwd')
        email_session=request.session.get('email')
        if email and pwd and email==email_session:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/Buyer/login/')
    return inner

# @loginValid
def index(request):
    goods_type = GoodsType.objects.all()
    result=[]
    for type in goods_type:
        goods = type.goods_set.order_by('goods_number')
        if len(goods)>=4:
            goods=goods[:4]
        result.append({'type':type,'goods':goods})
    return render(request,'buyer/index.html',locals())

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        if email and pwd:
            user=LoginUser.objects.filter(email=email).first()
            if user:
                if user.password==setPassword(pwd):
                    response = HttpResponseRedirect('/Buyer/index/')
                    response.set_cookie('email',email)
                    response.set_cookie('pwd',pwd)
                    request.session['email']=email
                    return response
                else:
                    error='密码错误'
            else:
                error='该用户不存在，请先注册'
        else:
            error='邮箱密码不可为空'
        print(error)
    return render(request,'buyer/login.html',locals())

def logout(request):
    response=HttpResponseRedirect('/Buyer/index/')
    response.delete_cookie('email')
    response.delete_cookie('pwd')
    del request.session['email']
    return response

def register(request):
    if request.method=='POST':
        email = request.POST.get('email')
        pwd=request.POST.get('pwd')
        if email and pwd:
           user=LoginUser()
           user.email=email
           user.password=setPassword(pwd)
           user.save()
           return HttpResponseRedirect('/Buyer/login/')
        else:
            error='邮箱和密码不可为空'
    return render(request,'buyer/register.html',locals())

import math
def goods_list(request):
    keywords=request.GET.get('keywords')
    goods_type=GoodsType.objects.get(id=keywords)
    goods = goods_type.goods_set.all()
    comment=goods_type.goods_set.order_by('goods_price')[:math.ceil(len(goods)/5)]
    return render(request,'buyer/goods_list.html',locals())