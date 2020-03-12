# -*- encoding: utf-8 -*-
'''
@File    :   exe4.py
@Time    :   2020/03/12 18:58:30
@Author  :   jackiex 
@Version :   1.0
'''

'''
4  判断用户输入的年份是否为闰年
'''
year = input("请输入您要判断的年份：")
year = int(year)
result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if result:
    s = "是"
else:
    s = "不是"
print("{0}年{1}闰年".format(year, s))
