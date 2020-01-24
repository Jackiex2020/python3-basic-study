#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 字典元素筛选
'''
from random import randint
import os

#先清屏
os.system("cls")
#定义字典
dic1={ x:randint(60,100) for x in range(1,11)}
print(dic1)

# for value in dic1.values():
#     print('value = {}'.format(value))

for key,value in dic1.items():
    print('{key}:{value}'.format(key = key, value = value))

#筛选出分数高于90分的同学
d={k:v for k,v in dic1.items() if v>90}
#print(d)
print("90分以上的记录:")
for key,value in d.items():
    print('{key}:{value}'.format(key = key, value = value))