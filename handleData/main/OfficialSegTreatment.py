#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 16:09:41
# @Author  : 沈力
# @Version : v1.0
# 进行去除停用词、专有名词分词
from Participle import seg_sentence
# 进行同义词替换（比较耗时）
from Participle import synonym_word
# 功能：本页面，按方法来实现较为完整的治则分词


# 文件的读取地址
readFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_out_mysql\\Treatment.txt"
# 文件的写地址
writeFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_out_mysqlI\\Treatment.txt"

# 开始进行文本的分析操作
# 流程 --> 学习专有名词 - 过滤停用词 - 同义词替换 - 分词
inputs = open(readFileName, 'r', encoding='utf-8')
outputs = open(writeFileName, 'w', encoding='utf-8')

for line in inputs:     # line 变量，才是从读取文件的每一行的原始数据
    line = line.replace('/', '')    # 这里是先将本句文本中的/，全部替换掉，那么line_seg得到的是一行纯文本( 不带/的 )
    line_seg = seg_sentence(line)  # line_seg 结果是经过 seg_sentence() 方法处理的分词结果，即.../.../..，这样的结果

    if line == '\n' :   # 如果此行只有换行，那么文本将不会输入到输出文件
        continue

    if line == '治则\n' :
        continue

    if line_seg == '/\n' :
        continue
    line_seg_latest = synonym_word(line_seg)
    # line_seg_latest = line_seg_latest.replace('/', '')  # 此处是为了处理最后的文本，将所有的/删除
    # line_seg_latest = line_seg_latest.replace('.', '')  # 此处是为了处理最后的文本，将所有的.删除

    # 请注意，此处可能不合适，因为 治则里有小治则
    # # 此处是为了处理文本的所有数字 导入: from string import digits
    # remove_digits = str.maketrans('', '', digits)
    # line_seg_latest = line_seg_latest.translate(remove_digits)

    line_seg_latest = line_seg_latest.replace('001', '')    # 根据治则的特殊字符'001'处理
    line_seg_latest = line_seg_latest.replace('//','/')     # 将分词后的 // 变成 /，便于进行数据库存储处理

    outputs.write(line_seg_latest + '\n')

outputs.close()
inputs.close()