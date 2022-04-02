# 用作布尔表达式（如用作if语句中的条件）时，下面的值都将被解释器视为假：
#  False None 0 "" () [] {}
# 换而言之，标准值False和None、各种类型（包括浮点数、复数等）的数值0、空序列（如空
# 01字符串、空元组和空列表）以及空映射（如空字典）都被视为假，而其他各种值都被视为真①，
# 包括特殊值True②。

# 布尔值True和False属于类型bool，而bool与list、str和tuple一样，可用来转换其他的值。
print(bool('asddf'))            #True
print(bool(42))                 #True
print(bool(''))                 #False
print(bool(0))                  #False
# 注意 虽然[]和""都为假（即bool([]) == bool("") == False），但它们并不相等（即[] != ""）。
# 对其他各种为假的对象来说，情况亦如此（一个更显而易见的例子是() != False）。
print(bool([]) == bool(())==False)  #True
print(bool([]))                     #False
print(bool(''))                     #False
print('[]==''',[]!='')              #[]== True


# 5.4.2 有条件地执行和 if 语句
# name = input("what is your name? ")
# if name.endswith('Gumby'):
#     print("hello,Mr. Gumby")

# #.endswith判断字符串是否以指定字符或子字符串结尾。
#     str = "i love python"
#     print("1:", str.endswith("n"))
#     print("2:", str.endswith("python"))
#     print("3:", str.endswith("n", 0, 6))  # 索引 i love 是否以“n”结尾。
#     print("4:", str.endswith(""))  # 空字符
#     print("5:", str[0:6].endswith("n"))  # 只索引 i love
#     print("6:", str[0:6].endswith("e"))
#     print("7:", str[0:6].endswith(""))
#     print("8:", str.endswith(("n", "z")))  # 遍历元组的元素，存在即返回True，否者返回False
#     print("9:", str.endswith(("k", "m")))
#
#     # 元组案例
#     file = "python.txt"
#     if file.endswith("txt"):
#         print("该文件是文本文件")
#     elif file.endswith(("AVI", "WMV", "RM")):
#         print("该文件为视频文件")
#     else:
#         print("文件格式未知")

# 5.4.3 elif 子句，else 子句
# if name.endswith('y'):
#     print("hello,Mr. Gumby")            #hello,Mr. Gumby
# elif name.endswith('i') :
#     print("hello,Ms.guohui")
# else:
#     print("输入错误请重新输入")

# 5.4.6 更复杂的条件
# 1. 比较运算符
# 表5-1 Python比较运算符
# 表 达 式 描 述
# x == y x 等于y
# x < y x小于y
# x > y x大于y
# x >= y x大于或等于y
# x <= y x小于或等于y
# x != y x不等于y
# x is y x和y是同一个对象
# x is not y x和y是不同的对象
# x in y x是容器（如序列）y的成员
# x not in y x不是容器（如序列）y的成员
# if name.endswith('y'):
#     name= input("请输入姓名全称：")
#     if name in ['Gumby','guohui',]:
#             print("hello,Mr. Gumby")            #hello,Mr. Gumby
#     else:
#             print("输入错误")
# elif name.endswith('i') :
#     print("hello,Ms.guohui")
# else:
#     print("输入错误请重新输入")

