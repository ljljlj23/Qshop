from django.shortcuts import render
from django.http import HttpResponseRedirect
import hashlib
from Saller.models import *
from Buyer.models import *

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
            user=LoginUser.objects.filter(email=email,user_type=1).first()
            if user:
                if user.password==setPassword(pwd):
                    response = HttpResponseRedirect('/Buyer/index/')
                    response.set_cookie('userid',user.id)
                    response.set_cookie('email',email)
                    response.set_cookie('pwd',pwd)
                    response.set_cookie('user_type',user.user_type)
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
    response.delete_cookie('user_type')
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
    '''
    如果req_type==findall
        是查看更多的功能
    如果req_type==search
        是模糊查询的功能
    '''
    keywords=request.GET.get('keywords')
    req_type=request.GET.get('req_type')
    if req_type=='findall':
        goods_type=GoodsType.objects.get(id=keywords)
        goods = goods_type.goods_set.all()
    elif req_type=='search':
        goods = Goods.objects.filter(goods_name__contains=keywords)
    comment = goods.order_by('goods_price')[:math.ceil(len(goods) / 5)]
    return render(request,'buyer/goods_list.html',locals())

def goods_detail(request):
    id=request.GET.get('id')
    good = Goods.objects.get(id=id)
    return render(request,'buyer/goods_detail.html',locals())
# 用户中心
@loginValid
def user_center_info(request):
    return render(request,'buyer/user_center_info.html',locals())
# 支付页面
import time
@loginValid
def place_order(request):
    goods_id = request.GET.get('goods_id')
    goods_count = request.GET.get('goods_count')
    user_id = request.COOKIES.get('userid')
    if goods_id and goods_count:
        goods_id=int(goods_id)
        goods_count=int(goods_count)
        goods = Goods.objects.get(id=goods_id)
        payorder = PayOrder()
        order_number=str(time.time()).replace('.','')
        payorder.order_number=order_number
        payorder.order_status=0
        payorder.order_total=goods.goods_price*goods_count
        payorder.order_user=LoginUser.objects.get(id=user_id)
        payorder.save()
        orderinfo = OrderInfo()
        orderinfo.order_id=payorder
        orderinfo.goods=goods
        orderinfo.goods_count = goods_count
        orderinfo.goods_price=goods.goods_price
        orderinfo.goods_total_price = goods.goods_price*goods_count
        orderinfo.store_id=goods.goods_store
        orderinfo.save()

        total_count=0
        all_infos=payorder.orderinfo_set.all()
        for one in all_infos:
            total_count+=one.goods_count
    return render(request,'buyer/place_order.html',locals())