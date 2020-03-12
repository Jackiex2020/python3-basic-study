#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   exe8.py
@Time    :   2020/03/12 20:06:35
@Author  :   Jackiex 
@Version :   1.0
'''

'''
设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资； 
将这10个员工，按照工资从高到低打印输出；
提示：可以组合使用我们的序列数据类型；
'''

employee=[
    {"No": "001", "name": "white", "years": 19,"wages":7850},
    {"No": "002","name": "jeney", "years": 10,"wages":6500},
    {"No": "003","name": "marry", "years": 20,"wages":8654},
    {"No": "004","name": "sam", "years": 9,"wages":5687},
    {"No": "005","name": "jack", "years": 9,"wages":4532},
    {"No": "006","name": "tom", "years": 9,"wages":3800}
]

employee.sort(key=lambda k:(k.get('wages', 0)))

print(employee)

