#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_timedelta.py
@Time    :   2020/03/19 09:34:55
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib
from datetime import timedelta
from datetime import datetime

time1 = datetime(2016, 10, 20)
time2 = datetime(2015, 11, 2)
"""计算天数差值"""
print((time1-time2).days)
"""计算两个日期之间相隔的秒数"""
print((time1-time2).total_seconds()) 