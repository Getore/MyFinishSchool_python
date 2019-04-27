#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 16:09:41
# @Author  : 沈力
# @Version : v1.0
import jieba
import jieba.analyse
from string import digits
# 功能：本页面，按方法来实现较为完整的治则分词

# --------------------------------步骤一  学习专有名词------------------------------------------
# 用来帮助 jieba 更好的进行名词等词语的分词
loadDictFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\rules\\suggestFreqTCM.txt"    # 自定义词典的路径
jieba.load_userdict(loadDictFileName)      # 根据 file_name 路径进行自我学习，更好的进行分词


# --------------------------------步骤二  过滤停用词------------------------------------------
# 创建停用词，用来删除文本中的停用词
setStopWordsFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\rules\\stopWordsTCM.txt"   # 停用词路径 - setStopWordsFileName
# stopwordslist 此方法，用来读取停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# ---------------------------------步骤三  同义词替换-----------------------------------------
# 读取同义词的词典
fileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\rules\\synonymTCM.txt"
def combinedfile(filepath):
    combine_dict = {}
    for line in open(filepath, "r", encoding="utf-8"):
        seperate_word = line.strip().split("\t")
        num = len(seperate_word)
        for i in range(1, num):
            combine_dict[seperate_word[i]] = seperate_word[0]

    return combine_dict

# 按照读取到的一行文本进行分割
def split_words(line):
    line_combine = line.split("/")
    return line_combine

def final_sentence_word(word_to_check):
    final_sentence = ""
    line_combine = split_words(word_to_check)
    for word in line_combine:   # line_combine 一个数组，用来存放分割后的字符串
        combine_dict = combinedfile(fileName)   # 获取同义词文本
        if word in combine_dict:
            word = combine_dict[word]
            final_sentence += word + "/"    # 给替换词的后面加 “/”
        else:
            final_sentence += word + "/"    # 按照原来的风格，展示分词的效果

    return final_sentence

# ---------------------------分词-----------------------------------------------
# seg_sentence 此方法，用来对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist(setStopWordsFileName)  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += "/"
    return outstr

# 文件的读取地址
readFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_out_mysql\\Treatment.txt"
# 文件的写地址
writeFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_out_mysqlI\\Treatment.txt"

# 开始进行文本的分析操作
# 流程 --> 学习专有名词 - 过滤停用词 - 同义词替换 - 分词
inputs = open(readFileName, 'r', encoding='utf-8')
outputs = open(writeFileName, 'w', encoding='utf-8')

for line in inputs:     # line 变量，才是从读取文件的每一行的原始数据
    line = line.replace('/', '')    # 这里是先将本句文本中的/，全部替换掉
    line_seg = seg_sentence(line)  # line_seg 结果是经过 seg_sentence() 方法处理的分词结果，即.../.../..，这样的结果
    line_seg_latest = final_sentence_word(line_seg)
    line_seg_latest = line_seg_latest.replace('/', '')  # 此处是为了处理最后的文本，将所有的/删除
    line_seg_latest = line_seg_latest.replace('.', '')  # 此处是为了处理最后的文本，将所有的.删除
    # 请注意，此处可能不合适，因为 治则里有小治则
    # # 此处是为了处理文本的所有数字 导入: from string import digits
    # remove_digits = str.maketrans('', '', digits)
    # line_seg_latest = line_seg_latest.translate(remove_digits)
    line_seg_latest = line_seg_latest.replace('001', '')
    outputs.write(line_seg_latest + '\n')

outputs.close()
inputs.close()

