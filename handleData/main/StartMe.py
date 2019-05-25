from TreatmentInsert import treatment_insert
from SplitFile import split_file
from TherapyInsert import therapy_insert
from StopWordsInsert import stop_words_insert
from SuggestWordsInsert import suggest_words_insert
from SynonymWordsInsert import synonym_words_insert

print('------------------------------------开始 中医临床诊疗术语治则治法部分数据的预处理------------------------------------')
# 分成治则、治法两个文件
split_file()
# 启动程序，进行 治则数据库的插入
treatment_insert()
# 启动程序，进行 治法名称数据库的插入
therapy_insert()

# 三大语义词库数据库整理
# 进行停用词词库数据库的插入
stop_words_insert()
# 进行专有名词词库数据库的插入
suggest_words_insert()
# 进行同义词词库数据库的插入
synonym_words_insert()

print('------------------------------------完成 中医临床诊疗术语治则治法部分数据的预处理------------------------------------')