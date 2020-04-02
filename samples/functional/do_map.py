#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# def square(x):
#     return x**2

# list1=[1,3,5,7]
# res=map(square,list1)
# print(type(res))
# print(list(res))


# def f(x):
#     return x * x

# print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# #匿名函数的写法
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))