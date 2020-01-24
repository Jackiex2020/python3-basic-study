#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
列表元素的显示和筛选,并比较其性能
'''

from random import randint
import timeit

#循环方式

# data=[1,-3,23,-23,-34,56,34,46]
# res=[]
# for x in  data:
#     if x>=0:
#         res.append(x)
# print(res)
data1=[randint(-10,10) for _ in range(10)]
print(data1)
print(list(filter(lambda x:x>=0,data1)))

#print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
print(timeit.timeit(stmt='filter(lambda x:x>=0,[1,2,-4,2,34])', number=1))

#timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000)

#列表解析，筛选列表中大于0的数
print([x for x in data1 if x>=0])
print(timeit.timeit(stmt='[x for x in [-2,3,5,-4,6,-21,3,-5,6.23] if x>=0]',number=1))