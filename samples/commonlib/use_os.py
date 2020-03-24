#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
#清理屏幕
os.system("cls")

# 在服务器的D盘创建一个文件夹
#os.mkdir('D:\\123hak')

#查看环境变量
os.environ
print(os.environ)

#如何使用python删除一个文件？
# import os
# file = r'D:\test.txt'
# if os.path.exists(file):
#     os.remove(file)
#     print('delete success')
# else:
#     print('no such file:%s' % file)

#使用代码实现查看列举目录下的所有文件。
# import os
# def dirpath(lpath, lfilelist):
#     list = os.listdir(lpath)
#     for f in list:
#         file = os.path.join(lpath, f)  # 拼接完整的路径
#         if os.path.isdir(file):  # 判断如果为文件夹则进行递归遍历
#             dirpath(file, lfilelist)
#         else:
#             lfilelist.append(file)
#     return lfilelist
#
# lfilelist = dirpath(os.getcwd(), [])
# for f in lfilelist:
#     print(f)

