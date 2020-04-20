#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_magic.py
@Time    :   2020/04/10 08:14:46
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib
class Foo:
    """ 描述类信息，这是用于看片的神奇 """
    def func(self):
        pass

#print(Foo.__doc__)

obj=Foo()
#print(obj.__module__)  # 输出 即：输出模块
#print(obj.__class__)  # 输出 即：输出类

print(Foo.__dict__)

