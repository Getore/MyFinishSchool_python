#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 16:09:41
# @Author  : 沈力
# @Version : v1.0

# 功能：本页面，按方法来实现较为完整的 治则分词
# 进行去除停用词、专有名词分词
from Participle import seg_sentence
# 进行同义词替换（比较耗时）
from Participle import synonym_word

# 文件的读取地址
readFileName = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outI\\Treatment.txt"
# 文件的写地址
writeFileName = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outII\\Treatment.txt"

inputs = open(readFileName, 'r', encoding='utf-8')      # 设置文本格式
outputs = open(writeFileName, 'w', encoding='utf-8')    # 设置文本格式

for line in inputs:
    line_seg = seg_sentence(line)
    line_seg = synonym_word(line)
    outputs.write(line_seg)
outputs.close()
inputs.close()