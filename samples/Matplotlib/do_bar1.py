#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_bar1.py
@Time    :   2020/02/12 18:41:42
@Author  :   Jackiex 
@Version :   1.0
'''

# 绘制柱状图

import matplotlib.pyplot as plt
import numpy as np

# 柱状图
x = np.arange(5)
y1, y2 = np.random.randint(1, 25, size=(2, 5))
width = 0.25
ax = plt.subplot(1,1,1)
ax.bar(x, y1, width, color='r')
ax.bar(x+width, y2, width, color='g')
ax.set_xticks(x+width)
ax.set_xticklabels(['a', 'b', 'c', 'd', 'e'])
plt.show()

