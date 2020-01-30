# -*- coding: utf-8 -*-
'''
 类方法的定义
 实例的方法就是在类中定义的函数，它的第一个参数永远是 self，
 指向调用该方法的实例本身，其他参数和一个普通函数是完全一样的
'''
class Person(object):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

'''
get_name(self) 就是一个实例方法，它的第一个参数是self。
__init__(self, name)其实也可看做是一个特殊的实例方法。    
 '''
p1 = Person('Bob')
print(p1.get_name())  # self不需要显式传入