# -*- coding: utf-8 -*-
'''
说明：
  1 一个python文件（.py文件）中，可以没有类，可以有一个或者多个类的定义；


'''
class Student(object):
    def __init__(self,id, name, score):
        self.id=id
        self.name = name
        self.score = score


    def print_info(self):
        print('%s: %s: %s' % (self.id,self.name, self.score))

student1=Student('002','lishi',80)
student1.print_info()

student2=Student('003','wagnwu',90)
student2.print_info()
