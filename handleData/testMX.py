import jieba

# 分词词典
jieba.load_userdict("F:\Trainee\pycharm-professional\myTest.txt")

text = "【中医临床诊疗术语国家标准(治法部分)】NO.1[分类]治则[治法名称]急则治标[注释]与缓则治本相对而言。在大出血、暴泻、剧痛等标症甚急的情况下．应及时救治标病，如止血、止泻、止痛等，然后治其本病的治疗原则。"

# 全模式
seg_list = jieba.cut(text, cut_all=True)
print(u"[全模式]: ", "/ ".join(seg_list))

# 精确模式
seg_list = jieba.cut(text, cut_all=False)
print(u"[精确模式]: ", "/ ".join(seg_list))

# 搜索引擎模式
seg_list = jieba.cut_for_search(text)
print(u"[搜索引擎模式]: ", "/ ".join(seg_list))