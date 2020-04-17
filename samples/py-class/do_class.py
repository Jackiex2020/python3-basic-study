#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_class.py
@Time    :   2020/04/07 19:54:31
@Author  :   Jackiex 
@Version :   1.0
'''

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()


# class Test:
#     def prt(runoob):
#         print(runoob)
#         print(runoob.__class__)
 
# t = Test()
# t.prt()