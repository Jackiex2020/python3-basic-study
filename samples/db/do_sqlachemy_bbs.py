#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_sqlachemy_bbs.py
@Time    :   2020/05/12 22:48:05
@Author  :   Jackiex 
@Version :   1.0
'''


from samples.db.models.bbsModel import BBsModel

if __name__ == '__main__':
       
    # 测试添加
    kwargs = {
            'username': 'jackiex',
            'content': '6666666'
        }

    result_dict = BBsModel.add_bbs(**kwargs)

    if result_dict.get('code') == '200':
        print("插入记录成功")

    