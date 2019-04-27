#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 11:09:41
# @Author  : 沈力
# @Version : v1.0

import re

# 文件的读取地址
readFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_in\\Therapy.txt"
# 文件的写地址
writeFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_out\\Therapy.txt"

# 开始进行文本的分析操作
# 流程 --> 学习专有名词 - 过滤停用词 - 同义词替换 - 分词
inputs = open(readFileName, 'r', encoding='utf-8')
outputs = open(writeFileName, 'w', encoding='utf-8')

flag = 0    # 用来对文本的存储做个开关设置
for line in inputs:     # line 变量，才是从读取文件的每一行的原始数据
    if line == '\n' :   # 如果此行只有换行，那么文本将不会输入到输出文件
        continue
    if line == '治则\n' : # 当读取到的一行文本是 '治则\n' 时，就打开存储开关
        flag = 1
    if line == '附录A\n' :
        flag = 0
    if flag == 1 :
        outputs.write(re.sub('\n+', '\n', line))    # 使用正则表达式，再一次去除每一行的换行

outputs.close()
inputs.close()