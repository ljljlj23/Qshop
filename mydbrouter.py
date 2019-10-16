import random

class Router(object):
    def db_for_read(self,model,**hints):
        # 返回读操作要使用的数据库
        return random.choice(['slave','slave2'])
    def db_for_write(self):
        # 返回写操作要使用的数据库
        return 'default'