from HTMLTestRunner import HTMLTestRunner
import unittest
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
from public import mail
import os
import time

def send_email(filename):
    mail_host = 'smtp.exmail.qq.com'
    mail_user = mail.mail_user #邮箱名 '282474952@qq.com'
    mail_pass = mail.mail_pass #密码：’#￥%......‘

    sender = mail.sender # 发送邮箱名
    receivers=['282474952@qq.com','pod@163.com'] # 收件人,列表形式存储，可以多个邮箱

    message = MIMEMultipart('related')

    f = open(filename,'rb')
    mail_body = f.read()
    att = MIMEText(mail_body,'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="report.html'
    message.attach(att)
    f.close()

    msg = MIMEText(mail_body,'html','utf-8')
    message.attach(msg)
    message['From']=sender
    message['To'] = ",".join(receivers)
    message['Subject'] = Header("接口自动化测试报告",'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.login(mail_user,mail_pass)
    smtp.sendmail(sender,receivers,message.as_string())
    smtp.quit()

def report(testreport): # 查找最新的测试报告
    lists = os.listdir(testreport) #返回指定的文件夹包含的文件或者文件夹名字的列表
    lists.sort(key=lambda fn:os.path.getatime(testreport+ "\\" + fn)) # 通过sort()方法 重新按时间对目录下的文件进行排序_
    filename = os.path.join(testreport,lists[-1])
    print(filename)
    return filename

if __name__ =="__main__":
    # testdata.init_data() #初始化接口测试数据
    # 指定测试用例为当前文件夹下的test_case目录
    test_dir = './test_case'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py') #加载test_dir目录下所有以 _test.py 结尾的文件

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='qiaoba testing Interface Test Report',
                            description='The result are following:')
    runner.run(discover)
    fp.close()

    test_report = './report'
    rep = report(test_report)
    send_email(rep)