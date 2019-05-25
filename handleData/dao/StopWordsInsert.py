# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 - 10:25
# @Author  : shenli
# @Version : v1.0
# @Function: 用于将停用词库存入数据库中
import MySQLdb
import re

def stop_words_insert():
    # 停用词词库的存放路径
    stopWordsPath = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\rules\\stopWordsTCM.txt"
    # 数据库存储字段设置默认值
    nameST = '停用词名称'
    typeST = 'StopWords'
    describeST = '停用词库'
    createTime = 'now()'
    createUser = 1
    remark = ''

    # 连接数据库         连接地址        账号      密码             数据库             数据库编码
    db = MySQLdb.connect("localhost", "root", "123456", "tcm_clinicaltttpart", charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 读取文件数据
    inputs = open(stopWordsPath, 'r', encoding='utf-8')  # 设置文本格式
    for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据
        if line == '\n':
            continue
        line = re.split('\n', line)

        # SQL 插入语句
        sql = """INSERT INTO stopwords(namest,typest, describest, create_time, create_user)
                 VALUES ('%s', '%s', '%s', now(), '%d')""" % (line[0], typeST, describeST, createUser)

        try:
            # 执行sql语句
            cursor.execute(sql)
            print('正在向数据库插入停用词词库：' + sql)
            # 提交到数据库执行
            db.commit()

        except:
            # Rollback in case there is any error
            db.rollback()
            # print('error')

    # 关闭数据库连接
    db.close()