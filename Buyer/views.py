from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
import hashlib
from django.core.paginator import Paginator
from Saller.models import *
from Buyer.models import *
from alipay import AliPay
from Qshop.settings import alipay_private_key_string,alipay_public_key_string

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
            url=request.META.get('HTTP_REFERER')
            response = HttpResponseRedirect('/Buyer/login/')
            response.set_cookie('url',url)
            return response
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
                    if request.COOKIES.get('url'):
                        response = HttpResponseRedirect(request.COOKIES.get('url'))
                    else:
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
    return render(request,'buyer/login.html',locals())

def logout(request):
    url = request.META.get('HTTP_REFERER')
    response=HttpResponseRedirect(url)
    for one in request.COOKIES.keys():
        response.delete_cookie(one)
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
def goods_list(request,page):
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
        print('goods:',goods)
    elif req_type=='search':
        goods = Goods.objects.filter(goods_name__contains=keywords)
    comment = goods.order_by('goods_price')[:math.ceil(len(goods) / 5)]
    paginator=Paginator(goods,10)
    page_obj=paginator.page(int(page))
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
        orderinfo.order_id_id=payorder.id
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

def AlipayView(request):
    order_id=request.GET.get('order_id')    # 订单ID
    payorder=PayOrder.objects.get(id=order_id)
    # 实例化支付对象
    alipay = AliPay(
        appid='2016101300673951',
        app_notify_url=None,
        app_private_key_string=alipay_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",
    )
    # 实例化订单
    order_string = alipay.api_alipay_trade_page_pay(
        subject='天天生鲜',  # 交易主题
        out_trade_no=payorder.order_number,  # 订单号
        total_amount=str(payorder.order_total),  # 交易总金额
        return_url='http://127.0.0.1:8000/Buyer/payresult/',  # 请求支付之后及时回调的一个接口
        notify_url='http://127.0.0.1:8000/Buyer/payresult/'  # 通知地址
    )
    # 发送支付请求
    # 请求地址：支付网关+实例化订单
    result = 'https://openapi.alipaydev.com/gateway.do?' + order_string
    return HttpResponseRedirect(result)

def payresult(request):
    order_number = request.GET.get('out_trade_no')
    payorder = PayOrder.objects.get(order_number=order_number)
    payorder.order_status=1
    payorder.save()
    return render(request,'buyer/payresult.html',locals())

# 添加购物车
def add_cart(request):
    '''
    使用post请求，完成添加购物车功能
    '''
    result = {'code':'10000','msg':''}
    if request.method=='POST':
        goods_id = request.POST.get('goods_id')
        count = int(request.POST.get('count','1'))    # 默认值1
        user_id = request.COOKIES.get('userid')
        goods = Goods.objects.get(id=goods_id)
        cart = Cart()
        cart.goods_number = count
        cart.goods_price = goods.goods_price
        cart.goods_total = goods.goods_price*count
        cart.goods = goods
        cart.cart_user = LoginUser.objects.get(id=user_id)
        cart.save()
        result['msg']='成功加入购物车'
    else:
        result['code']=10001
        result['msg']='请求方式不正确'
    return JsonResponse(result)

@loginValid
def cart(request):
    user_id = request.COOKIES.get('userid')
    carts = Cart.objects.filter(cart_user_id=user_id,).order_by('-id')    # 晚添加的在上面
    cart_list = []
    for one in carts:
        # 说明有订单号
        if one.order_number != '0':
            payorder = PayOrder.objects.get(order_number=one.order_number)
            if payorder.order_status == 0:
                cart_list.append(one)
        else:
            cart_list.append(one)
    count = len(cart_list)
    return render(request,'buyer/cart.html',locals())

@loginValid
def place_order_more(request):
    data=request.GET
    userid = request.COOKIES.get('userid')
    # 通过获取前端get请求的参数，找到goods_id和对应的数量
    request_data=[]
    for key,value in data.items():
        if key.startswith('goods'):
            goods_id = key.split('_')[1]
            count = request.GET.get('count_'+goods_id)
            cart_id = key.split('_')[2]
            request_data.append((int(goods_id),int(count),int(cart_id)))
    if request_data:
        payorder = PayOrder()
        order_number = str(time.time()).replace('.', '')
        payorder.order_number = order_number
        payorder.order_status = 0
        payorder.order_total = 0
        order_total = 0
        total_count = 0
        payorder.order_user = LoginUser.objects.get(id=userid)
        payorder.save()
        for goods_id_one,count_one,cart_id in request_data:
            goods = Goods.objects.get(id=goods_id_one)
            orderinfo = OrderInfo()
            orderinfo.order_id_id = payorder.id
            orderinfo.goods = goods
            orderinfo.goods_count = count_one
            orderinfo.goods_price = goods.goods_price
            orderinfo.goods_total_price = goods.goods_price * count_one
            orderinfo.store_id = goods.goods_store
            orderinfo.save()
            order_total+=orderinfo.goods_total_price
            total_count+=count_one

            cart = Cart.objects.get(id=cart_id)
            cart.order_number = order_number
            cart.save()

        payorder.order_total=order_total
        payorder.save()
    return render(request,'buyer/place_order.html',locals())

@loginValid
def user_center_order(request,page):
    user_id = request.COOKIES.get('userid')
    user = LoginUser.objects.get(id=user_id)
    payorder = user.payorder_set.order_by('-order_date','order_status')
    paginator = Paginator(payorder, 2)
    page_obj = paginator.page(int(page))
    return render(request,'buyer/user_center_order.html',locals())