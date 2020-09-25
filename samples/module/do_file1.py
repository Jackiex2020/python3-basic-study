#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:do_file1.py
# author:jackiex
# datetime:2020/9/25 17:33
# software: PyCharm
'''
this is function  description 
'''
# import module your need

from file1 import  func1,func2    # 程序运行不会报错；标红
#from .file1 import func2,func1   # 会报错，相对导入的程序中，包含了程序入口
#from samples.module.file1 import  func1,func2

def test():
    func1()
    func2()

if __name__ == '__main__':
    test()