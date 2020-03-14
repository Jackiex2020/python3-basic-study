#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_fileread.py
@Time    :   2020/03/14 20:31:07
@Author  :   Jackiex 
@Version :   1.0
'''

# 打开文件  并读取内容输出
f = open("foo.txt", "r")
str = f.read()
print(str)

# 关闭打开的文件
f.close()