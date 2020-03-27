#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_log.py
@Time    :   2020/03/27 07:57:15
@Author  :   Jackiex 
@Version :   1.0
'''

import logging
file_handler = logging.FileHandler(filename='x1.log', mode='a', encoding='utf-8',)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    handlers=[file_handler,],
    level=logging.ERROR
)

logging.error('你好')