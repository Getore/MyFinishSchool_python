#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 16:09:41
# @Author  : 沈力
# @Version : v1.0

# 功能：本页面，进行治则预处理，变成格式：.../.../.../...的形式
from Participle import seg_sentence
# 进行同义词替换（比较耗时）
from Participle import synonym_word

def seg_treatment():
    # 文件的读取地址
    segTreatmentFile_todo = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outI\\Treatment.txt"
    # 文件的写地址
    segTreatmentFile_done = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outII\\Treatment.txt"

    inputs = open(segTreatmentFile_todo, 'r', encoding='utf-8')  # 设置文本格式
    outputs = open(segTreatmentFile_done, 'w', encoding='utf-8')  # 设置文本格式

    for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据
        line_seg = seg_sentence(line)  # 进行去除停用词、专有名词分词，line_seg 结果是经过 seg_sentence() 方法处理的分词结果，即.../.../..，这样的结果
        # line_seg = synonym_word(line)  #TODO 待改进 进行同义词替换（比较耗时）
        outputs.write(line_seg + '\n')
    outputs.close()
    inputs.close()
