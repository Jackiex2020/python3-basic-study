# -*- encoding: utf-8 -*-
'''
@File    :   decorator1.py
@Time    :   2020/03/22 12:38:25
@Author  :   jackiex 
@Version :   1.0
'''
'''装饰器的定义和使用：'''

import time, random

# 定义一个闭包函数；
def outer(func):  # 将index的地址传递给func
    def inner():
        start_time = time.time()
        func()   # fun = index  即func保存了外部index函数的地址
        end_time = time.time()
        print("运行时间为%s"%(end_time - start_time))
    return inner  # 返回inner的地址

# @outer
# 原函数(希望被装饰的函数)
def index():
    time.sleep(random.randrange(1, 5))
    print("welcome to index page")

#函数调用
index = outer(index)  # 这里返回的是inner的地址，并重新赋值给index
index()