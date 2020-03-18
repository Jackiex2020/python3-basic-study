#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_fileopen.py
@Time    :   2020/03/14 20:32:30
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib


'''文件操作'''
import os

print("当前工作路径：",os.getcwd())


# 打开一个文件
#f = open("foo.txt", "w")

# 如果每次运行，都将内容添加到末尾：
#f = open("foo.txt", "a")

# 如果想打开指定地址的文件
# 默认在当前工作路径打开文件
# . 代表当前工作的路径，.. 代表当前路径的上一级路径
#f = open("../foo123.txt", "a")

#打开和py文件同一级目录下的文件;open("foo.txt", "a")需要在py文件所在的目录下运行程序即可;

# 打开任意指定位置的文件

f = open(r'E:\flask\foo222.txt', 'w', encoding='gbk')   #  r：代表处理不转义现象;正则表达式一种

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()

#print("内容写入完毕，请到此地址查看:",os.getcwd())

# 去文件系统，去查看这个被打开的文件，看是否写入了内容；
# 删除foo.txt，继续运行


