# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 - 10:15
# @Author  : shenli
# @Version : v1.0
# @Function: 用来将文本处理成准数据库的格式
import re



# (思路呆板，不用)思路1：先分词，再根据分词判断，根据数字判断是否换行，[i-1] 、 [i+1]判断是否是数字...
# 思路2：现将文本转换成 - 3.1急则治标与缓则治本相对而言在大出血、暴泻、剧痛等标症甚急的情况下，应及时救治标病，如止血、止泻、止痛等，然后治其本病的治疗原则。(换行3.2...)

# 将文本变成思路二的形式
# 判断除了第一个数字(i>0,!=0)每一行的第一个是否是数字
#   如果是那么去除换行符
#   如果不是，那么就需要与上一行相连

# 文件的读取地址
firstFile = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_out\\Treatment.txt"
# 文件的写地址
secondFile = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_out_mysql\\Treatment.txt"

inputs = open(firstFile, 'r', encoding='utf-8')  # 设置文本格式
outputs = open(secondFile, 'w', encoding='utf-8')  # 设置文本格式

result = ''
flag = 0    # 用来判断是否是上一个数字
for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据
    arrLine = re.split('\n', line)  # 通过换行符，将文本进行分割

    if arrLine[0][0:1].isdigit():
        outputs.write(result + '\n')
    if arrLine[0][0:1].isdigit():
        result = arrLine[0]
    if not arrLine[0][0:1].isdigit():
        result += arrLine[0]

outputs.close()
inputs.close()
