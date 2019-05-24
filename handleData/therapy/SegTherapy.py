# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 - 11:13
# @Author  : shenli
# @Version : v1.0
# @Function: 本页面，进行治法预处理，变成格式：.../.../.../...的形式
from SQLPrepareTheraproject import prepare_theraproject
from Participle import seg_sentence
# 进行同义词替换（比较耗时）
from Participle import synonym_word

def seg_therapy():
    prepare_theraproject() # 进行第一道文本处理，完成治法文本的内容合并
    # 文件的读取地址
    segTreatmentFile_todo = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outI\\Therapy.txt"
    # 文件的写地址
    segTreatmentFile_done = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outII\\Therapy.txt"

    inputs = open(segTreatmentFile_todo, 'r', encoding='utf-8')  # 设置文本格式
    outputs = open(segTreatmentFile_done, 'w', encoding='utf-8')  # 设置文本格式

    for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据
        if line[0:1].isdigit():  # 如果此行数据的第一个字符是数字，那么就跳过，不处理，因为是专有名称
            outputs.write(line)
            continue
        else:
            line_seg = seg_sentence(line)  # 进行去除停用词、专有名词分词，line_seg 结果是经过 seg_sentence() 方法处理的分词结果，即.../.../..，这样的结果
            line_syn = synonym_word(line_seg)
            outputs.write(line_syn + '\n')

    outputs.close()
    inputs.close()