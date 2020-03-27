#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
#清理屏幕
os.system("cls")

# 在服务器的D盘创建一个文件夹
# os.mkdir('D:\\234hak')

#查看环境变量
# os.environ
# print(os.environ)

#如何使用python删除一个文件？
# import os
# file = r'D:\test.txt'
# if os.path.exists(file):
#     os.remove(file)
#     print('delete success')
# else:
#     print('no such file:%s' % file)


# list = os.listdir(os.getcwd())
# print(list)

#使用代码实现查看列举目录下的所有文件。
# def dirpath(lpath, lfilelist):
#     list = os.listdir(lpath)
#     for f in list:
#         file = os.path.join(lpath, f)  # 拼接完整的路径
#         if os.path.isdir(file):  # 判断如果为文件夹则进行递归遍历
#             dirpath(file, lfilelist)
#         else:
#             lfilelist.append(file)
#     return lfilelist

# lfilelist = dirpath(os.getcwd(), [])
# for f in lfilelist:
#     print(f)

import sys
 
#获取脚本文件的当前路径 
# def cur_file_dir():
 
#      #获取脚本路径 
#      path = sys.path[0] 
#      #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
 
#      if os.path.isdir(path): 
#          return path 
#      elif os.path.isfile(path): 
#          return os.path.dirname(path)

# cur_file_dir()

# # 获取当前工作目录

print(os.getcwd())#获得当前工作目录 
print(os.path.abspath('.'))#获得当前工作目录 
print(os.path.abspath('..'))#获得当前工作目录的父目录 
print(os.path.abspath(os.curdir))#获得当前工作目录