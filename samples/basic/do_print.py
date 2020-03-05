#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print('The quick brown fox', 'jumps over', 'the lazy dog')
# print(300)
# print(100 + 200)
# print('100 + 200 =', 100 + 200)


print("How old are you?",end='')
age = input()
print("How tall are you?",end='  ')
height = input()
print("How much do you weight?",end='   ')
weight = input()
 
# 多种输出方式
#print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print('your age：{0} \nyour height：{1} \nyour weigth:{2}'.format(age, height,weight))

