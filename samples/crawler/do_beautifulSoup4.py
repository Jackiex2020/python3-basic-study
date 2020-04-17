#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:do_beautifulSoup4.py
# author:jackiex
# datetime:2020/4/16 16:04
# software: PyCharm
'''
this is function  description 
'''
from bs4 import BeautifulSoup
import requests

htmltest="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="xiaodeng"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
<a href="http://example.com/lacie" class="sister" id="xiaodeng">Lacie</a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup=BeautifulSoup(htmltest,'html.parser')

# 获取整个a标签相关属性
for k in soup.find_all('a'):
    print(k)
    print(k['class'])#查a标签的class属性
    print(k['id'])#查a标签的id值
    print(k['href'])#查a标签的href值
    print(k.string)#查a标签的string

# 通过文本分析，我们能定向抓取目标内容网页
