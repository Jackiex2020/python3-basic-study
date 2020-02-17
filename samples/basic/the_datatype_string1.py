# -*- encoding: utf-8 -*-
'''
@File    :   the_datatype_string1.py
@Time    :   2020/02/17 12:09:00
@Author  :   jackiex 
@Version :   1.0
'''

'''code description：string类型是不可变数据类型？'''
# here put the import lib
stra = 'hello'
print (id(stra))

stra += 'world'
print (id(stra))