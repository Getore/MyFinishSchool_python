# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 - 11:14
# @Author  : shenli
# @Version : v1.0
# @Function: 用来将治法文本处理成可分词的格式
import re
from CheckFa import check_fa

# 文件的读取地址
prepareFile_todo = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_out\\Therapy.txt"
# 文件的写地址
prepareFile_done = "F:\\Trainee\\pycharm-professional\\workspace\\handleData\\words_outI\\Therapy.txt"

inputs = open(prepareFile_todo, 'r', encoding='utf-8')  # 设置文本格式
outputs = open(prepareFile_done, 'w', encoding='utf-8')  # 设置文本格式

for line in inputs:  # line 变量，才是从读取文件的每一行的原始数据
    if all((check_fa(line, 9) == 1, line != '方法。\n', line != '法。\n', line != '治疗方法。\n', line != '的治疗方法。\n',
            line != '病的治疗方法。\n', line != '疗方法。\n', line != '的治疗方法\n', line != '体〔毫〕针疗法\n',
            line != '27.2头针疗法\n', line != '27.3面针疗法\n', line != '眼针疗法\n', line != '27.5鼻针疗法\n', line != '27.6耳针疗法\n',
            line != '2了.了舌针疗法\n', line != '27.9手针疗法\n', line != '同义词:吸筒疗法\n', line != '推拿[按摩]疗法\n',
            line != '28.7指拨疗法\n', line != '一种推拿疗法。\n', line != '药〔热〕熨疗法\n', line != '热敷疗法\n', line != '敷贴疗法\n',
            line != '29膏药疗法\n', line != '同义词:薄贴疗法\n', line != '29药膏疗法\n', line != '29.6箍围疗法\n', line != '湿敷疗法\n',
            line != '(敷)脐疗(法)\n', line != '治疗法。\n', line != '熏洗疗法\n', line != '同义词:汽浴疗法\n', line != '同义词:天灸疗法\n',
            line != '29.29钩割法\n', line != '同义词:坐药疗法\n', line != '2957挂线疗法\n', line != '的一种治疗方法。\n', line != '食(物)疗(法)\n',
            line != '30.2药膳疗法\n', line != '药饭疗法\n', line != '药粥疗法\n', line != '药酒疗法\n', line != '药茶疗法\n',
            line != '脏器疗法\n', line != '31情志疗法\n', line != '同义词:精神疗法\n', line != '1意示人眠疗法\n', line != '3以情胜情疗法\n',
            line != '移情易性疗法\n', line != '暗示解惑疗法\n', line != '顺意疗法\n', line != '习以平惊疗法\n', line != '音乐疗法\n', line != '歌吟疗法\n',
            line != '舞蹈疗法\n', line != '湿泥疗法\n', line != '热蜡疗法\n', line != '32.3沐浴疗法\n', line != '矿泉疗法\n', line != '日光浴疗法\n', line != '32.6握药疗法\n',
            line != '32.7药枕疗法\n', line != '32.9药带疗法\n', line != '等症的治疗方法。\n', line != '病症的治疗方法。\n', line != '症的治疗方法。\n')): # 结果是 1 表示，在line字符串中前6个字符中有‘法’字，注意'\n'，也算一个字符
        line = '0' + line

    outputs.write(line)
outputs.close()
inputs.close()