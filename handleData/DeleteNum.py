# 功能：去除字符串中的数字

from string import digits

s = 'abc123def456ghi789zero0'
remove_digits = str.maketrans('', '', digits)
res = s.translate(remove_digits)
print(res)
# 'abcdefghizero'