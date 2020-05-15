#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:bbs.py
# author:jackiex
# datetime:2020/5/15 16:34
# software: PyCharm
'''
   显示留言信息
'''
from flask import Flask,request,render_template,redirect

app = Flask(__name__)

