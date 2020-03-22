# -*- encoding: utf-8 -*-
'''
@File    :   decorator2.py
@Time    :   2020/03/22 12:40:59
@Author  :   jackiex 
@Version :   1.0
'''

'''有参数装饰器'''
import time, random

# 定义一个闭包函数；作为装饰器
def outer(func):  # 将index的地址传递给func
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)   # fun = index  即func保存了外部index函数的地址
        end_time = time.time()
        print("运行时间为%s"%(end_time - start_time))
    return inner  # 返回inner的地址

# 原函数(希望被装饰的函数)
@outer
def index():
    time.sleep(random.randrange(1, 5))
    print("welcome to index page")

#函数调用
index()