# -*- coding: utf-8 -*-
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.__score))

bart = Student('BartSimpson', 59)
bart.print_score()
print(bart.name)
#print(bart.__score)