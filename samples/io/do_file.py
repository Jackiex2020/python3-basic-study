# -*- encoding: utf-8 -*-
'''
@File    :   do_file.py
@Time    :   2020/03/13 13:02:00
@Author  :   jackiex 
@Version :   1.0
'''

'''文件操作'''
import os

print("当前工作路径：",os.getcwd())


# 打开一个文件
#f = open("foo.txt", "w")
# 如果每次运行，都将内容添加到末尾：
#f = open("foo.txt", "a")

# 如果想打开指定地址的文件
# . 代表当前的路径，.. 代表当前路径的上一级路径
f = open("./foo.txt", "a")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()

#print("内容写入完毕，请到此地址查看:",os.getcwd())

# 去文件系统，去查看这个被打开的文件，看是否写入了内容；
# 删除foo.txt，继续运行


