#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:common.py
# author:jackiex
# datetime:2020/9/25 17:11
# software: PyCharm
'''
this is function  description 
'''
# import module your need
from flask import g

def funa():
	print('funa %s' % g.uname)

def funb():
	print('funb %s' % g.uname)

def func():
	print('func %s' % g.uname)