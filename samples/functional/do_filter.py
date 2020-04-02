#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list1=[1,2,3,4,5,6,7,8,9,10]
# def even(x):
#     return x%2!=1
# print(list(filter(even,list1)))
# #匿名函数的写法
# print(list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10])))


# def is_odd(n):
#     return n % 2 == 1

# L = range(100)

# print(list(filter(is_odd, L)))


def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '  ', 'B', None, 'C', 'd  '])))
