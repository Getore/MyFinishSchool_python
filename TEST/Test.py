import re
st = "hello,world!!%[545]你好234世界。。。"
ste = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", st)
print(ste)

#从字符串中提取数字
totalCount = '100abc'
totalCount = re.sub("\D", "", totalCount)
print(totalCount)

#从字符串中提取字母字符串
import re
st = "hello,world!!%[545]你好234世界。。。"
result = ''.join(re.findall(r'[A-Za-z]', st))
print(result)