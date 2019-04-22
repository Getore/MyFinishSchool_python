#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 连接数据库      连接地址  账号  密码   数据库   数据库编码
db = MySQLdb.connect("localhost", "root", "123456", "mysql", charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()

