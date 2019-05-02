# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 - 15:27
# @Author  : shenli
# @Version : v1.0
# @Function: 将数据插入 - theraproject表中
import re
import MySQLdb
from Utils import check_first_char
from Utils import del_words
from Utils import count_name

def theraproject_insert():
    # 连接数据库         连接地址        账号      密码             数据库             数据库编码
    db = MySQLdb.connect("localhost", "root", "123456", "tcm_clinicaltttpart_pure", charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 规定数据库各列的初始值
    count = 2  # 用来作为 大法 的计数
    parentId = 0  # 默认值为 0
    nametp = '解表法'
    nametpUnit = 'DE05.01.902'  # DE05.01.902   解表法
    orderNum = 1
    createTime = 'now()'
    createUser = 1
    remark = ''

    # 文件的读取地址
    prepareFile_todo = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outI\\Therapy.txt"

    inputs = open(prepareFile_todo, 'r', encoding='utf-8')  # 设置文本格式

    for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据

        if check_first_char(line, '0') == 1:  # 根据第一位字符是否是‘0’来判断是否是大法
            arrList = re.split('\n', line)  # 去除换行符
            nametp = del_words(arrList[0])  # 大法的名称

            # nametpUnit的编码搭配
            nametpUnit = 'DE05.01.9' + count_name(count) + '.00'
            count += 1

            orderNum += 1  # 排序值自加
            # SQL 插入语句
            sqlTheraproject = """INSERT INTO theraproject(parent_id,
                     nametp, nametp_unit, order_num, create_time, create_user)
                     VALUES ('%s', '%s', '%s', '%d', now(), '%d')""" % (
            parentId, nametp, nametpUnit, orderNum, createUser)

            try:
                # 执行sql语句
                cursor.execute(sqlTheraproject)
                # 提交到数据库执行
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()
                print("error")

    inputs.close()

    # 关闭数据库连接
    db.close()
    inputs.close()