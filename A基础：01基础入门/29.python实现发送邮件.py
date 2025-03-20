# coding: utf-8

# 邮件发送发 （发送方地址 授权码 smtp地址 ）
# 邮件的内容
# 邮件接收方 （接收方地址）
# 模块 pyemail
# 导入方式

import smtplib  # stmp邮件方法
from email.mime.text import MIMEText

# 设置发送部分
msg_from = 'cc_blog@163.com'
pwd = 'PRKTHDOIBFAGVONB'  # 20211222 emali密码：数据库密码
to = '857339512@qq.com'

subject = '这是一份python测试发送的邮件！'
# 内容可以设置为HTML网页
content = '<h2>这是一封测试邮件！</h2>'

# 构造邮件内容
msg = MIMEText(content, 'html', 'utf-8')
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = to

# 发送邮件 实例化对象
ss = smtplib.SMTP_SSL('smtp.163.com', 465)
ss.login(msg_from, pwd)
ss.sendmail(msg_from, to, msg.as_string())

print('邮件已成功发送！')
