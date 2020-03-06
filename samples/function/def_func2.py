#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   def_func2.py
@Time    :   2020/03/06 08:45:22
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
