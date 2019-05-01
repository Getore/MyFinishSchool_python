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

# 规定数据库各列的初始值
countI = 1      # 用来作为 小法 的计数
countII = 1     # 用来作为 小小法 的计数
parentIdI = 0
title = '治则'
titleUnit = 'DE05.01.901.01'    # DE05.01.901.01小法；DE05.01.901.01.01小小法

parentIdII = ''     # 以小小法 titleUnit 优先
content = ''

orderNum = 1
createTime = 'now()'
createUser = 1
remark = ''

# 用来判断当前的 cou 是否是一位，一位则输出‘01’的形式，两位则无需加‘0’的前缀
def count_name(cou):
    cou = str(cou)
    lengthCou = len(cou)
    if lengthCou == 1:
        cou = '0' + cou

    return cou

# 文件的读取地址
readFileName = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outII\\Treatment.txt"

num = '0'
oldNum = 0  # 用来存上一个标识
newNum = 0  # 用来存现在的这个标识

inputs = open(readFileName, 'r', encoding='utf-8-sig')  # UTF-8以字节为编码单元，它的字节顺序在所有系统中都是一様的，没有字节序的问题，也因此它实际上并不需要BOM(“ByteOrder Mark”)。但是UTF-8 with BOM即utf-8-sig需要提供BOM。
for line in inputs:
    if line == '\n':    # 清除没有内容的一行，如第一行
        continue

    arrList = re.split('/',line)
    length = len(arrList)  # 获取数组的长度

    oldNum = newNum
    newNum = arrList[0]
    if oldNum == newNum:
        # print('小小法')
        parentIdI = 'DE05.01.901.' + count_name(countI-1)
        titleUnit = 'DE05.01.901.' + count_name(countI-1) + '.' + count_name(countII)
        countII += 1
        title = arrList[2]
    else:
        # print('小法')
        parentIdI = 0
        titleUnit = 'DE05.01.901.' + count_name(countI)
        countI += 1
        countII = 1     # 将小小法的计数归 1
        title = arrList[1]

    # print(parentIdI)
    # print(title)
    # print(titleUnit)
    orderNum += 1   # 排序值自增
    # SQL 插入语句
    sqlTreatmentProject = """INSERT INTO treatproject(parent_id,
             title, title_unit, order_num, create_time, create_user)
             VALUES ('%s', '%s', '%s', '%d', now(), '%d')""" % (parentIdI, title, titleUnit, orderNum, createUser)
    #
    # sqlTreatmentContent = """INSERT INTO treatment_content(parent_id,
    #          content, order_num, create_time, create_user)
    #          VALUES ('%s', '%s', '%d', now(), '%d')""" % (nameUnitII, content, orderNumContent, createUser)

    try:
        # 执行sql语句
        cursor.execute(sqlTreatmentProject)
        # cursor.execute(sqlTreatmentContent)
        # print(sql)
        # 提交到数据库执行
        db.commit()
        # print("com")
    except:
        # Rollback in case there is any error
        db.rollback()
        print("error")

    # i = 0
    # while i < length:
    #     num = arrList[i][2:4]  # 取每个数组的第[2:4]的字符，是否是数字
    #
    #     if all((num.isdigit(), content != '')) :
    #         i += 1
    #         # print(title)
    #         # print(content)
    #         content = ''
    #         continue
    #     if arrList[i-1][2:4].isdigit():     # TODO 运行一遍，就会发现问题，在文本最后方加 字符串 3.99 就正常了，请解决一下√
    #         title = arrList[i]
    #     else:
    #         content += arrList[i]
    #
    #     i += 1

inputs.close()

try:
   # 执行sql语句
   cursor.execute(sqlTreatmentProject)
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