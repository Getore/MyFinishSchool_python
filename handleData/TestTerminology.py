import jieba
# terminology （某学科的）术语，专有名词
# 注意，本页面代码操作，需要运行 IDEA 中的文本转换 --> ExtractText.java 文件
# 页面功能：通过专有名词的设置，更好的进行文本的分词操作

# 用来帮助 jieba 更好的进行名词等词语的分词
file_name = "F:\BigStudyGraduation\MyFinishSchool\pythonFile\suggestFreqTCM.txt"
jieba.load_userdict(file_name)      # file_name 为自定义词典的路径。

# 文件的读取地址
fileNameRead = "F:\Trainee\ideaIU-2018.2\TraditionalChineseMedicine_PDF_Check\src\\txt\\test.txt"
# 文件的写地址
fileNameWrite = "F:\Trainee\ideaIU-2018.2\TraditionalChineseMedicine_PDF_Check\src\\txt\\testResult.txt"

# 进行文本分词操作，并将结果存放到 fileNameWrite 文件中
with open(fileNameRead, encoding='utf-8', errors='ignore') as f:
    document = f.read()
    document_code = document.encode("utf-8","ignore")
    # 使用 jieba 工具进行分词操作
    document_cut = jieba.cut(document_code)
    result = "/".join(document_cut)

    # 在控制台打印出分词后的效果
    print(result)

    # 将分词好的文件存放到路径为 fileNameWrite 中，并注明编码格式 utf-8
    result = result.encode("utf-8")
    with open(fileNameWrite, "wb+") as f2:
        f2.write(result)

# 关闭读取的所有文件
f.close()
f2.close()