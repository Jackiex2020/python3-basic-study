#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

aList = [123, 'xyz', 'zara', 'abc'];
aTuple = tuple(aList)
 
print("Tuple elements : ", aTuple,type(aTuple))


tup = (1, 2, ['a', 'b', 'c'], 'd', 'e', ('gu', 'tang'))

print ("tup[0] =",tup[0]) # 打印索引为0的元素
#输出结果
#tup[0] = 1

print ("tup[1:] =",tup[1:])   #从索引为1到最后一个元素
#输出结果
#tup[1:] = (2, ['a', 'b', 'c'], 'd', 'e', ('gu', 'tang'))

print ("tup[:-1] =",tup[:-1])  # 到倒第二个元素但不包含第二个
#输出结果
#tup[:-1] = (1, 2, ['a', 'b', 'c'], 'd', 'e')

print ("tup[1::1] =",tup[1::1]) # 等价于tup[1:]   从左到右一个个去取，步长为1
#输出结果
#tup[1::1] = (2, ['a', 'b', 'c'], 'd', 'e', ('gu', 'tang'))

print ("tup[1::2] =",tup[1::2]) #从左到右隔一个去取  步长为2
#输出结果
#tup[1::2] = (2, 'd', ('gu', 'tang'))

print ("tup[::-1]",tup[::-1])   # 反向输出 步长为1
#输出结果
#tup[::-1] (('gu', 'tang'), 'e', 'd', ['a', 'b', 'c'], 2, 1)

print ("tup[::-2]",tup[::-2])   # 反向输出 步长为2（隔一个去取））
#输出结果
#tup[::-2] (('gu', 'tang'), 'd', 2)