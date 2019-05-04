# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 - 10:15
# @Author  : shenli
# @Version : v1.0
# @Function: 用来将治则文本处理成可分词的格式，就是将连续的文字合并成一行
import re

def prepare_treatment():
    # 文件的读取地址
    prepareFile_todo = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_out\\Treatment.txt"
    # 文件的写地址
    prepareFile_done = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outI\\Treatment.txt"

    inputs = open(prepareFile_todo, 'r', encoding='utf-8')  # 设置文本格式
    outputs = open(prepareFile_done, 'w', encoding='utf-8')  # 设置文本格式

    result = ''
    flag = 0  # 用来判断是否是上一个数字
    for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据
        arrLine = re.split('\n', line)  # 通过换行符，将文本进行分割

        if any((line == '国家技术监督局1997-03-04批准\n', line == '1997-10-01实施\n')):
            continue

        if arrLine[0][0:1].isdigit():
            outputs.write('\n' + line)
        else:
            outputs.write(arrLine[0])

    outputs.close()
    inputs.close()