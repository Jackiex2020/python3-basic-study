#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
timeit模块使用,测试性能
'''

import timeit
foooo = """
sum = []
for i in range(1000):
    sum.append(i)
"""
 
print(timeit.timeit(stmt="[i for i in range(1000)]", number=100000))
print(timeit.timeit(stmt=foooo, number=100000))