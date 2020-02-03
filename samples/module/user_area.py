#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
使用另外一个py文件中定义的变量
'''
from def_cost import PI

def calc_round_area(radius):
    return PI * (radius ** 2)
 
def main():
    print("round area: ", calc_round_area(2))

if __name__=='__main__': 
    main()


