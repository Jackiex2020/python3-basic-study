#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_re4.py
@Time    :   2020/04/14 22:17:58
@Author  :   Jackiex 
@Version :   1.0
'''

# . 匹配任意1个字符（除了\n）

import re

ret = re.match(".","BAD")
print(ret.group())

ret = re.match("t.o","too")
print(ret.group())

ret = re.match("t.o","two")
print(ret.group())

# ret = re.match("t.o","tw")
# print(ret.group())

#没匹配上,打印会报错
ret = re.match("one","two")
print(ret.group())