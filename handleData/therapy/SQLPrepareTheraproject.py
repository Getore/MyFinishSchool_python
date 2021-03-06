# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 - 11:14
# @Author  : shenli
# @Version : v1.0
# @Function: 用来将治法文本处理成可分词的格式，就是将连续的文字合并成一行
from SplitFile import split_file
from string import digits
from Utils import is_num_word
import re

def prepare_theraproject():
    # 文件的读取地址
    prepareFile_todo = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_out\\Therapy.txt"
    # 文件的写地址
    prepareFile_done = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outI\\Therapy.txt"

    inputs = open(prepareFile_todo, 'r', encoding='utf-8')  # 设置文本格式
    outputs = open(prepareFile_done, 'w', encoding='utf-8')  # 设置文本格式

    result = ''
    flag = 0  # 用来判断是否是上一个数字
    content = ''  # 用来暂时存储文字
    for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据
        if is_num_word(line) == 1:
            continue

        arrLine = re.split('\n', line)

        if arrLine[0][0:1].isdigit():
            outputs.write('\n' + line)
        else:
            outputs.write(arrLine[0])

    outputs.close()
    inputs.close()