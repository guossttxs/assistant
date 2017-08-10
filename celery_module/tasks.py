#!/usr/bin/env python
#-*- coding:utf8 -*-

import os
import sys
sys.path.append(os.path.abspath(__file__).split('celery_module')[0])
import requests
from celery_module.celery import celery
from pro_config import project_services
from mail import send_mail

@celery.task
def add(x, y):
    return x+y

@celery.task
def inspection_service():
    for pro in project_services:
        try:
            response = requests.get(pro['url'])
            code = response.status_code
            if code != 200:
                content = '{}请求失败, code: {}, ip: {}'.format(pro['description'], code, pro['ip'])
                send_mail(content)
        except Exception as e:
            print(e)
            content = '{}服务故障, ip:{}'.format(pro['description'], pro['ip'])
            send_mail(content)

if __name__ == '__main__':
    pass