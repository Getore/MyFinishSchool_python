#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 11:09:41
# @Author  : 沈力
# @Version : v1.0
# 功能：本页面主要用来将PDF转换得到的TXT文本，分为 治则和治法 两个部分文本
import re

def split_file():
    # filePath 表示公共路径
    filePath = "F:\\Trainee\\pycharm-professional\\workspace\\handleData"
    # 文件的读取地址
    readFileName = filePath + "\\words_in\\TreatmentTherapy.txt"
    # 文件的写地址
    TREATMENTWRITE = filePath + "\\words_out\\Treatment.txt"
    THERAPYWRITE = filePath + "\\words_out\\Therapy.txt"

    # 设置文件信息
    inputs = open(readFileName, 'r', encoding='utf-8')
    treatmentOutput = open(TREATMENTWRITE, 'w', encoding='utf-8')
    therapyOutput = open(THERAPYWRITE, 'w', encoding='utf-8')

    flag = 0  # 用来对文本的存储做个开关设置           flag = 1 打开存储开关；   flag = 0 关闭存储开关；
    mark = 0  # 用来对输出的哪个文件做一个开关设置     mark = 1 输出到治法文件； mark = 0 输出到治则文件；
    for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据
        # 用来过滤治则部分的无用信息
        if any((line == '\n', line == 'GB/T16751.3-1997\n', line == 'GB/T16751.3一1997\n',
                line == 'I\n', line == '国家技术监督局1997一03一04批准1997门0一01实施\n')):  # 如果此行只有换行，那么文本将不会输入到输出文件
            continue  # continue表示 - 跳过本次循环，无用信息就不用进行接下来的文本输出了

        if line == '治则\n':  # 当读取到的一行文本是 '治则\n' 时，就打开存储开关
            flag = 1
            continue  # 跳过本次循环，无用信息就不用进行接下来的文本输出了
        if line == '附录A\n':
            flag = 0
        if line == '解表法\n':  # 从 解表法 开始，将文本信息存储在治法文件里
            mark = 1

        if all((flag == 1, mark == 0)):
            treatmentOutput.write(re.sub('\n+', '\n', line))  # 使用正则表达式，再一次去除每一行的换行
        elif all((flag == 1, mark == 1)):
            therapyOutput.write(re.sub('\n+', '\n', line))

    treatmentOutput.close()
    therapyOutput.close()
    inputs.close()