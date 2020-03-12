#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   listsort.py
@Time    :   2020/03/12 21:13:39
@Author  :   Jackiex 
@Version :   1.0
'''

'''
列表排序问题;分析列表中的元素
'''
# 列表初始化方法1
#list1=[1,2,3]

# 列表初始化方法2
# list2=list(range(10))
# print(list2)

# 列表初始化方法3  生成一定个数的随机数
#from random import randint
# import random

# list3=[random.randint(0,100) for _ in range(1,11)]
# print(list3)

'''
reverse反转/倒序排序、sort正序排序、sorted可以获取排序后的列表。
在更高级列表排序中，后两中方法还可以加入条件参数进行排序。
见:课件列表小结中,补充部分;
'''
# import random

# list3=[random.randint(0,100) for _ in range(11)]
# print(list3)
# list3.sort()
# print(list3)
# list3.reverse()
# print(list3)



# 复杂列表元素排序问题
lst = [('d', 2), ('a', 4), ('b', 3), ('c', 2)]
 
# 按照value排序
lst.sort(key=lambda k: k[1])
print(lst)
 
# 按照key排序
lst.sort(key=lambda k: k[0])
print(lst)
 
# # 先按value排序再按key排序
# lst.sort(key=lambda k: (k[1], k[0]))
# print(lst)
 
# # 输出---->>>
# [('d', 2), ('c', 2), ('b', 3), ('a', 4)]
# [('a', 4), ('b', 3), ('c', 2), ('d', 2)]
# [('c', 2), ('d', 2), ('b', 3), ('a', 4)]
 
 
# # 复杂的dict，按照dict对象中某一个属性进行排序
# lst = [{'level': 19, 'star': 36, 'time': 1},
#        {'level': 20, 'star': 40, 'time': 2},
#        {'level': 20, 'star': 40, 'time': 3},
#        {'level': 20, 'star': 40, 'time': 4},
#        {'level': 20, 'star': 40, 'time': 5},
#        {'level': 18, 'star': 40, 'time': 1}]
 
# # 需求:
# # level越大越靠前;
# # level相同, star越大越靠前;
# # level和star相同, time越小越靠前;
 
# # 先按time排序
# lst.sort(key=lambda k: (k.get('time', 0)))
 
# # 再按照level和star顺序
# # reverse=True表示反序排列，默认正序排列
# lst.sort(key=lambda k: (k.get('level', 0), k.get('star', 0)), reverse=True)
 
 
 
# for idx, r in enumerate(lst):
#     print 'idx[%d]\tlevel: %d\t star: %d\t time: %d\t' % (idx, r['level'], r['star'],r['time'])
 
# # 输出---->>>
# idx[0]   level: 20       star: 40        time: 2        
# idx[1]   level: 20       star: 40        time: 3        
# idx[2]   level: 20       star: 40        time: 4        
# idx[3]   level: 20       star: 40        time: 5        
# idx[4]   level: 19       star: 36        time: 1        
# idx[5]   level: 18       star: 40        time: 1  
