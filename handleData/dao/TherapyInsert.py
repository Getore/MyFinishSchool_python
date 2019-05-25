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
from Utils import point_num
from SQLPrepareTheraproject import prepare_theraproject
from WordSegmentation import delete_stop_words
from SegTherapy import seg_therapy

def therapy_insert():
    seg_therapy()   # 预处理治法文本，准备接下来的数据库存储
    # 连接数据库         连接地址        账号      密码             数据库             数据库编码
    db = MySQLdb.connect("localhost", "root", "123456", "tcm_clinicaltttpart", charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 规定数据库各列的初始值
    countI = 2  # 用来作为 大法 的计数
    countII = 1  # 用来作为 小法 的计数
    countIII = 1  # 用来作为 小小法 的计数
    parentIdI = 0  # 默认值为 0
    nametp = '解表法'
    nametpUnit = 'DE05.01.902'  # DE05.01.902   解表法
    orderNum = 1
    createTime = 'now()'
    createUser = 1
    remark = ''

    parentIdII = 0  # 治法内容的父节点
    applicableSymptom = ''  # 适用症候，适用于
    specificTreatment = ''  # 具体的治疗方法
    synonymWord = ''  # 与治法相同的同义词语

    # 文件的读取地址
    prepareFile_todo = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outII\\Therapy.txt"

    inputs = open(prepareFile_todo, 'r', encoding='utf-8')  # 设置文本格式

    for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据

        if line == '\n':
            continue

        pointNum = point_num(line)

        if any((line[0:3] == '923', line[0:3] == '926', line[0:3] == '193', line[0:3] == '232',
                line[0:3] == '234', line[0:4] == '2317', line[0:3] == '278', line[0:3] == '283',
                line[0:4] == '2943')):  # 纠正：小法
            pointNum = 1

        if any((line[0:4] == '81.1', line[0:4] == '8.51', line[0:2] == '85', line[0:2] == '88',
                line[0:4] == '9.42', line[0:2] == '94', line[0:6] == '12.174', line[0:6] == '12.178',
                line[0:6] == '14.148', line[0:6] == '14.172', line[0:7] == '14.2315', line[0:7] == '14.3312',
                line[0:7] == '14.3313', line[0:4] == '73.4', line[0:5] == '224.3', line[0:3] == '234',
                line[0:5] == '235.1',
                line[0:5] == '24.36', line[0:5] == '24.38', line[0:5] == '24.39', line[0:5] == '24.53',
                line[0:5] == '25.23', line[0:5] == '252.8', line[0:5] == '253.7', line[0:5] == '25.39',
                line[0:5] == '25.52', line[0:3] == '256')):  # 纠正：小小法
            pointNum = 2

        if line[0:1].isdigit():
            orderNum += 1

            if pointNum == 0:  # 如果是治法一级名称
                parentIdI = 0
                nametp = del_words(line)    # 调用Utils工具类，del_words()方法
                nametpUnit = 'DE05.01.9' + count_name(countI)
                countI += 1
                countII = 1
                countIII = 1

                sqlTheraproject = """INSERT INTO theraproject(parent_id,
                                     nametp, nametp_unit, order_num, create_time, create_user)
                                     VALUES ('%s', '%s', '%s', '%d', now(), '%d')""" % (
                    parentIdI, nametp, nametpUnit, orderNum, createUser)
            elif pointNum == 1:  # 如果是治法二级名称
                parentIdI = 'DE05.01.9' + count_name(countI - 1)
                nametp = del_words(line)    # 调用Utils工具类，del_words()方法
                nametpUnit = 'DE05.01.9' + count_name(countI - 1) + '.' + count_name(countII)
                countII += 1
                countIII = 1

                sqlTheraproject = """INSERT INTO theraproject(parent_id,
                                                 nametp, nametp_unit, order_num, create_time, create_user)
                                                 VALUES ('%s', '%s', '%s', '%d', now(), '%d')""" % (
                    parentIdI, nametp, nametpUnit, orderNum, createUser)
            elif pointNum == 2:  # 如果是治法三级名称
                parentIdI = 'DE05.01.9' + count_name(countI - 1) + '.' + count_name(countII - 1)
                nametp = del_words(line)    # 调用Utils工具类，del_words()方法
                nametpUnit = 'DE05.01.9' + count_name(countI - 1) + '.' + count_name(countII - 1) + '.' + count_name(
                    countIII)
                countIII += 1

                sqlTheraproject = """INSERT INTO theraproject_detailtcm(parent_id,
                                                 nametpd, nametpd_unit, order_num, create_time, create_user)
                                                 VALUES ('%s', '%s', '%s', '%d', now(), '%d')""" % (
                    parentIdI, nametp, nametpUnit, orderNum, createUser)

            try:
                # 执行sql语句
                cursor.execute(sqlTheraproject)
                print('正在向数据库插入治则名称：' + sqlTheraproject)
                # 提交到数据库执行
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()
                print("error")

        parentIdII = nametpUnit
        flag = 0  # 用来控制 0 适用症候，适用于  1 具体的治疗方法   2 同义词
        if not line[0:1].isdigit():
            flag = 1  # 打开输出开关    0 适用症候，适用于  1 具体的治疗方法   2 同义词
            line = delete_stop_words(line)
            arrList = re.split('/', line)
            length = len(arrList)
            i = 0
            while i < length:
                if any((arrList[i] == '适用于', arrList[i] == '常用于', arrList[i] == '多用于',
                        arrList[i] == '可用于', arrList[i] == '用于', arrList[i] == '用以',
                        arrList[i] == '常用者', arrList[i] == '主用于', arrList[i] == '运用于')):
                    flag = 0

                if any((arrList[i] == '同义词', arrList[i] == '同义诃')):
                    flag = 2

                if flag == 0:
                    applicableSymptom += arrList[i]  # 适用症候，适用于

                if flag == 1:
                    specificTreatment += arrList[i]  # 具体的治疗方法

                if flag == 2:
                    synonymWord += arrList[i]  # 与治法相同的同义词语

                i += 1

            sqlTheracontent = """INSERT INTO theracontent(parent_id,
                                             applicable_symptom, specific_treatment,synonym_word,
                                              order_num, create_time, create_user)
                                             VALUES ('%s', '%s', '%s', '%s', '%d', now(), '%d')""" % (
                parentIdII, applicableSymptom, specificTreatment, synonymWord, orderNum, createUser)

            try:
                # 执行sql语句
                cursor.execute(sqlTheracontent)
                print('正在向数据库插入治则内容：' + sqlTheracontent)
                # 提交到数据库执行
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()
                print("error")

            # print(parentIdII)
            # print(applicableSymptom)
            # print(specificTreatment)
            # print(synonymWord)

            # 将三个词语置空，以便接下来存储
            applicableSymptom = ''
            specificTreatment = ''
            synonymWord = ''

    inputs.close()

    # 关闭数据库连接
    db.close()
    inputs.close()
