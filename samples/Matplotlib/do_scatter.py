#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_scatter.py
@Time    :   2020/02/12 18:11:56
@Author  :   Jackiex 
@Version :   1.0
'''

# 绘制散点图
import matplotlib.pyplot as plt
import numpy as np

# 绘制散点图
# x = np.arange(50)
# y = x + 5 * np.random.rand(50)
# plt.scatter(x, y)
# plt.show()


m=np.random.normal(0,1,64)
n=np.random.normal(0,1,64)
plt.scatter(m, n,marker='*')
plt.show()
