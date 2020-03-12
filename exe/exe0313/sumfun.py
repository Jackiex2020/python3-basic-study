#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   sumfun.py
@Time    :   2020/03/12 23:08:23
@Author  :   Jackiex 
@Version :   1.0
'''

# 写一个函数，接收n个数字，求这些参数数字的和
def sum_func(*args):
    sm = 0
    for i in args:
        sm += i
    return sm
 
print(sum_func(1,2,3,7,4,5,6))