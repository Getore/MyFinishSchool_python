# 进行去除停用词、专有名词分词
# 进行同义词替换（比较耗时）
# 进行治则治法文件的分隔
from SplitFile import split_file

# 文件的读取地址
readFileName = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_in\\TreatmentTherapy.txt"
# 文件的写地址
writeFileName = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_out\\TreatmentTherapy.txt"

inputs = open(readFileName, 'r', encoding='utf-8')      # 设置文本格式
outputs = open(writeFileName, 'w', encoding='utf-8')    # 设置文本格式

split_file()    # 进行治则治法文件的分隔

# for line in inputs:     # line 变量，才是从读取文件的每一行的原始数据
#     line_seg = seg_sentence(line)  # 进行去除停用词、专有名词分词，line_seg 结果是经过 seg_sentence() 方法处理的分词结果，即.../.../..，这样的结果
#     line_seg_latest = synonym_word(line_seg)        # 进行同义词替换（比较耗时）
#     outputs.write(line_seg_latest + '\n')
# outputs.close()
# inputs.close()