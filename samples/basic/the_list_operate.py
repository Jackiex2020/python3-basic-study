#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
列表元素的操作,初始化,增加,删除,修改
'''

from random import randint
import os

#先清屏
os.system("cls")
#  通过列表解析式,产生列表元素

lis1=[randint(1,100) for _ in range(1,6)]
print(lis1)
print(max(lis1))
print(min(lis1))

lis1.pop()
print(lis1)

lis1.insert(2,4)
print("After insert value at index 2 : ")
print(lis1)

del lis1[2]
print("After deleting value at index 2 : ")
print(lis1)


lis1.append(11)
print(lis1)

aList = [123, 'xyz', 'zara', 'abc', 123]

print("Count for 123 : ", aList.count(123))
print("Count for zara : ", aList.count('zara'))