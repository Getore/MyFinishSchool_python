import jieba
import jieba.analyse

# delete 删除停用词

# 页面功能：
# 1.通过专有名词的设置，更好的进行文本的分词操作；
# 2.根据自己设置的停用词，进行文本的删除、过滤操作；

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
loadDictFileName = "F:\BigStudyGraduation\MyFinishSchool\pythonFile\suggestFreqTCM.txt"    # 自定义词典的路径
jieba.load_userdict(loadDictFileName)      # 根据 file_name 路径进行自我学习，更好的进行分词

# 创建停用词，用来删除文本中的停用词
# 关键词提取所使用停用词（Stop Words）文本语料库可以切换成自定义语料库的路径。
# jieba.analyse.set_stop_words(file_name) #file_name为自定义语料库的路径。
# 如：jieba.analyse.set_stop_words("../extra_dict/stop_words.txt")
# ------------------停用词 - 自定义语料库 --------------------------------------
# stopwords = {}.fromkeys(["术语","的","是","、","。","，","NO"])
# ------------------停用词 - 自定义语料库 --------------------------------------
setStopWordsFileName = "F:\BigStudyGraduation\MyFinishSchool\pythonFile\stopWordsTCM.txt"
jieba.analyse.set_stop_words(setStopWordsFileName)      # file_name 为自定义语料库的路径。

# 文件的读取地址
readFileName = "F:\Trainee\ideaIU-2018.2\TraditionalChineseMedicine_PDF_Check\src\\txt\\test.txt"
# 文件的写地址
writeFileName = "F:\Trainee\ideaIU-2018.2\TraditionalChineseMedicine_PDF_Check\src\\txt\\testResult00.txt"

# 进行文本分词操作，并将结果存放到 fileNameWrite 文件中
with open(readFileName, encoding='utf-8', errors='ignore') as f:
    document = f.read()
    document_code = document.encode("utf-8","ignore")
    # 使用 jieba 工具进行分词操作
    document_cut = jieba.cut(document_code, cut_all = False)

    # 删除停用词
    final = ''
    for res in document_cut:
        if res not in stopwords:    # 如果是停用词，那么就不加入
            final += res
    print(final)

    seg_list = jieba.cut(final, cut_all=False)
    result = "/".join(seg_list)   # join 方法是用来连接两个字符串
    print(result)

    # 在控制台打印出分词后的效果
    # print(result)

    # 将分词好的文件存放到路径为 fileNameWrite 中，并注明编码格式 utf-8
    result = result.encode("utf-8")
    with open(writeFileName, "wb+") as f2:
        f2.write(result)

# 关闭读取的所有文件
f.close()
f2.close()