import jieba

# Synonym 同义词


# 读取同义词的词典
fileName = "F:\\BigStudyGraduation\\MyFinishSchool\\pythonFile\\synonymTCM.txt"
def combinedfile(filepath):
    combine_dict = {}
    for line in open(filepath, "r", encoding="utf-8"):
        seperate_word = line.strip().split("\t")
        num = len(seperate_word)
        for i in range(1, num):
            combine_dict[seperate_word[i]] = seperate_word[0]

    return combine_dict


jieba.suggest_freq("北平城", tune = True)
seg_list = jieba.cut("北京是中国的首都，京城的景色非常优美，就像当年的北平城，我爱这故都的一草一木。", cut_all = False)
f = "/".join(seg_list)
result = open("F:\\Trainee\\ideaIU-2018.2\\TraditionalChineseMedicine_PDF_Check\\src\\txt\\testResultSynonym.txt", "wb")
result.write(f.encode("utf-8"))
result.close()

# 按照读取到的文本进行分割，依据 “/”分隔，为了去除同义词
def split_file():
    for line in open(
            "F:\\Trainee\\ideaIU-2018.2\\TraditionalChineseMedicine_PDF_Check\\src\\txt\\testResultSynonym.txt", "r",
            encoding="utf-8"):
        line_combine = line.split("/")

    return line_combine


# 按照读取到的一行文本进行分割
def split_words(line):
    line_combine = line.split("/")
    return line_combine


word_to_check = "北京/是/中国/的/首都/，/京城/的/景色/非常/优美/，/就/像/当年/的/北平城/，/我/爱/这/故都/的/一草一木/。"
def final_sentence_word(word_to_check):
    final_sentence = ""
    line_combine = split_words(word_to_check)
    for word in line_combine:   # line_combine 一个数组，用来存放分割后的字符串
        combine_dict = combinedfile(fileName)   # 获取同义词文本
        if word in combine_dict:
            word = combine_dict[word]
            final_sentence += word + "/"
        else:
            final_sentence += word + "/"

    return final_sentence

print(final_sentence_word(word_to_check))



