#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-16 16:09:41
# @Author  : 沈力
# @Version : v1.0
# 功能：将文本读取，并进行判断是否是数字
# 1.是数字 - 是哪种数字
# 2.在数字后的第一个，是专有名词，直接进行数据库存储
# 3.剩下的字符串全部相加，变成一个字符串，直到遇到数字
#
# treatment_project
# parentIdI  title   titleUnit  orderNum   createTime    createUser     remark
#
# treatment_content
# parentIdII  content            orderNum   createTime  createUser   remark

import os,glob

import MySQLdb
import re

# 连接数据库         连接地址        账号      密码             数据库             数据库编码
db = MySQLdb.connect("localhost", "root", "123456", "tcm_clinicaltttpart_pure", charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()


# TODO 根据数字的大小和同等长度判断标识
# def  identify_

# 文件的读取地址
readFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_out_mysqlI\\Treatment.txt"

# 规定数据库各列的初始值
parentIdI = 0
title = '治则'
titleUnit = 'DE05.01.901.00.00'
orderNum = 1
createTime = 'now()'
createUser = 1
remark = ''

parentIdII = ''
content = ''
# 规定数据库各列的初始值

flag = 0    # 用来判断第一个数组，是否是数字，是就打开（1）开关存入 title ，不是则关闭（0），从第0个数组开始起作为 content 内容
arrList = ''
inputs = open(readFileName, 'r', encoding='utf-8-sig')  # UTF-8以字节为编码单元，它的字节顺序在所有系统中都是一様的，没有字节序的问题，也因此它实际上并不需要BOM(“ByteOrder Mark”)。但是UTF-8 with BOM即utf-8-sig需要提供BOM。
for line in inputs:     # line 变量，才是从读取文件的每一行的原始数据
    arrList = re.split('/', line)
    length = len(arrList)   #获取数组的长度

    num = arrList[0][2:4]       # 判断第0个数组的第[2:4]的字符是否是数字
    if num.isdigit() :          # 字符是否是数字
        flag = 1

    if flag == 1:               # 如果是数字，那么其后，肯定是专有名词，也就是title
        title = arrList[1]
        flag = 0                # 将title保存完就赶紧关闭，因为只有一个专有名词

        i = 2                   # 将剩下的作为content进行存储
        if i >= length:
            while i < length:
                content += arrList[i]
    else:
        i = 0
        while i < length:       # 将所有的文字存到 content 中
            content += arrList[i]
            i += 1

content = content.replace('\n','')      # 去除content的换行，使其变成一句，存入数据库
print(title)
print(content)
    # print(num)
    # print(arrList[0][0:1])
    # print(arrList[0][0:2])
inputs.close()


#
# # parentId = "0"
# print(parentId)
# # title = "急则治标"
# print(title)
# nameUnitI = "DE05.01.901.01"     # 小法
# nameUnitII = "DE05.01.901.01.01"    # 小小法   如果有小小法，那么注释所对应的 parentId 是 nameUnitII
# orderNum = 1
# createUser = 1
#
# # content = "与缓则治本相对而言。在大出血、暴泻、剧痛等标症甚急的情况下．应及时救治标病，如止血、止泻、止痛等，然后治其本病的治疗原则。"
# print(content)
# orderNumContent = 1














# SQL 插入语句
# sqlTreatmentProject = """INSERT INTO treatment_project(parent_id,
#          title, title_unit, order_num, create_time, create_user)
#          VALUES ('%s', '%s', '%s', '%d', now(), '%d')""" % (parentId, title, nameUnitI, orderNum, createUser)
#
# sqlTreatmentContent = """INSERT INTO treatment_content(parent_id,
#          content, order_num, create_time, create_user)
#          VALUES ('%s', '%s', '%d', now(), '%d')""" % (nameUnitII, content, orderNumContent, createUser)


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