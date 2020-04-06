#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 问题: 一条直线的方程,通过X轴的值,求y轴的坐标;y=ax+b    
'''
# 第一种方式
# a=2
# b=5
# x=0
# y=a*x+b
# print("y轴坐标值为:",y)
# 缺点是:?


# 第二种方式,定义函数
# def line2(a,b,x):
#     return a*x+b
# print(line2(2,5,0))
# print(line2(2,5,1))
# print(line2(2,5,2))
#其优缺点是:?

# 第三种方式,定义函数,加上全局变量
# a=2
# b=5
# def line3(x):
#     return a*x+b
# print(line3(0))
# print(line3(1))
# print(line3(2))

# 第四种方式,定义函数,使用缺省参数
# def line4(x,a=2,b=5):
#     return a*x+b
# print(line4(0))
# print(line4(1))
# print(line4(2))
# 优缺点:?

# 第五种方式,引入面向对象的方式
# class line5(object):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __call__(self,x):
#         print(self.a*x+self.b)
     
# line5_1=line5(2,5)
# line5_1(0)   #必须定义__call__方法,实例名称才能如此调用
# line5_1(1)
# line5_1(2)
#缺点: 如果要计算多条线,会创建多个实例对象,浪费资源

# 闭包方式:能计算任意一条直线的y坐标值;也减少了存储资源的浪费
# def line6(a,b):
#     def caculate_y(x):
#         print(a*x+b)
#     return caculate_y

# line6_1=line6(2,5)
# line6_1(0)   
# line6_1(1)
# line6_1(2)

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())

