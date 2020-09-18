#!/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib import  request

# python2当中的写法
# response = urllib.urlopen("http://www.baidu.com")
url = "http://www.baidu.com"
headers = { 'User-Agent':user_agent}

req = request.Request(url, headers)

response = request.urlopen(req)

print(response.read())
