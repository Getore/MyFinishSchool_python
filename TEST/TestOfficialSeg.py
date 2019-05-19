import jieba
import jieba.analyse

# 本页面，按方法来实现较为完整的完成分词、使用停用词、学习专有名词的功能
# 优点：代码思路清晰



# 用来帮助 jieba 更好的进行名词等词语的分词
# ###载入词典
# 开发者可以指定自己自定义的词典，以便包含 jieba 词库里没有的词。虽然 jieba 有新词识别能力，但是自行添加新词可以保证更高的正确率。
# 用法： jieba.load_userdict(file_name) # file_name 为自定义词典的路径。
# 词典格式和dict.txt一样，一个词占一行；每一行分三部分，一部分为词语，另一部分为词频（可省略），最后为词性（可省略），用空格隔开。
# 词频可省略，使用计算出的能保证分出该词的词频。
# 更改分词器的 tmp_dir 和 cache_file 属性，可指定缓存文件位置，用于受限的文件系统。
# -----------单个分词描述----------------
# jieba.suggest_freq("中医临床", True)
# jieba.suggest_freq("急则治标", True)
# jieba.suggest_freq("缓则治本", True)
# ----------------------------------------
loadDictFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\rules\\suggestFreqTCM.txt"    # 自定义词典的路径
jieba.load_userdict(loadDictFileName)      # 根据 file_name 路径进行自我学习，更好的进行分词

# jieba.load_userdict('userdict.txt')
# 创建停用词list

# 创建停用词，用来删除文本中的停用词
# 关键词提取所使用停用词（Stop Words）文本语料库可以切换成自定义语料库的路径。
# jieba.analyse.set_stop_words(file_name) #file_name为自定义语料库的路径。
# 如：jieba.analyse.set_stop_words("../extra_dict/stop_words.txt")
# ------------------停用词 - 自定义语料库 --------------------------------------
# stopwords = {}.fromkeys(["术语","的","是","、","。","，","NO"])
# ------------------停用词 - 自定义语料库 --------------------------------------
setStopWordsFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\rules\\stopWordsTCM.txt"   # 停用词路径 - setStopWordsFileName
# stopwordslist 此方法，用来读取停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

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
readFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_in\\TreatmentTherapy.txt"
# 文件的写地址
writeFileName = "F:\\Trainee\\pycharm-professional\\workspace\\MyFinishSchool_python\\handleData\\words_out\\TreatmentTherapy.txt"

# 开始进行文本的分析操作
# 流程 --> 分词 - 过滤停用词
inputs = open(readFileName, 'r', encoding='utf-8')
outputs = open(writeFileName, 'w', encoding='utf-8')
for line in inputs:     # line 变量，才是从读取文件的每一行的原始数据
    line_seg = seg_sentence(line)  # line_seg 结果是经过 seg_sentence() 方法处理的分词结果，即.../.../..，这样的结果
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()