#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:do_BeautyfelSoup2.py
# author:jackiex
# datetime:2020/4/16 14:49
# software: PyCharm
'''
   BeautifulSoup模块的用法
'''
from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3
urllib3.disable_warnings()

baseurl='https://python123.io/ws/demo.html'
baseurl='https://www.ncepu.edu.cn/index.htm'
baseurl='https://www.ncepu.edu.cn/index.htm'

html=requests.get(baseurl)

soup=BeautifulSoup(html.text,'html.parser')

print(soup.title)
print(soup.a)           # 打印第一个a标签
print(soup.a.name)      # 打印第一个a标签的名字
print(soup.a.parent.name)




#获取整个a标签的内容
# a_tag=soup.find_all('a')
# for url in a_tag:
#     # print(url["href"])
#     print(url)

