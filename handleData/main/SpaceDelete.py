#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 11:09:41
# @Author  : 沈力
# @Version : v1.0
# 功能：本页面主要用来将PDF转换得到的TXT文本，分为 治则和治法 两个部分文本

import re

# 文件的读取地址
readFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_in\\TreatmentTherapy.txt"
# 文件的写地址
TREATMENTWRITE = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_out\\Treatment.txt"
THERAPYWRITE = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_out\\TreatmentTherapy.txt"

# 设置文件信息
inputs = open(readFileName, 'r', encoding='utf-8')
treatmentOutput = open(TREATMENTWRITE, 'w', encoding='utf-8')
therapyOutput = open(THERAPYWRITE, 'w', encoding='utf-8')

flag = 0    # 用来对文本的存储做个开关设置
mark = 0    # 用来对输出的哪个文件做一个开关设置
for line in inputs:     # line 变量，才是从读取文件的每一行的原始数据
    if line == '\n' :   # 如果此行只有换行，那么文本将不会输入到输出文件
        continue
    if line == '治则\n' : # 当读取到的一行文本是 '治则\n' 时，就打开存储开关
        flag = 1
    if line == '附录A\n' :
        flag = 0

    if line == '解表法\n' :    # 从 解表法 开始，将文本信息存储在法治文件里
        mark = 1

    if all(( flag == 1, mark == 0 )) :
        treatmentOutput.write(re.sub('\n+', '\n', line))    # 使用正则表达式，再一次去除每一行的换行
    elif all(( flag == 1, mark == 1 )) :
        therapyOutput.write(re.sub('\n+', '\n', line))

treatmentOutput.close()
inputs.close()