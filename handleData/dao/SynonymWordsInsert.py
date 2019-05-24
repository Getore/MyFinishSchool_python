# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 - 10:28
# @Author  : shenli
# @Version : v1.0
# @Function: 用于将同义词词库存入数据库中
import MySQLdb
import re

def synonym_words_insert():
    # 停用词词库的存放路径
    suggestpWordsPath = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\rules\\synonymTCM.txt"
    # 数据库存储字段设置默认值
    nameSY = '同义词库名称'
    typeSY = 'SynonymWords'
    describeSY = '同义词词库'
    synonymSY = ''
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
        words = re.split('\t', line[0])
        length = len(words)  # 获得此行词的数量
        # print(length)
        i = 1
        while i < length:
            if i == 1:
                synonymSY += words[i]       # 如果是第一个同义词，那么其左侧不用显示'|'
            else:
                synonymSY += '|' + words[i] # 如果不是第一个同义词，那么其左侧显示'|'

            i += 1

        # SQL 插入语句
        sql = """INSERT INTO synonymwords(namesy,typesy, describesy, synonymsy, create_time, create_user)
                 VALUES ('%s', '%s', '%s', '%s', now(), '%d')""" % (words[0], typeSY, describeSY, synonymSY, createUser)

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            synonymSY = ''  # 清空同义词内容，方便存储下一个同义词
        except:
            # Rollback in case there is any error
            db.rollback()
            # print('error')

    # 关闭数据库连接
    db.close()