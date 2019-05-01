# Segmentation  n 分割；划分     Synonym n 同义词
#
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-16 16:09:41
# @Author  : 沈力
# @Version : v1.0
import jieba
import jieba.analyse

# 本页面，按方法来实现较为完整的完成分词、使用停用词、学习专有名词的功能
# 优点：代码思路清晰


# --------------------------------步骤一  学习专有名词------------------------------------------
# 用来帮助 jieba 更好的进行名词等词语的分词
loadDictFileName = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\rules\\suggestFreqTCM.txt"    # 自定义词典的路径
jieba.load_userdict(loadDictFileName)      # 根据 file_name 路径进行自我学习，更好的进行分词


# --------------------------------步骤二  过滤停用词------------------------------------------
# 创建停用词，用来删除文本中的停用词
setStopWordsFileName = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\rules\\stopWordsTCM.txt"   # 停用词路径 - setStopWordsFileName
# stopwordslist 此方法，用来读取停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# ---------------------------------步骤三  以下模块 同义词替换-----------------------------------------
# 读取同义词的词典
fileName = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\rules\\synonymTCM.txt"
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

# 进行同义词替换
def synonym_word(word_to_check):
    final_sentence = ""
    line_combine = split_words(word_to_check)
    for word in line_combine:   # line_combine 一个数组，用来存放分割后的字符串
        combine_dict = combinedfile(fileName)   # 获取同义词文本
        if word in combine_dict:
            word = combine_dict[word]
            final_sentence += word    # 给替换词的后面加 “/”
        else:
            final_sentence += word    # 按照原来的风格，展示分词的效果

    return final_sentence
# ---------------------------------步骤三  以上模块 同义词替换-----------------------------------------


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