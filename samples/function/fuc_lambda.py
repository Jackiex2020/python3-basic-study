#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
1 匿名函数lambda：是指一类无需定义标识符（函数名）的函数或子程序。
lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。
2 lambda匿名函数的格式：冒号前是参数，可以有多个，用逗号隔开，冒号右边的为表达式。
其实lambda返回值是一个函数的地址，也就是函数对象;
3 使用场景:用在需要封装特殊的、非重用代码上，避免令我的代码充斥着大量单行函数。
'''


import os

os.system('cls')

#这是一个单行语句函数
# def sum(x,y):
#         return x+y

# '''
# 用lambda来实现：
# '''
# p = lambda x,y:x+y
# print(p(4,6))

# '''
# 例2：传入一个参数的lambda函数
# '''
# a=lambda x:x*x
# print(a(3))       # 注意：这里直接a(3)可以执行，但没有输出的，前面的print不能少

# '''
# 匿名函数通常被用作高阶函数(higher-order function,参数为函数的函数)的参数。
# 比如，几个内置函数：filter(),map(),reduce()。
# 经常需要将匿名函数作为参数
# '''
lis1 = [1, 2, 3, 4, 5, 6, 7, 8]
res = filter(lambda x: x%2==0, lis1) #返回偶数
print(list(res))




# squared = map(lambda x: x**2, [1, 2, 3, 4, 5])
# print(list(squared))