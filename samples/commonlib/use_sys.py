#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_sys.py
@Time    :   2020/03/25 08:31:56
@Author  :   Jackiex 
@Version :   1.0
'''
import sys
import time

# 输出当前程序的绝对路径
# print(sys.argv[0])

# 输出当前程序的工作路径 
# import os
# print(os.getcwd())
# print(os.path.abspath('.'))
# print(os.path.abspath(os.curdir))


#通过dir（sys）查看模块中可用的方法
# print(dir(sys))

for i in range(20):
    sys.stdout.write('\r')
    sys.stdout.write(' %s%%   %s' %  ((int(i/20*100)),int(i/20*100)*'*'))
    sys.stdout.flush()
    time.sleep(1)


