#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_timedate.py
@Time    :   2020/03/19 09:05:02
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib
from datetime import datetime
now = datetime.now() # 获取当前datetime 

# print(type(now))
print(now)

#去掉毫秒
d = datetime.now().replace(microsecond=0) 
print(d)

# print(now.date())
# print(now.time())
# print(now.timestamp())

# #当前时间
# print(datetime.now())
# #取年
# print(datetime.now().year)
# #取月
# print(datetime.now().month)
# #取日
# print(datetime.now().day)
# #取时
# print(datetime.now().hour)
# #取分
# print(datetime.now().minute)
# #取秒
# print(datetime.now().second)

# dt = datetime(2015, 4, 19, 12, 20,39) # 用指定日期时间创建datetime
# print(dt)