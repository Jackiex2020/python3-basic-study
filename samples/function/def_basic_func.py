#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''基本的函数定义:无参数,有参数(基本数据类型),序列数据类型等'''

# def myfunc():
#     pass

def myfunc1():
 print("hello world!")

myfunc1()

# def myfunc2(a,b):
#     return a+b

# print(myfunc2(1,2))

# 字符串数据类型
# def printme(str):
#     print(str)
# printme("我爱中国!")

#打印列表中的偶数元素  参数为列表
# def printEvenNumber(mylist):
#     for i in mylist:
#         if i%2!=0:
#             print(i)

# printEvenNumber([3,5,1,4,7,34])

# 练习: 写一个函数,计算N的阶乘

# def calculateFactorial(n):
#     i=1
#     res=1
#     while i<=n:
#         res*=i
#         i+=1
#     return res
# print(calculateFactorial(5))

# 练习:写一个函数,输出斐波那契数列的第前N个数;
#  
# -*- coding: UTF-8 -*-
  
# Python 斐波那契数列实现

#定义计算斐波那契数列的第n个数的函数
'''--------递推方法-----------------'''
# def Fibonacci(n):
#     a, b = 0, 1
#     for i in range(n + 1):
#         a, b = b, a + b    # 注意这个表达式的含义
#     return a

# for i in range(10):
#     print(Fibonacci(i), end=' ')

'''--------递归函数-----------------'''

# def fib_recur(n):
#   assert n >= 0, "n > 0"
#   if n <= 1:
#     return n
#   return fib_recur(n-1) + fib_recur(n-2)

# for i in range(1, 20):
#     print(fib_recur(i), end=' ')

'''--------生成器-----------------'''

# def fib_loop_while(max):
#     a, b = 0, 1
#     while max > 0:
#         a, b = b, a + b
#         max -= 1
#         yield a


# for i in fib_loop_while(10):
#     print(i)