#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_flask2.py
@Time    :   2020/05/02 12:14:15
@Author  :   Jackiex 
@Version :   1.0
'''

'''
  前面的例子，是写死的数据，传递到前端显示
  那如何从数据库中查询数据，传递到前端呢？
'''

from flask import Flask,render_template
import pymysql

from flask_bootstrap import Bootstrap

# 创建flask应用对象
app=Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/users2')
def userlist2():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='test_db', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM user"
    cur.execute(sql)
    userlist = cur.fetchall()  # 数据集为返回一个嵌套元组
    conn.close()
    return render_template('users.html',u=userlist)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
    
    