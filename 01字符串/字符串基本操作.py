#所有标准序列操作（索引、切片、乘法、成员资格检查、长度、最小值和最
#大值）都适用于字符串


website =  'http://www.python.org'
print("切片%s " % website[-3:])         #切片org
# website[-3:] = 'com'                    #赋值：报错 所有的元素赋值和切片赋值都是非
# 法的。

#设置字符串的格式：精简版
formats = 'hello,%s,%s enough fors ya'          #两个字符串运算符%s
values = ('world','hot')
print(formats %values)                          #'Hello, world. Hot enough for ya?'

x = 3.1415926
pai = "π等于%.3f" %x          #%.3f将值的格式设置为包含3位小数的浮点数
print(pai)                     #π等于3.142

#format方法:在最简单的情况下，替换字段没有名称或将索引用作名称。
print("{},{},{}".format("first","sencond","third"))         #first,sencond,third
#然而，索引无需像上面这样按顺序排列。
print("{5},{4},{3},{2},{1},{0},{1},{2},{3},{4},{5}".format('aa','bb','cc','dd','ee','ff'))   #ff,ee,dd,cc,bb,aa,bb,cc,dd,ee,ff

from math import pi
print("{name} is approximatel {value}".format(value=pi, name='π') )        #π is approximatel 3.141592653589793
#每个值都被插入字符串中，以替换用花括号括起的替换字段。要在最
#终结果中包含花括号，可在格式字符串中使用两个花括号（即{{或}}）来指定。
print("{{ceci n'est pas une replacement field}}".format())          #{ceci n'est pas une replacement field}

print( "{foo} {} {bar} {}".format(1, 2, bar=4, foo=3))      #替换字段名 3 1 4 2
# 你并非只能使用提供的值本身，而是可访问其组成部分（就像在常规Python代码中一样），
# 如下所示：
fullname=["Alfred","Smoketoomuch"]
print("Mr {name[1]}".format(name=fullname))
import math
tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
print(tmpl.format(mod=math))
# 可使用索引，还可使用句点表示法来访问导入的模块中的方法、属性、变量和函
# 数（看起来很怪异的变量__name__包含指定模块的名称）。

#=========================================基本转换
print("{pi!s}{pi!r}{pi!a}".format(pi = "π")) #三个标志（s、r和a）指定分别使用str、repr和ascii进行转换

print("the number is {num}".format(num=42))
print("the number is {num:b}".format(num=42))       #b 将整数表示为二进制数the number is 101010
print("the number is {num:c}".format(num=42))       #c 将整数解读为Unicode码点is *
print("the number is {num:d}".format(num=42))       #d 将整数视为十进制数进行处理，这是整数默认使用的说明符
print("the number is {num:e}".format(num=42))       #e 使用科学表示法来表示小数（用e来表示指数）is 4.200000e+01
print("the number is {num:E}".format(num=42))       #E 与e相同，但使用E来表示指数is 4.200000E+01
# f 将小数表示为定点数
# F 与f相同，但对于特殊值（nan和inf），使用大写表示
# g 自动在定点表示法和科学表示法之间做出选择。这是默认用于小数的说明符，但在默认情况下至少有1位小数
# G 与g相同，但使用大写来表示指数和特殊值
# n 与g相同，但插入随区域而异的数字分隔符
# o 将整数表示为八进制数
# s 保持字符串的格式不变，这是默认用于字符串的说明符
# x 将整数表示为十六进制数并使用小写字母
# X 与x相同，但使用大写字母
# % 将数表示为百分比值（将数表示为百分比值乘以100，按说明符f设置格式，再在后面加上%）

#==========宽度、精度和千位分隔符
print("{num:100}".format(num=100))          #' 100'
print("{num:100}".format(num="guohui"))     #'guohui    '  数和字符串对齐方式不同。

print( "Pi day is {pi:.2f}".format(pi=pi))      #Pi day is 3.14
print( "{pi:10.2f}".format(pi=pi))              #      3.14
print( "{:.9}".format("Guido van Rossum"))      #Guido van对于其他类型也可指定精度，但是这样做的情形不太常见。
#可使用逗号来指出你要添加千位分隔符。
print( 'One googol is {:,}'.format(10**10))     #One googol is 10,000,000,000


# 符号、对齐和用 0 填充
print( '{:010.2f}'.format(pi))                  #0000003.14

#要指定左对齐、右对齐和居中，可分别使用<、>和^。
print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi))
# 3.14
#    3.14
#       3.14

# 可以使用填充字符来扩充对齐说明符，这样将使用指定的字符而不是默认的空格来填充。
print( "{:$^15}".format(" WIN BIG "))          # $$$ WIN BIG $$$

#更具体的说明符=，它指定将填充字符放在符号和数字之间。
print('{0:10.2f}\n{1:10.2f}'.format(pi, -pi))
# 3.14
# -3.14
print('{0:10.2f}\n{1:=10.2f}'.format(pi, -pi))
      # 3.14
# -     3.14
# 如果要给正数加上符号，可使用说明符+（将其放在对齐说明符后面），而不是默认的-。如
# 果将符号说明符指定为空格，会在正数前面加上空格而不是+。
print('{0:-.2}\n{1:-.2}'.format(pi, -pi))  # 默认设置
# 3.1
# -3.1
print('{0:+.2}\n{1:+.2}'.format(pi, -pi))
# +3.1
# -3.1
print('{0: .2}\n{1: .2}'.format(pi, -pi))
#  3.1
# -3.1
# 需要介绍的最后一个要素是井号（#）选项，你可将其放在符号说明符和宽度之间（如果指
# 定了这两种设置）。这个选项将触发另一种转换方式，转换细节随类型而异。例如，对于二进制、
# 八进制和十六进制转换，将加上一个前缀。
print("{:b}".format(42))        #101010
print("{:#b}".format(42))       #0b101010
#对于各种十进制数，它要求必须包含小数点（对于类型g，它保留小数点后面的零）
print("{:g}".format(42))        #42
print("{:#g}".format(42))       #42.0000

# 字符串格式设置示例:根据指定的宽度打印格式良好的价格列表
width = int(input('请输入宽度：'))
pice_width = 10
item_width= width - pice_width
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width,pice_width)
fmt  = '{{:{}}}{{:>{}}}'.format(item_width,pice_width)
print('='*width)
print(header_fmt.format('Item','Price'))
print('-'*width)
print(fmt.format('apples',0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots (16 oz.)', 8))
print(fmt.format('Prunes (4 lbs.)', 12))
