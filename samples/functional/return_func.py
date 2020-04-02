#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# def add(x, y, f):
#     return f(x) + f(y)
# sum=add(-2,-5,abs)
# print(sum)

# def sonfunc():
#     print("in the sonfunc..")
 
# def highfunc(func):
#     func()
#     print("in the highfunc..")
     
# highfunc(sonfunc)

import time

# def test(func):
#     print(func)
#     start=time.time()
#     func()
#     end=time.time()
#     print("运行时间%s"%(end-start))

# def foo():
#     time.sleep(2)
#     print("你好")

# test(foo)


# def sonfunc():
#     print("in the sonfunc..")

# def highfunc(func):
#     print("in the highfunc..")
#     return func
# res=highfunc(sonfunc)
# #res()

# def foo():
#     time.sleep(2)
#     print("from the foo")

# def test(func):
#     return func

# myfunc=test(foo)
# start=time.time()
# myfunc()
# end=time.time()
# print("执行时间%s"%(end-start))


import time
def foo():
    time.sleep(3)
    print("来自foo")
#不修改foo源代码
#不修改foo调用方式
def timer(func):
    start=time.time()
    func()
    end=time.time()
    print("执行时间%s"%(end-start))
    return func

f=timer(foo)
f()


# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum

# f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
# print(f)
# print(f())

# # why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i * i
#         fs.append(f)
#     return fs

# f1, f2, f3 = count()

# print(f1())
# print(f2())
# print(f3())

# # fix:
# def count():
#     fs = []
#     def f(n):
#         def j():
#             return n * n
#         return j
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs

# f1, f2, f3 = count()

# print(f1())
# print(f2())
# print(f3())
