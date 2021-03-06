# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 - 11:34
# @Author  : shenli
# @Version : v1.0
# @Function: 检测前面的五个字是否有法字，如果有，那么则是治法名称；没有，则是注释或其他
# 用法：
# lines = '表里双解法'
# print(check_fa(lines, 5))
import re
from string import digits

# check_fa，查找前 num 中是否有‘法’。num的意思是表示超过的值，可以减少判断，优化部分
def check_fa(line, num):
    length = len(line)
    arrList = list(line)

    if length > num:
        return 0

    i = 0
    while i < length:
        if arrList[i] == '法':
            return 1
        i += 1

    return 0

# 对比第一个字符，看是否是需要的字符 str
def check_first_char(line, str):
    arrList = list(line)
    if arrList[0] == str:
        return 1

    return 0

# 删除line中的所有数字部分
def del_num(line):
    remove_digits = str.maketrans('', '', digits)
    result = line.translate(remove_digits)
    return result

# 去除字符串中的数字、字母以及 ! % [ ] , 。 ‘ ‘这些特殊符号
def del_words(line):
    result = re.sub("[A-Za-z0-9\!\%\[\]\,\。\‘\‘\.]", "", line)
    return result

# 判断此行字符串是否有数字、字母、/ . - — 特殊字符
def is_num_word(line):
    value = re.compile("[A-Za-z0-9\/\.\-\—\n]+")
    arrList = list(line)
    length = len(arrList)
    i = 0
    while i < length:
        result = value.match(arrList[i])    # 匹配 value 中的字符
        if not result:
            return 0
        i += 1

    return 1

# 判断前8个字符串中有几个点 . 或者,用来判断名称
# 0 没有点   是大法/也有可能是内容   在治则中，没有点就是内容；在治法中，没有点可能两者意思
# 1 一个点   是一级小法/一级小治
# 2 两个点   是二级小法/二级小治
#
# 最大值 “99.99.99” 最大 8 个字符
def point_num(line):
    count = 0   # 用来存储.的个数
    max = 0     # 用来存储行字符的最大值
    arrList = list(line)
    length = len(arrList)
    i = 0

    if length < 8:
        max = length
    else:
        max = 8

    while i < max:
        if any((arrList[i] == '.', arrList[i] == ',')):
            count += 1
        i += 1

    return count

# 用来判断当前的 cou 是否是一位，一位则输出‘01’的形式，两位则无需加‘0’的前缀
def count_name(cou):
    cou = str(cou)
    lengthCou = len(cou)
    if lengthCou == 1:
        cou = '0' + cou

    return cou

# lines = '23.5,2补[固]肾摄精'
# print(point_num(lines))