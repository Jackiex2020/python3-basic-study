#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打印list:
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)

# 打印数字 0 - 9
# for x in range(10):
#     print(x)

for i in range(1, 10):
    for j in range(1, i+1):
        print('{0}x{1}={2}\t'.format(j, i, i*j), end='')
    print()