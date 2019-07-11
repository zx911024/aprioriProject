# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 11:30:13 2017
@author: zhangxun
"""
import pymysql
import pymssql
import pandas as pd
from logConf.logger import get_logger
from conf.conf import *


logging = get_logger()


class dbase():
    def __init__(self):
        pass

    def readSqlServerDb(self, sql):
        """
        连接mysql数据库（从），并进行数据查询，如果连接失败，会把错误写入日志中，并返回false，如果sql执行失败，也会把错误写入日志中，并返回false，如果所有执行正常，则返回查询到的数据，这个数据是经过转换的，转成字典格式，方便模板调用，其中字典的key是数据表里的字段名
        """
        try:
            conn = pymssql.connect(host=db_ip_sqlserver, user=db_user_sqlserver, database=db_name_sqlserver, password=db_pass_sqlserver)
            cursor = conn.cursor()
        except Exception as e:
            logging.error('数据库连接失败:%s' % e)
            return False
        try:
            cursor.execute(sql)
            # data = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in
            #         cursor.fetchall()]
            data = cursor.fetchall()  # 转换数据，字典格式
        except Exception as  e:
            logging.error('数据执行失败:%s' % e)
            return False
        finally:
            cursor.close()
            conn.close()
        return data

    def readSqlServerDbDict(self, sql):
        """
        连接mysql数据库（从），并进行数据查询，如果连接失败，会把错误写入日志中，并返回false，如果sql执行失败，也会把错误写入日志中，并返回false，如果所有执行正常，则返回查询到的数据，这个数据是经过转换的，转成字典格式，方便模板调用，其中字典的key是数据表里的字段名
        """
        try:
            conn = pymssql.connect(host=db_ip_sqlserver, user=db_user_sqlserver, database=db_name_sqlserver, password=db_pass_sqlserver)
            cursor = conn.cursor()
        except Exception as e:
            logging.error('数据库连接失败:%s' % e)
            return False
        try:
            cursor.execute(sql)
            data = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in
                    cursor.fetchall()]
            # data = cursor.fetchall()  # 转换数据，字典格式
        except Exception as  e:
            logging.error('数据执行失败:%s' % e)
            return False
        finally:
            cursor.close()
            conn.close()
        return data

