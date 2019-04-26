#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-16 16:09:41
# @Author  : 沈力
# @Version : v1.0
import os,glob

import MySQLdb
import re

# 连接数据库         连接地址        账号      密码             数据库             数据库编码
db = MySQLdb.connect("localhost", "root", "123456", "tcm_clinicaltttpart_pure", charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# --------------------------首先处理小法情况-----------------------------
# 文件的读取地址
readFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_in\\treatment.txt"


inputs = open(readFileName, 'r', encoding='utf-8-sig')  # UTF-8以字节为编码单元，它的字节顺序在所有系统中都是一様的，没有字节序的问题，也因此它实际上并不需要BOM(“ByteOrder Mark”)。但是UTF-8 with BOM即utf-8-sig需要提供BOM。
for line in inputs:     # line 变量，才是从读取文件的每一行的原始数据
    arrList = re.split('/', line)

    if (arrList[0] == '治则') :    # SyntaxError: invalid syntax错误，记得在 if , elif , else , for , while , class ,def 声明末尾添加 :
        parentId = "0"

    title = arrList[1]
    content = arrList[2]
    # line_seg = seg_sentence(line)  # line_seg 结果是经过 seg_sentence() 方法处理的分词结果，即.../.../..，这样的结果
    # line_seg_latest = final_sentence_word(line_seg)
inputs.close()


# parentId = "0"
print(parentId)
# title = "急则治标"
print(title)
nameUnitI = "DE05.01.901.01.00"     # 小法
nameUnitII = "DE05.01.901.01.01"    # 小小法   如果有小小法，那么注释所对应的 parentId 是 nameUnitII
orderNum = 1
createUser = 1

# content = "与缓则治本相对而言。在大出血、暴泻、剧痛等标症甚急的情况下．应及时救治标病，如止血、止泻、止痛等，然后治其本病的治疗原则。"
print(content)
orderNumContent = 1

# SQL 插入语句
sqlTreatmentProject = """INSERT INTO treatment_project(parent_id, 
         title, title_unit, order_num, create_time, create_user)
         VALUES ('%s', '%s', '%s', '%d', now(), '%d')""" % (parentId, title, nameUnitI, orderNum, createUser)

sqlTreatmentContent = """INSERT INTO treatment_content(parent_id, 
         content, order_num, create_time, create_user)
         VALUES ('%s', '%s', '%d', now(), '%d')""" % (nameUnitII, content, orderNumContent, createUser)


try:
   # 执行sql语句
   # cursor.execute(sqlTreatmentProject)
   # cursor.execute(sqlTreatmentContent)
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

