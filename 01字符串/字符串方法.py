# 3.4.1 center方法center通过在两边添加填充字符（默认为空格）让字符串居中。
print("the middle by jimmy eat world".center(39))
#     the middle by jimmy eat world
print("the middle by jimmy eat world".center(39, "*"))
#*****the middle by jimmy eat world*****

#3.4.2 find方法find在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回-1。
print('with a moo-moo here,and moo-moo there'.find('moo'))
# 7
title = "monty python`s flying circus python`s"
print(title.find('monty'))
print(title.find('python'))
print(title.find("flying"))
print(title.find("circus"))

# 注意 字符串方法find返回的并非布尔值。如果find像这样返回0，就意味着它在索引0处找到
# 了指定的子串。
subject = '$$$ get rich now!!! $$$'
print(subject.find('$$$'))      #0
print(subject.find('$$$',1))    #只指定了起点
print(subject.find('!!!'))      #16
print(subject.find('!!!',0,16)) #同时指定了起点和终点-1


# 3.4.3 join是一个非常重要的字符串方法，其作用与split相反，用于合并序列的元素。
seq = [1,2,3,4,5]
slp = '+'
# slp.join(seq)         #报错TypeError: sequence item 0: expected string, int found
ssl = ['1','2','3','4','5']
print(slp.join(ssl))        # #合并一个字符串列表1+2+3+4+5

dirs = '','usr','bin','evn'     #/usr/bin/evn
print('/'.join(dirs))

print('c:'+'\\'.join(dirs))       #c:\usr\bin\evn


# 3.4.4 lower方法lower返回字符串的小写版本。
print('TRONDHEIM Hammer Dance'.lower())     #trondheim hammer dance

# name = 'Gumby'
# names = ['gumby','smith','jones']
# if name.lower() in names:print("Found it")


# 3.4.5 replace方法replace将指定子串都替换为另一个字符串，并返回替换后的结果。
print('This is a test'.replace('is','eez'))     #Theez eez a test


# 3.4.6 splitsplit是一个非常重要的字符串方法，其作用与join相反，用于将字符串拆分为序列。
print('1+2+3+4+5'.split('+'))       #['1', '2', '3', '4', '5']

print('/usr/bin/env'.split('/'))        #['', 'usr', 'bin', 'env']

print('Using the default '.split())     #['Using', 'the', 'default']如果没有指定分隔符，将默认在单个或多个连续的空白字符（空格、制表符、换行符
# 等）处进行拆分。


#3.4.7 方法strip将字符串开头和末尾的空白（但不包括中间的空白）删除，并返回删除后的结果。
print('     internal whitespace is kept     '.strip())      #internal whitespace is kept
name = 'Gumby'
names = ['gumby','smith','jones']
if name.lower() in names:print("Found it")
na = 'Gumby '
print(na.lower().strip())                   #可以叠加使用，先变成小写，在删除空格
if na.lower().strip() in names:print("Found it")

print('****** SPAM * for * everyone!!!!*********'.strip('  *!'))        #SPAM * for * everyone

# 3.4.8 translate方法translate与replace一样替换字符串的特定部分，但不同的是它只能进行单字符替换。
# 这个方法的优势在于能够同时替换多个字符，因此效率比replace高。
# 要创建转换表，可对字符串类型str调用方法maketrans，这个方法接受两个参数：两个
# 长度相同的字符串，它们指定要将第一个字符串中的每个字符都替换为第二个字符串中的相应字
# 符①。就这个简单的示例而言，代码类似于下面这样：
table = str.maketrans('cs', 'kz')           #创建表完成
print(table)            #{99: 107, 115: 122}
print('this is an incredible test'.translate(table))        #thiz iz an inkredible tezt  转换成功
table = str.maketrans('cs','kz',' ')                        #调用方法maketrans时，还可提供可选的第三个参数，指定要将哪些字母删除。
print('this is an increddible test'.translate(table))       #thizizaninkreddibletezt

# 小结
# 本章介绍了字符串的两个重要方面。
#  字符串格式设置：求模运算符（%）可用于将值合并为包含转换标志（如%s）的字符串，
# 这让你能够以众多方式设置值的格式，如左对齐或右对齐，指定字段宽度和精度，添加
# 符号（正号或负号）以及在左边填充0等。
#  字符串方法：字符串有很多方法，有些很有用（如split和join），有些很少用到（如istitle
# 和capitalize）。
# 3.5.1 本章介绍的新函数
# 函 数 描 述
# string.capwords(s[, sep]) 使用split根据sep拆分s，将每项的首字母大写，再以空格为分隔符将它们合并起来
# ascii(obj) 创建指定对象的ASCII表示




