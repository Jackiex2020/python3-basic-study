#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_brokenline.py
@Time    :   2020/02/12 17:54:20
@Author  :   Jackiex 
@Version :   1.0
'''

# 绘制一条直线 y=2x
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[i*2 for i in x]
#plt.plot(x,y)
# 增加直线的显示效果
plt.plot(x,y,marker='v',color='red',linewidth=1,linestyle=':',label='y=2x')
plt.xlabel('Price')  #增加图例
plt.ylabel('Sales')  #增加图例
plt.legend(loc='lower right')   # 图例出现的位置
plt.show()