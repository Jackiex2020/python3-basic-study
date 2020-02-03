#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''闭包使用  分析以下程序执行过程'''
def set_func(func):
    def call_func():
        print("-----这次权限验证1-----")
        print("-----这次权限验证2-----")
        func()
    return call_func

def test():
     print("------test-----")

# ret=set_func(test)
# ret()

# test()  # 不装饰之前,输出
# test=set_func(test)  # 对test函数,用"set_func"装饰一下,然后返回值继续赋值给test函数
# test()

'''这就相当于在test函数之前加上@set_func代码的效果'''

test()
@set_func
def test1():
     print("------test-----")

test1()