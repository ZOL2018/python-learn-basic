# coding=utf-8

import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"

import smtplib
from email.mime.text import MIMEText

mailto_list = ["YYY@YYY.com"]
mail_host = "smtp.XXX.com"  # 设置服务器
mail_user = "XXX"  # 用户名
mail_pass = "XXXX"  # 口令
mail_postfix = "XXX.com"  # 发件箱的后缀


def send_mail(to_list, sub, content):  # to_list：收件人；sub：主题；content：邮件内容
    me = "hello" + "<" + mail_user + "@" + mail_postfix + ">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content, _subtype='html', _charset='gb2312')  # 创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub  # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  # 连接smtp服务器
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(me, to_list, msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    if send_mail(mailto_list, "hello", "<a href='http://www.w3cschool.cn/'>W3Cschool</a>"):
        print "发送成功"
    else:
        print "发送失败"
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

#创建一个带附件的实例
msg = MIMEMultipart()

#构造附件1
att1 = MIMEText(open('d:\\123.rar', 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="123.doc"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)

#构造附件2
att2 = MIMEText(open('d:\\123.txt', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="123.txt"'
msg.attach(att2)

#加邮件头
msg['to'] = 'YYY@YYY.com'
msg['from'] = 'XXX@XXX.com'
msg['subject'] = 'hello world'
#发送邮件
try:
    server = smtplib.SMTP()
    server.connect('smtp.XXX.com')
    server.login('XXX','XXXXX')#XXX为用户名，XXXXX为密码
    server.sendmail(msg['from'], msg['to'],msg.as_string())
    server.quit()
    print '发送成功'
except Exception, e:
    print str(e) 