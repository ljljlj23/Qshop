from django.db import models
from Saller.models import *

ORDER_STATUS=(
    (0,'未支付'),
    (1,'已支付'),
    (2,'待发货'),
    (3,'待收货'),
    (4,'完成'),
    (5,'拒收'),
)
# 订单表
class PayOrder(models.Model):
    order_number = models.CharField(unique=True,max_length=32,verbose_name='订单编号')
    order_date = models.DateField(auto_now=True,verbose_name='订单日期')
    order_status = models.IntegerField(choices=ORDER_STATUS,verbose_name='订单状态')
    order_total = models.FloatField(verbose_name='订单总价')
    order_user = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,verbose_name='订单用户')

# 订单详情表
class OrderInfo(models.Model):
    order_id = models.ForeignKey(to=PayOrder,on_delete=models.CASCADE,verbose_name='订单表外键')
    goods = models.ForeignKey(to=Goods,on_delete=models.CASCADE,verbose_name='商品表')
    goods_count = models.IntegerField(verbose_name='商品数量')
    goods_total_price = models.FloatField(verbose_name='商品小计')
    goods_price=models.FloatField(verbose_name='商品单价')
    store_id = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,verbose_name='店铺id')

# 购物车表
class Cart(models.Model):
    goods_number = models.IntegerField(verbose_name='商品数量')
    goods_price = models.FloatField(verbose_name='商品单价')
    goods_total = models.FloatField(verbose_name='商品总价')
    goods = models.ForeignKey(to=Goods,on_delete=models.CASCADE)
    cart_user = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)
    order_number = models.CharField(max_length=32,default=0)