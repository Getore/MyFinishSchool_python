# split 划分 1.2.3
import re

# arrlist = re.split('\.', '1.2.3')
arrList = re.split(r'\W', '1.2.3')  # 这两个效果一样

print(arrList)