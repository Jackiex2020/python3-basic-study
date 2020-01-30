# -*- coding: utf-8 -*-
'''
 类属性的使用
 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
'''
class Student(object):
    count = 0  #类属性

    def __init__(self, name):
        self.name = name
        Student.count+=1
student=Student('zhangsan')
print(student.count)
print(student.name)