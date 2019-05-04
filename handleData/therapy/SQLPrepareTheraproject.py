# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 - 11:14
# @Author  : shenli
# @Version : v1.0
# @Function: 用来将治法文本处理成可分词的格式
import re
from Utils import check_first_char
from Utils import del_words
from Utils import point_num
from Utils import del_words
from string import digits

# 文件的读取地址
prepareFile_todo = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outI\\Therapy.txt"

inputs = open(prepareFile_todo, 'r', encoding='utf-8')  # 设置文本格式

# count = 1
pointNum = 0
for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据
    if line == '\n':
        continue

    pointNum = point_num(line)

    if any((line[0:3] == '923', line[0:3] == '926', line[0:3] == '193', line[0:3] == '232',
            line[0:3] == '234', line[0:4] == '2317', line[0:3] == '278', line[0:3] == '283',
            line[0:4] == '2943')):
        pointNum = 1

    if any((line[0:4] == '81.1', line[0:4] == '8.51', line[0:2] == '85', line[0:2] == '88',
            line[0:4] == '9.42', line[0:2] == '94', line[0:6] == '12.174', line[0:6] == '12.178',
            line[0:6] == '14.148', line[0:6] == '14.172', line[0:7] == '14.2315', line[0:7] == '14.3312',
            line[0:7] == '14.3313', line[0:4] == '73.4', line[0:5] == '224.3', line[0:3] == '234', line[0:5] == '235.1',
            line[0:5] == '24.36', line[0:5] == '24.38', line[0:5] == '24.39', line[0:5] == '24.53',
            line[0:5] == '25.23', line[0:5] == '252.8', line[0:5] == '253.7', line[0:5] == '25.39',
            line[0:5] == '25.52', line[0:3] == '256')):
        pointNum = 2

    if line[0:1].isdigit():
        if pointNum == 0:   # 大法系列
            line = del_words(line)
            # print(line)
        # elif pointNum == 1:  # 小法系列
            # print(line)
        elif pointNum == 2:  # 小小法系列
            print(line)


    # result = line
    #
    # if check_first_char(line, '0') == 1:    # 根据第一位字符是否是‘0’来判断是否是大法
    #     arrList = re.split('\n', line)      # 去除换行符
    #     result = del_words(arrList[0])
    #     print(str(count) + result)
    #     count += 1
    #     # result = ''     # 看是否有必要去掉大法的名称，也就是主要看后期处理的方式

inputs.close()