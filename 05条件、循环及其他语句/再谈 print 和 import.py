# 5.1.1 打印多个参数
print('age: ',42)
name = 'Gumby'
salutationi = 'Mr.'
greeting = 'hello,'
print(greeting,salutationi,name)        #hello, Mr. Gumby
greeting = 'hello'                      #如果greeting变量不包含','号
print(greeting,salutationi,name)        #hello Mr. Gumby
print(greeting+',',salutationi,name)    #hello, Mr. Gumby

#如果需要，可自定义分隔符：
print("I","wish","to","register","a","complaint",sep="_")       #I_wish_to_register_a_complaint

# 还可自定义结束字符串，以替换默认的换行符。例如，如果将结束字符串指定为空字符串，
# 以后就可继续打印到当前行。
print('hello',end=',')
print('word!')              #hello,word!


# 5.1.2 导入时重命名
# import somemodule
# from somemodule import somefunction
# 但如果有两个模块，它们都包
# 含函数open，该如何办呢？你可使用第一种方式导入这两个模块，并像下面这样调用函数：
# module1.open(...)
# module2.open(...)
# 但还有一种办法：在语句末尾添加as子句并指定别名。下面是一个导入整个模块并给它指定
# 别名的例子：
import math as foobar
print(foobar.sqrt(4))
# 下面是一个导入特定函数并给它指定别名的例子：
from math import sqrt as foobar
print(foobar(4))