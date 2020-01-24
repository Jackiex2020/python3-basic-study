#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
集合元素的显示和筛选
'''
from random import randint
import os

#先清屏
os.system("cls")

#集合元素初始化,用一个列表
data1=[randint(-10,10) for _ in range(10)]
print(data1)
s=set(data1)
print(s)

# 打印出这个集合中,能被3整除的数
# 用集合解析的方式

s1={x for x in s if x%3==0}
print(s1)

