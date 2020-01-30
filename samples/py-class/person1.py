# -*- coding: utf-8 -*-
'''
 范例：请给 Person 类增加一个私有属性 __score，表示分数，再增加一个实例方法 get_grade()，
 能根据 __score 的值分别返回 A-优秀, B-及格, C-不及格三档。
'''
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):

        if self.__score>=90:
            return 'A'

        elif self.__score>=60 :

            return 'B'

        else:
            return 'C'

p1 = Person('Bob', 90)

p2 = Person('Alice', 65)

p3 = Person('Tim', 48)

#  print("%s%s" %(a1,a2))打印多个变量的值
print("%s ：%s" %(p1.name,p1.get_grade()))

print("%s ： %s" %(p2.name,p2.get_grade()))

print("%s ：%s" %(p3.name,p3.get_grade()))