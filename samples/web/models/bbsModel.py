# coding: utf-8

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BbsModel(db.Model):
    __tablename__ = 'bbs'

    autoID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), info='留言标题')
    content = db.Column(db.Text, info='留言内容')
    author = db.Column(db.String(255), info='留言人')
    datetime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='留言时间')

    # 添加留言；所需要的参数通过键值对传入
    @classmethod
    def add_bbs(cls, **kwargs):
        '''
           参数说明：kwargs为各字段字典格式数据
        '''
        pass

    @classmethod
    def get_bbs(cls):
        pass





