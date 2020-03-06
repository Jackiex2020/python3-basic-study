#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   def_fun1.py
@Time    :   2020/03/06 08:22:14
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib
def ChangeInt( a ):
    print("a重新赋值之前的地址:",id(a))
    a = 10
    print("a重新赋值后的值:",a)
    print("a重新赋值后的地址:",id(a))
 
b = 2
print('b的地址:',id(b))
ChangeInt(b)
print('传了参数后的b的地址:',id(b))
print('b的值:', b )