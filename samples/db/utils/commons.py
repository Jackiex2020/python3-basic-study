#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file: commons.py
# author: lidekun
# datetime: 2020/5/8 15:50
# software: PyCharm


from datetime import datetime as cdatetime  # 有时候会返回datatime类型
from datetime import date, time
from sqlalchemy import DateTime, Numeric, Date, Time

# sqlachemy查询结果（对象）转换为字典,下面的所有方法为一个模块，使用时直接调用该方法即可
def all_to_dict(all_vendors):
    v = [to_dict(ven) for ven in all_vendors]
    return v

def to_dict(self):
    result = {}
    for key in self.__mapper__.c.keys():
        if getattr(self, key) is not None:
            result[key] = str(getattr(self, key))
        else:
            result[key] = getattr(self, key)
    return result

# 当结果为result对象列表时，result有key()方法
def result_to_dict(results):
    res = [dict(zip(r.keys(), r)) for r in results]
    # 这里r为一个字典，对象传递直接改变字典属性
    for r in res:
        find_datetime(r)
    return res


def model_to_dict(model):  # 这段来自于参考资源
    for col in model.__table__.columns:
        if isinstance(col.type, DateTime):
            value = convert_datetime(getattr(model, col.name))
        elif isinstance(col.type, Numeric):
            value = float(getattr(model, col.name))
        else:
            value = getattr(model, col.name)
        yield (col.name, value)


def find_datetime(value):
    for v in value:
        if isinstance(value[v], cdatetime):
            value[v] = convert_datetime(value[v])  # 这里原理类似，修改的字典对象，不用返回即可修改


def convert_datetime(value):
    """
    数据库datetime类型转时间字符串
    :param value:
    :return:
    """
    if value:
        if isinstance(value, (cdatetime, DateTime)):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(value, (date, Date)):
            return value.strftime("%Y-%m-%d")
        elif isinstance(value, (Time, time)):
            return value.strftime("%H:%M:%S")
    else:
        return ""