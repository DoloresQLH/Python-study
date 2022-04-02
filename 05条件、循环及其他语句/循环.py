
#================== 5.5.1 while 循环
# while语句非常灵活，可用于在条件为真时反复执行代码块。
x = 1
while x <=10:          #打印1-100的数字
    print(x)
    x +=1

#使用循环输入名称
# name = ''
# # not name or name.isspace()
# while not name.strip():
#     print("name.isspace()",name.isspace())
#     print("name.strip()",name.strip())
#     name = input("请输入你的名称： ")
#     if name=='':
#         print("您输入的名称为空格，为非法输入，请重新输入")
#         name = input("请重新输入名称：")
#         if name.endswith("y"):
#             if name in ['Gumby','guohui']:
#                 print('hello,{}!'.format(name))
#             else:
#                 print("名称输入再次失败")
#         else:
#             print("输入错误重新输入")
#     else:
#         print("名称输入失败！")


# 5.5.2 for 循环
# 可迭代对象是可使用for循环进行遍历的对象。
words =  ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for numbers in numbers:
    print(numbers)


#=============5.5.3 迭代字典
# 要遍历字典的所有关键字，可像遍历序列那样使用普通的for语句
print(list(range(10)))                  #迭代遍历[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d = {'x':1,'y':2,'z':3}
print(d.items())
for key in d:
    print(key ,'correspods to ', d[key])
for key ,value in d.items():
    print(key ,'correspods to ', value)

# 1. 并行迭代
# 有时候，你可能想同时迭代两个序列。假设有下面两个列表：
names = ['anne', 'beth', 'george', 'damon']
ages = [12,23,42,145]
for i in range(len(names)):
    print(names[i],'is',ages[i],'years old')
# anne is 12 years old
# beth is 23 years old
# george is 42 years old
# damon is 145 years old
# 一个很有用的并行迭代工具是内置函数zip，它将两个
# 序列“缝合”起来，并返回一个由元组组成的序列。返回值是一个适合迭代的对象，要查看其内
# 容，可使用list将其转换为列表。
print(list(zip(names,ages)))                #序列“缝合”起来[('anne', 12), ('beth', 23), ('george', 42), ('damon', 145)]
# “缝合”后，可在循环中将元组解包。
for name,age in zip(names,ages):
    print(name,'is',age,'years old')
# anne is 12 years old
# beth is 23 years old
# george is 42 years old
# damon is 145 years old

# 函数zip可用于“缝合”任意数量的序列。需要指出的是，当序列的长度不同时，函数zip将
# 在最短的序列用完后停止“缝合”。
print(list(zip(range(10),range(10000000000000))))
#list(range())代表迭代遍历 zip()代表并行缝合[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# 2. 迭代时获取索引在有些情况下，你需要在迭代对象序列的同时获取当前对象的索引。
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中。
seq = ['one', 'two', 'three']
print(enumerate(seq))               #<enumerate object at 0x000001DD94F30750>把列表、元祖、字符串组合为一个索引序列对象
for index, value in enumerate(seq):
     print(index, value)            #index索引 ，value值
# 0 one
# 1 two
# 2 three
list1 = ['01','02','03']
unit_value = '1'
for index, value in enumerate(list1):
  list1[index] = unit_value + value         #['101', '102', '103']
print(list1)

# 3. 反向迭代和排序后再迭代
# 来看另外两个很有用的函数：reversed和sorted。它们类似于列表方法reverse和sort（sorted
# 接受的参数也与sort类似），但可用于任何序列或可迭代的对象，且不就地修改对象，而是返回
# 反转和排序后的版本。
print(sorted([4,2,1,2,34]))                 #sorted   [1, 2, 2, 4, 34]
a = [4,2,1,2,34]
a.sort()
print("a.sort()",a )                        #a.sort() [1, 2, 2, 4, 34]
print(sorted("hello,world!"))               #['!', ',', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print(list(sorted("hello,world!")))         #['!', ',', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']

print(''.join(reversed("hello,world!")))
print(reversed("hello,world!"))             #翻转后的对象<reversed object at 0x0000022A4B1174A8>
xxx = [1,2,3,4,56,6,7,8,90,2]
reversed(xxx)
print("reversed(xxx)", xxx)                 #reversed  [1, 2, 3, 4, 56, 6, 7, 8, 90, 2]
xxx.reverse()
print("a.reverse()",xxx)                    #reverse   [2, 90, 8, 7, 6, 56, 4, 3, 2, 1]
# 请注意，sorted返回一个列表，而reversed像zip那样返回一个更神秘的可迭代对象。你无需
# 关心这到底意味着什么，只管在for循环或join等方法中使用它，不会有任何问题。只是你不能
# 对它执行索引或切片操作，也不能直接对它调用列表的方法。要执行这些操作，可先使用list对
# 返回的对象进行转换。
# 要按字母表排序，可先转换为小写。为此，可将sort或sorted的key参数设置为str.lower。
# 例如，sorted("aBc", key=str.lower)返回['a', 'B', 'c']。
print(sorted("Hello,World!".lower()))               #['!', ',', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print(sorted("Hello,World!",key=str.lower))         #['!', ',', 'd', 'e', 'H', 'l', 'l', 'l', 'o', 'o', 'r', 'W']


# 5.5.5 跳出循环
# 要结束（跳出）循环，可使用break。
# 找出小于100的最大平方值（整数与自己相乘
# 的结果），可从100开始向下迭代。找到一个平方值后，无需再迭代，因此直接跳出循环。
from math import sqrt
for n in range(99,0,-1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
# 2. continue
# 语句continue没有break用得多。它结束当前迭代，并跳到下一次迭代开头。
# condition1=condition2=condition3=True
# for x in seq:
#     if condition1:
#         continue
#     if condition2:
#         continue
#     if condition3:
#         continue
#         do_something()
#         do_something_else()
#         do_another_thing()
#         etc()
# 然而，在很多情况下，使用一条if语句就足够了。
# for x in seq:
    # if not (condition1 or condition2 or condition3):
    #     do_something()
    #     do_something_else()
    #     do_another_thing()
    #     etc()

# ==============================3. while True/break成例
# for和while循环非常灵活，但偶尔遇到的一些问题可能让你禁不住想：如果这
# 些循环的功能更强些就好了。例如，假设你要在用户根据提示输入单词时执行某种操作，并在用
# 户没有提供单词时结束循环。为此，一种办法如下：
# word = 'guohui'
# while word:
#     if word.endswith('guohui'):
#         word = input("请输入你的名字：")
#         print("欢迎：" + word+"回家")
#     else:
#         print("输入错误")
#         break
word = input("请输入你的名字：")
while True:
    if word.endswith('guohui'):
        print("欢迎：" + word+"回家")
    elif not word.endswith('guohui'):
        print("输入错误")
    break

x = 1
while x <=10:          #打印1-10的数字
    if x == 5:
        x += 1
        continue
    print(x ,end='')                #print(xx,end='')实现打印输出不换行，123467890
    x +=1

# 5.5.6 循环中的 else 子句
# 通常，在循环中使用break是因为你“发现”了什么或“出现”了什么情况。要在循环提前
# 结束时采取某种措施很容易，但有时候你可能想在循环正常结束时才采取某种措施。如何判断循
# 环是提前结束还是正常结束的呢？可在循环开始前定义一个布尔变量并将其设置为False，再在跳
# 出循环时将其设置为True。这样就可在循环后面使用一条if语句来判断循环是否是提前结束的。
for n in range(99,0,-1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        if n ==64:
            continue
        elif n<64:
            break

