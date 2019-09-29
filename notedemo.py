# import requests
#
# url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"
#
# # APIID
# account = "C57458345"
# # APIkey
# password = "1226532b886870b5208d8d817d2d5f74"
#
# mobile = "13811780791"
# content = "您的验证码是：1111。请不要把验证码泄露给其他人。"
# # 请求头
# headers = {
#     "Content-type": "application/x-www-form-urlencoded",
#     "Accept": "text/plain"
# }
# # 构建发送参数
# data = {
#     "account": account,
#     "password": password,
#     "mobile": mobile,
#     "content": content,
# }
# # 发送
# response = requests.post(url,headers = headers,data=data)
#     # url--请求地址
#     # headers--请求头
#     # data--请求数据，内容
#
# print(response.content.decode())