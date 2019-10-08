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
def myprint(name,age):
    time.sleep(5)
    print('%s:%s'%(name,age))
    return 'I am myprint'