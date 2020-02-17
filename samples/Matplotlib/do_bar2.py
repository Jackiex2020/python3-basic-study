#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_bar2.py
@Time    :   2020/02/12 18:45:30
@Author  :   Jackiex 
@Version :   1.0
'''

# 显示12个月的销售数据
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,13)
y=np.random.uniform(0.5,1.0,12)*(1-x/float(13))
plt.bar(x,y,facecolor='green')
for x,y in zip(x,y):
    plt.text(x+0.05,y+0.02,'%.2f'%y,ha='center',va='center')

plt.show()