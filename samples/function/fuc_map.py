#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   fuc_map.py
@Time    :   2020/01/24 17:44:53
@Author  :   Jackiex 
@Version :   1.0
 函数: map(function, iterable, ...)
 说明:会根据提供的函数对指定序列做映射;以参数序列中的每一个元素调用 function 函数
 参数:function -- 函数;iterable -- 一个或多个序列
 返回值: 每次 function 函数返回值组成的新列表;Python 3.x 返回迭代器
'''

# here put the import lib
def square(x) :            # 计算平方数
    return x ** 2
a=map(square, [1,2,3,4,5])   
# map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
print(a)        
#输出为<map object at 0x0033CFB0>   可以看出map返回的实际上是一个map对象
print(list(a))  
#输出为[1, 4, 9]   通过list（）方式 显示出来   


ls1='ABC'
ls2='abc'
print(list(map(lambda x,y:x+y,ls1,ls2)))
#['Aa', 'Bb', 'Cc']

ls3='ABC'
ls4='ab'
print(list(map(lambda x,y:x+y,ls3,ls4)))
#['Aa', 'Bb']