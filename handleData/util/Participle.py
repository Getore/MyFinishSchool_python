# Segmentation  n 分割；划分     Synonym n 同义词
# @Date    : 2019/4/27 - 10:15
# @Author  : shenli
# @Version : v1.0
# @Function:本页面，按方法来实现较为完整的完成分词、使用停用词、学习专有名词的功能
import jieba
import jieba.analyse
import re

# --------------------------------步骤一  学习专有名词------------------------------------------
suggestFreqTCM_url = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\rules\\suggestFreqTCM.txt"    # 自定义词典的路径
# 载入中医临床诊疗术语治则治法部分数据的专有名词词库
jieba.load_userdict(suggestFreqTCM_url)      # suggestFreqTCM_url为专有名词词库存放路径

# --------------------------------步骤二  过滤停用词------------------------------------------
# 创建停用词，用来删除文本中的停用词
setStopWordsFileName = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\rules\\stopWordsTCM.txt"   # 停用词路径 - setStopWordsFileName
# stopwordslist 读取停用词
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
# def split_words(line):
#     line_combine = line.split("/")
#     return line_combine

# 进行同义词替换
def synonym_word(word_to_check):
    final_sentence = ""     # 输出结果文字
    line_combine = re.split('/',word_to_check)

    for word in line_combine:   # line_combine 一个数组，用来存放分割后的字符串
        combine_dict = combinedfile(fileName)   # 获取同义词文本
        if word in combine_dict:
            word = combine_dict[word]
            final_sentence += word    # 给替换词的后面加 “/”
        else:
            final_sentence += word    # 按照原来的风格，展示分词的效果

    print('同义词替换后的效果：' + final_sentence)   # 打印同义词替换后的效果
    return final_sentence
# ---------------------------------步骤三  以上模块 同义词替换-----------------------------------------


# ---------------------------分词-----------------------------------------------
# seg_sentence 此方法，用来对句子进行分词，使用了停用词库
def seg_sentence(sentence):
    outstr = ''
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist(setStopWordsFileName)  # 这里加载停用词的路径
    for word in sentence_seged:     # 对分词的词语进行查找
        if word not in stopwords:   # 如果不在停用词中，则存入临时变量outstr中
            if word != '\t':
                outstr += word
                outstr += "/"       # 保持原分词效果

    print('预处理分词后的效果：' + outstr)   # 用于在此软件后台显示分词的运行效果，方便观察
    return outstr