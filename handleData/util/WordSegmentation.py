# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 - 15:19
# @Author  : shenli
# @Version : v1.0
# @Function: 这里存放一些，分词所需要的工具方法
import jieba
import re

# 规则文件的总路径
rulePath = 'F:\\Trainee\\pycharm-professional\\workspace\\handleData\\rules'

# --------------------------------步骤一  学习专有名词------------------------------------------
# 用来帮助 jieba 更好的进行名词等词语的分词
loadDictFileName = rulePath + "\\suggestFreqTCM.txt"    # 自定义词典的路径
jieba.load_userdict(loadDictFileName)      # 根据 file_name 路径进行自我学习，更好的进行分词

# --------------------------------步骤二  过滤停用词------------------------------------------
setStopWordsFileName = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\rules\\stopWordsTCM.txt"   # 停用词路径 - setStopWordsFileName
# stopwordslist 此方法，用来读取停用词
def stopwordslist(filePath):
    stopwords = [line.strip() for line in open(filePath, 'r', encoding='utf-8').readlines()]
    # print(stopwords)
    return stopwords


# 用来根据停用词库，删除jieba分词后的无用词汇
def delete_stop_words(line):
    result = ''
    seg_list = jieba.cut(line, cut_all=False)       # 精确模式
    stopwords = stopwordslist(setStopWordsFileName)  # 这里加载停用词的路径
    for word in seg_list:
        if word in stopwords:
            continue
        else:
            result += word
            result += '/'

    return result

# 判断该字符是否是适用的症候
def is_applicable_symptom(line):
    line = delete_stop_words(line)  # 清除无用词汇，并以 / 的形式进行分词
    arrList = re.split('/', line)
    length = len(arrList)
    i = 0
    while i < length:
        if any((arrList[i] == '适用于', arrList[i] == '常用于', arrList[i] == '多用于',
                arrList[i] == '可用于', arrList[i] == '用于', arrList[i] == '用以',
                arrList[i] == '常用者', arrList[i] == '主用于')):
            return 1
        i += 1

    return 0

# line = "用味辛性温的方药,以发散风寒,适于风寒束表证的治疗方法。同义词:发表散寒"
# print(is_applicable_symptom(line))


