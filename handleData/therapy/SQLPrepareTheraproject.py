# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 - 11:14
# @Author  : shenli
# @Version : v1.0
# @Function: 用来将治法文本处理成可分词的格式
import re
from Utils import check_first_char
from Utils import del_words

# 文件的读取地址
prepareFile_todo = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outI\\Therapy.txt"

inputs = open(prepareFile_todo, 'r', encoding='utf-8')  # 设置文本格式

for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据
    result = line

    if check_first_char(line, '0') == 1:    # 根据第一位字符是否是‘0’来判断是否是大法
        arrList = re.split('\n', line)      # 去除换行符
        result = del_words(arrList[0])
        print(result)
        result = ''     # 看是否有必要去掉大法的名称，也就是主要看后期处理的方式

inputs.close()