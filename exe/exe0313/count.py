#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   count.py
@Time    :   2020/03/12 22:34:58
@Author  :   Jackiex 
@Version :   1.0
'''

'''
 40个同学的成绩;计算平均分,统计低于平均分的人数
'''

import random
li = [random.randint(50,100) for i in range(40)]    
##上面这一行是列表生成式，等同于下面三行代码
# li = []  
# for i in range(40):
#     li.append(random.randint(50,100))
# print('学生成绩如下:',li)

avgScore = sum(li) / len(li)
print('平均分:',avgScore)
lowAvgscoreNum = 0
for stuScore in li:
    if stuScore < avgScore:
        lowAvgscoreNum += 1
print('成绩低于平均分的学生人数为:',lowAvgscoreNum)

li.sort(reverse=True)
print('学生成绩从大到小排序为:',li)