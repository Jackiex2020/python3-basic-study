#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_listdir.py
@Time    :   2020/03/18 07:48:23
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib
import os
#列出指定目录下的所有文件
#files 里面既包含文件名也包含目录名

path='D:\Python38-32'
print(os.listdir(path))

files_and_dirs = os.listdir('D:\Python38-32')
  #一般来说会用一个for循环来逐个判断

print('D:\Python38-32文件夹下:')
for name in files_and_dirs:
    print(name)