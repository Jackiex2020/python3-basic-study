# -*- encoding: utf-8 -*-
'''
@File    :   exe3.py
@Time    :   2020/03/12 18:55:46
@Author  :   jackiex 
@Version :   1.0
'''
'''
  定义2个列表，并初始化；找出这2个列表中，相同的元素并输出；
'''
l1 = [11, 22, 33]
l2 = [22, 33, 44]
# for i1 in l1:
#     for i2 in l2:
#         if i1 == i2:
#             print(i1)

set1=set(l1)
set2=set(l2)

print(set1&set2)