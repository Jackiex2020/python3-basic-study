#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def myfun(x,*args):
    print('第一个参数:', x)
    print('第二个参数:', args)
    for i in args:
        print('第二个参数里面的值:',i)

myfun(11,22,33,44,55)

myfun(11,'a','b','c',55)


def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

# hello('Hi') # => greeting='Hi', args=()
# hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
# hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')
