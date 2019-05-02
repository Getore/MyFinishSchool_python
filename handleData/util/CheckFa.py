# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 - 11:34
# @Author  : shenli
# @Version : v1.0
# @Function: 检测前面的五个字是否有法字，如果有，那么则是治法名称；没有，则是注释或其他
# 用法：
# lines = '表里双解法'
# print(check_fa(lines, 5))

def check_fa(line, num):    # num 的意思是表示超过的值，可以减少判断，优化部分
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

# lines = '表里双解法'
# print(check_fa(lines, 5))

