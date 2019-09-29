import smtplib
from email.mime.text import MIMEText

# 构建邮件
# 主题
subject = 'demo'
# 内容
content = '比心心'
# 发件人
sender = 'ljljlj23@163.com'
# 收件人
receiver ='1074819863@qq.com'
# 服务密码
password = 'ljljlj23'
# MIMEtext
# 参数：发送内容 内容类型 编码
message = MIMEText(content,'plain','utf-8')
message["Subject"] = subject
message["From"] = sender
message["To"] = receiver

# 发送
smtp = smtplib.SMTP_SSL('smtp.163.com',465)
# 发件人登录
smtp.login(sender,password)
# 参数：发件人 收件人（需要列表） 发送邮箱，类似一种json
smtp.sendmail(sender,receiver.split(","),message.as_string())
smtp.close()