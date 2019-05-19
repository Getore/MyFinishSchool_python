import jieba

suggestFreqTCM_url = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\rules\\suggestFreqTCM.txt"

# 载入中医临床诊疗术语治则部分的专有名词词库
jieba.load_userdict(suggestFreqTCM_url) # suggestFreqTCM_url 为专有名词词库存放路径

text = "用味辛性温的方药,以发散风寒,适用于风寒束表证的治疗方法。同义词:发表散寒"

# 全模式
seg_list = jieba.cut(text, cut_all=True)
print(u"[全模式]: ", "/ ".join(seg_list))

# 精确模式
seg_list = jieba.cut(text, cut_all=False)
print(u"[精确模式]: ", "/ ".join(seg_list))

# 搜索引擎模式
seg_list = jieba.cut_for_search(text)
print(u"[搜索引擎模式]: ", "/ ".join(seg_list))