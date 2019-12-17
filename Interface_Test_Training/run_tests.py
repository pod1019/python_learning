from HTMLTestRunner import HTMLTestRunner
import unittest
import smtplib # 发送邮件模块
from email.mime.text import MIMEText # 定义邮件内容
from email.header import Header # 定义邮件标题
from email.mime.multipart import MIMEMultipart #定义邮件附件
from public import mail
import os,sys
import time
sys.path.append('./test_case')
sys.path.append('./public')

# 定义发送邮件
def send_email(filename):
    # 发送邮件的
    # mail_host = 'smtp.exmail.qq.com'
    mail_host = 'smtp.163.com'
    mail_user = mail.mail_user #邮箱名 '282474952@qq.com'
    mail_pass = mail.mail_pass #密码：’#￥%......‘

    sender = mail.sender # 发送邮箱名
    receiver=['282474952@qq.com','pod1019@163.com'] # 收件人,列表形式存储，可以多个邮箱

    message = MIMEMultipart('related')

    f = open(filename,'rb')
    # 读取邮件正文
    mail_body = f.read()
    att = MIMEText(mail_body,'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="report.html'
    message.attach(att)
    f.close()

    # 编写邮件正文
    msg = MIMEText(mail_body,'html','utf-8')
    message.attach(msg)
    message['From']=sender
    message['To'] = ",".join(receiver)
    message['Subject'] = Header("接口自动化测试报告", 'utf-8')

    '''#建立和SMTP邮件服务器的连接 '''
    smtp = smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.login(mail_user,mail_pass)
    smtp.sendmail(sender,receiver,message.as_string())
    smtp.quit()

def report(testreport): # 查找最新的测试报告
    lists = os.listdir(testreport) #返回指定的文件夹包含的文件或者文件夹名字的列表
    lists.sort(key=lambda fn:   os.path.getatime(testreport + "\\" + fn)) # 通过sort()方法 重新按时间对目录下的文件进行排序_
    filename = os.path.join(testreport,lists[-1]) #通过lists[-1] 取出最新生成的

    print(filename)
    return filename

if __name__ =="__main__":
    # testdata.init_data() #初始化接口测试数据
    # 指定测试用例存放的目录为当前文件夹下的test_case目录
    test_dir = './test_case' #传给discover方法
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py') #discover自动识别用例。加载test_dir目录下所有以 _test.py 结尾的文件

    now = time.strftime("%Y-%m-%d %H_%M_%S") #时间戳
    filename = './report/' + now + '_result.html' #生成文件名，赋给filename
    fp = open(filename,'wb') # 以写的方式打开filename

    #stream放生成报告的路径
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况：')
    runner.run(discover) #调用HTMLTestReport文件下的run方法
    fp.close()

    test_report = './report'
    rep = report(test_report)
    send_email(rep)