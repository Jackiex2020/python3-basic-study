#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_re5.py
@Time    :   2020/04/14 22:25:24
@Author  :   Jackiex 
@Version :   1.0
'''
# 匹配多个字符
# 需求：匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无


import re

ret = re.match("[A-Z][a-z]*","M")
print(ret.group())

ret = re.match("[A-Z][a-z]*","MnnM")
print(ret.group())

ret = re.match("[A-Z][a-z]*","Aabcdef")
print(ret.group())