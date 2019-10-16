from __future__ import absolute_import
from Qshop.celery import app
import time

# 创建任务
@app.task    # 将普通的函数转换为celery任务
def test():
    time.sleep(2)
    print('--------I am test task--------')
    return 'I am test task'

@app.task
def send_email(params):
    return 'send email'

@app.task
def myprint(name,age):
    time.sleep(5)
    print('%s:%s'%(name,age))
    return 'I am myprint'

@app.task
def note():
    import requests
    url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"
    account = "C57458345"
    password = "1226532b886870b5208d8d817d2d5f74"
    mobile = "13811780791"
    content = "您的验证码是：1111。请不要把验证码泄露给其他人。"
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }
    data = {
        "account": account,
        "password": password,
        "mobile": mobile,
        "content": content,
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.content.decode())
    return 'send note'