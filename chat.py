#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
微信消息功能监听接口
环境要求：python2.7 暂不支持python3
'''

import itchat
itchat.auto_login(hotReload=True)

def test():
    for i in range(5):
        itchat.send(str(i))

if __name__ == '__main__':
    test()
