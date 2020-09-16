#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

pwd = os.path.abspath('')

print(pwd)
print(os.getcwd())

print('Name           Size       Last Modified')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%s%s    %10d    %s' %(f,flag,fsize, mtime))
