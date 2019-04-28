# 用isdigit函数判断是否数字
# 用isalpha判断是否字母
# isalnum判断是否数字 或 字母 或 数字与字母的组合
# 截取字符串的哪一段str[ x : y ]  取前不取后的原则       # 可以多取，没有的就不会显示

str_1 = "缓则治本"
str_2 = "Abc"
str_3 = "123Abc"

print(str_1[0 : 2])     # str[ x : y ]  取前不取后的原则
print(str_1[0 : 2].isdigit())


print(str_2[2 : 3])     # str[ x : y ]  取前不取后的原则
print(str_2[2 : 4])     # 可以多取，没有的就不会显示

#用isdigit函数判断是否数字
print(str_1.isdigit())
print(str_2.isdigit())
print(str_3.isdigit())

#用isalpha判断是否字母
print(str_1.isalpha())
print(str_2.isalpha())
print(str_3.isalpha())

#isalnum判断是否数字 或 字母 或 数字与字母的组合
print(str_1.isalnum())
print(str_2.isalnum())
print(str_1.isalnum())