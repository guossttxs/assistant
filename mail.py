#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
发送邮件有关的接口
SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
'''

import smtplib
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
from pro_config import mail_username, mail_user, mail_port, mail_host, mail_to, mail_pwd

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(msg):
    '''
    发送邮件
    :param msg:
    :return:
    '''
    msg = MIMEText(msg, 'plain', 'utf-8')
    msg['From'] = _format_addr('1亿年后的自己 <%s>' % mail_username)
    msg['To'] = ';'.join(mail_to)
    msg['Subject'] = Header('server error', 'utf-8').encode()

    try:
        s = smtplib.SMTP_SSL(mail_host, mail_port)
        s.connect(mail_host)
        s.login(mail_user, mail_pwd)
        s.sendmail(mail_username, mail_to, msg.as_string())
        s.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    send_mail('患者端服务停止')