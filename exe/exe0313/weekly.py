# -*- encoding: utf-8 -*-
'''
@File    :   weekly.py
@Time    :   2020/03/25 13:35:51
@Author  :   jackiex 
@Version :   1.0
'''

'''判断当前日期，是今年的第几周'''
# here put the import lib

import time
from datetime import datetime

print(datetime.now().isocalendar())
# print(time.strftime("%W"))

# today = datetime.now().weekday()
# print(today)

# week = datetime.strptime("20171225","%Y%m%d").strftime("%W")
# print(week)