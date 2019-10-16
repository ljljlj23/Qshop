from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
#
class MiddleWareTest(MiddlewareMixin):
    pass
#     # 处理请求
#     def process_request(self,request):
#         # 封杀非法ip
#         # 1.获取请求ip
#         # 2.判断ip
#         # 3.返回响应
#         ip = request.META.get('REMOTE_ADDR')
#         print('我是process_request')
#         if ip == '10.10.107.2':
#             return HttpResponse('你被禁用了')
#     # 还可以对request携带的参数进行预处理
#
#     def process_view(self,request,callback,callback_args,callback_kwargs):
#         '''
#         :param request: 请求对象
#         :param callback:对应的视图函数，访问的是哪个视图函数，callback就是哪个函数
#         :param callback_args: 元组，视图函数的参数
#         :param callback_kwargs: 字典，视图函数的参数
#         :return:
#         '''
#         print('我是process_view')
#         print('callback:',callback)    # callback: <function index at 0x0000000004C6A840>
#
#     # def process_exception(self,request,exception):
#     #     '''
#     #     :param request: 请求对象
#     #     :param exception: 异常信息
#     #     '''
#     #     print('我是process_exception')
#     #     # 将异常写入文件error.log
#     #     import os
#     #     import time
#     #     from Qshop.settings import BASE_DIR
#     #     file = os.path.join(BASE_DIR,'error.log')
#     #     with open(file,'a') as f:
#     #         now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
#     #         content = '[%s]:%s'%(now,exception)
#     #         f.write(content + '\n')
#     #     # 给boss发送短信/邮件 异步
#     #     # from CeleryTask.tasks import send_email
#     #     # params = {
#     #     #     'content':'报错了'
#     #     # }
#     #     # send_email.delay(params)
#     #     return HttpResponse('代码报错了 <br> %s'% exception)
#
#     def process_template_response(self,request,response):
#         print('我是process_template_response')
#         return response
#
#     def process_response(self,request,response):
#         '''
#         :param request: 请求对象
#         :param response: 响应对象
#         '''
#         print('我是process_response')
#         return response