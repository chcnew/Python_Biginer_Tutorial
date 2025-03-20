# _*_encoding: utf-8 _*_

"""
功能：邮件发送
"""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import sys
import os
import base64


class MailInfo(object):
    def __init__(self, username, password, host, sender, receiver, cc):
        self.username = username
        self.password = password
        self.host = host
        self.sender = sender
        self.receiver = receiver
        self.cc = cc

    # 发送不带附件的纯文本邮件
    def send_text_mail(self, subject, content):
        try:
            mail = MIMEText(content)  # 简单纯文本消息的邮件
            # mail = MIMEText('邮件正文', _subtype='html', _charset='utf-8') # HTML格式的邮件
            mail['Subject'] = subject
            mail['From'] = self.sender  # 需与邮件服务器的认证用户一致
            send_to = self.receiver.split(',')
            mail['To'] = self.receiver.replace(' ', ',')
            send_cc = self.cc.split(',')
            mail['Cc'] = ",".join(send_cc)
            for eachone in send_cc:
                send_to.append(eachone)
            server = smtplib.SMTP()
            try:
                server.connect(self.host, 25)  # 设置邮件服务器地址与端口
                server.login(self.username, self.password)  # 登录邮件服务器
                server.sendmail(self.sender, send_to, mail.as_string())  # 发送邮件
            except Exception as e:
                return False, '发送失败:服务器连接/发送失败【{}】'.format(str(e))
            finally:
                if server:
                    server.quit()  # 关闭邮件服务器
            return True, '发送成功'
        except Exception as e:
            return False, '发送失败:{}'.format(str(e))

    # 发送带附件的html邮件
    def send_html_mail(self, subject, content=None, files=None):
        if content or files:
            try:
                mail = MIMEMultipart()  # 构造邮件
                # mail = MIMEText('邮件正文', _subtype='html', _charset='utf-8') # HTML格式的邮件
                # 邮件主题
                mail['Subject'] = subject
                # 发送人
                mail['From'] = self.sender  # 需与邮件服务器的认证用户一致
                # 收件人
                send_to = self.receiver.split(',')
                mail['To'] = self.receiver.replace(' ', ',')
                # 抄送人
                send_cc = self.cc.split(',')
                mail['Cc'] = ",".join(send_cc)
                for eachone in send_cc:
                    send_to.append(eachone)
                # 邮件正文内容
                if content:
                    mail.attach(MIMEText(content, _subtype='html', _charset='utf-8'))
                # 添加附件
                if files:
                    for file in files:
                        # 构造附件并添加至邮件
                        try:
                            with open(file, 'rb') as f:
                                attachment = MIMEText(f.read(), 'base64', 'utf-8')
                        except Exception as e:
                            return False, '发送失败:附件["{}"]读取错误【{}】'.format(file, str(e))
                        else:
                            attachment['Content-Type'] = 'application/octet-stream'
                            file_name = os.path.split(file)[1]
                            # 下面一句是处理附件名是中文的情况
                            file_name = '=?utf-8?b?' + base64.b64encode(
                                file_name.encode()).decode() + '?='
                            attachment[
                                "Content-Disposition"] = 'attachment; filename="%s"' % file_name
                            mail.attach(attachment)
                server = smtplib.SMTP()
                try:
                    server.connect(self.host, 25)  # 设置邮件服务器地址与端口
                    server.login(self.username, self.password)  # 登录邮件服务器
                    server.sendmail(self.sender, send_to, mail.as_string())  # 发送邮件
                except Exception as e:
                    return False, '发送失败:服务器连接/发送失败【{}】'.format(str(e))
                finally:
                    if server:
                        server.quit()  # 关闭邮件服务器
                return True, '发送成功'
            except Exception as e:
                return False, '发送失败:{}'.format(str(e))
        else:
            return False, '发送失败:【邮件正文与附件都为空】'


if __name__ == "__main__":
    host = 'smtpscn.xxx.com'
    username = 'xxxxxx'
    password = 'xxxxxx'
    sender = 'xxxxxx@h-partners.com'  # 发件人
    receiver = 'xxxxxx@h-partners.com'  # 收件人
    cc = ''  # 抄送
    mailInfo = MailInfo(host, sender, username, password, receiver, cc)
    subject = "测试报告"
    # content = u"TTTTTTT"
    # flag, message = mailInfo.send_text_mail(subject, content)
    html = u'''
        <p><b>文件说明：</b></p>
        <p>1、Linux-ip:从该linux服务器上获取日志文件，获取日志文件的存在路径从cgf/pathconfig.cfg配置文件中配置</p>
        <p>2、文件名：获取到的日志文件名</p>
        <p>3、Linux路径：该日志文件存在的linux上的绝对路径</p>
        <p>4、本地路径：该日志文件存在的执行机上的绝对路径</p>
        <p>5、异常总行数：该日志文件存在fail、error关键字的异常行数</p>
    '''
    files = ['task.html']
    flag, message = mailInfo.send_html_mail(subject, html, files)
    print(message)
    sys.exit(0)
