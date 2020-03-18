#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_dircreate.py
@Time    :   2020/03/18 07:38:43
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib
import os

#显示当前工作路径
print("当前工作路径:",os.getcwd())
# 创建目录test
#os.mkdir("test222")
# 删除”test”目录
#os.rmdir("test222")

# 将当前目录改为"/samples"
os.chdir("samples")
print("修改后当前工作路径:",os.getcwd())

os.mkdir("test123")