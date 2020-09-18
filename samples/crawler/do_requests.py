#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:do_requests.py.py
# author:jackiex
# datetime:2020/4/16 14:25
# software: PyCharm
'''
this is function  description 
'''
import requests

def getHtmlText(url):
    try:        # 网络连接有风险，异常处理很重要
        r = requests.get(url,timeout=30)
        r.raise_for_status()   # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
         return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"

    print(getHtmlText(url))