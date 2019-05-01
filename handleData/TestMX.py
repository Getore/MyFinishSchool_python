import jieba

# 分词词典
jieba.load_userdict("F:\\Trainee\\pycharm-professional\\workspace\\handleData\\rules\\suggestFreqTCM.txt")

text = "3.3标本兼仁同]治在病证出现标本并重的情况下，可采用治标与治本相结合的治疗原则。"

# 全模式
seg_list = jieba.cut(text, cut_all=True)
print(u"[全模式]: ", "/ ".join(seg_list))

# 精确模式
seg_list = jieba.cut(text, cut_all=False)
print(u"[精确模式]: ", "/ ".join(seg_list))

# 搜索引擎模式
seg_list = jieba.cut_for_search(text)
print(u"[搜索引擎模式]: ", "/ ".join(seg_list))