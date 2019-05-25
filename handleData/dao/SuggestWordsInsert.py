# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 - 10:28
# @Author  : shenli
# @Version : v1.0
# @Function: 用于将专有名词词库存入数据库中
import MySQLdb
import re

def suggest_words_insert():
    # 停用词词库的存放路径
    suggestpWordsPath = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\rules\\suggestFreqTCM.txt"
    # 数据库存储字段设置默认值
    nameSG = '专有名词名称'
    typeSG = 'SuggestWords'
    describeSG = '专有名词词库'
    createTime = 'now()'
    createUser = 1
    remark = ''

    # 连接数据库         连接地址        账号      密码             数据库             数据库编码
    db = MySQLdb.connect("localhost", "root", "123456", "tcm_clinicaltttpart", charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 读取文件数据
    inputs = open(suggestpWordsPath, 'r', encoding='utf-8')  # 设置文本格式
    for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据
        if line == '\n':
            continue
        line = re.split('\n', line)

        # SQL 插入语句
        sql = """INSERT INTO suggestwords(namesg,typesg, describesg, create_time, create_user)
                 VALUES ('%s', '%s', '%s', now(), '%d')""" % (line[0], typeSG, describeSG, createUser)

        try:
            # 执行sql语句
            cursor.execute(sql)
            print('正在向数据库插入专有名词词库：' + sql)
            # 提交到数据库执行
            db.commit()

        except:
            # Rollback in case there is any error
            db.rollback()
            # print('error')

    # 关闭数据库连接
    db.close()