#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-16 16:09:41
# @Author  : 沈力
# @Version : v1.0
import os,glob

# 功能：本页面主要用来将得到的文本存储到数据库

import MySQLdb

# 连接数据库         连接地址        账号      密码             数据库             数据库编码
db = MySQLdb.connect("localhost", "root", "123456", "tcm_clinicaltttpart_pure", charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

parentId = "0"
title = "急则治标"
nameUnit = "DE05.01.901.01.01"
orderNum = 1
createUser = 1


# SQL 插入语句
sql = """INSERT INTO treatment_project(parent_id, 
         title, title_unit, order_num, create_time, create_user)
         VALUES ('%s', '%s', '%s', '%d', now(), '%d')""" % (parentId, title, nameUnit, orderNum, createUser)

try:
   # 执行sql语句
   cursor.execute(sql)
   # print(sql)
   # 提交到数据库执行
   db.commit()
   # print("com")
except:
   # Rollback in case there is any error
   db.rollback()
   print("error")

# 关闭数据库连接
db.close()
