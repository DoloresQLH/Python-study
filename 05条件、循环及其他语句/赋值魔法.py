# 5.2.1 序列解包
# 可同时（并行）给多个变量赋值：
x,y,z = 1,2,3
print(x,y,z)                    #1 2 3
# 看似用处不大？看好了，使用这种方式还可交换多个变量的值。
x,y= y,x
print(x,y,z)                    #2 1 3
# 实际上，这里执行的操作称为序列解包（或可迭代对象解包）：将一个序列（或任何可迭代
# 对象）解包，并将得到的值存储到一系列变量中。下面用例子进行解释。
values = 1,2,3
print(values)
x,y ,z = values
print(x)                        #1
# 这在使用返回元组（或其他序列或可迭代对象）的函数或方法时很有用。假设要从字典中随
# 便获取（或删除）一个键值对，可使用方法popitem，它随便获取一个键值对并以元组的方式
# 返回。接下来，可直接将返回的元组解包到两个变量中。
scoundrel = {'name':'Robin','girlfriend':'Marion'}
key,value = scoundrel.popitem()
print(key)                      #girlfriend
print(value)                    #Marion

#这让函数能够返回被打包成元组的多个值，然后通过一条赋值语句轻松地访问这些值。要解
# 包的序列包含的元素个数必须与你在等号左边列出的目标个数相同，否则Python将引发异常。
# x,y,z = [1,2,3,4,5]               #序列包含的元素个数与等号左边的不相同
# print(x,y,z)                    #ValueError: too many values to unpack (expected 3)
# 可使用星号运算符（*）来收集多余的值，这样无需确保值和变量的个数相同，如下例所示：
x,y,z,*d= [1,2,3,4,5]
print(z,y)                          #3 2
print(d)                           #[4, 5]
name = "Albus Percival Wulfric Brian Dumbledore"
first,*middle ,last = name.split()              #.split()c拆分成列表['Percival', 'Wulfric', 'Brian']
print(middle)

# 赋值语句的右边可以是任何类型的序列，但带星号的变量最终包含的总是一个列表。在变量
# 和值的个数相同时亦如此。
x,y,z = 1,2,3
print(x)                                #1
*x,y,z = 1,2,3                          #带星号的，且两边相同情况下，带星号的值会是一个列表[1]
print(x)
*x,y,z =1,2,3,4,5,6
print(x)                                #[1, 2, 3, 4]

# 5.2.2 链式赋值
# 链式赋值是一种快捷方式，用于将多个变量关联到同一个值。这有点像前一节介绍的并行赋
# 值，但只涉及一个值：
x=y=scoundrel
print(x,y)          #{'name': 'Robin'} {'name': 'Robin'}

# 5.2.3 增强赋值
# 可以不编写代码x = x + 1，而将右边表达式中的运算符（这里是+）移到赋值运算符（=）的前面，从而写成x += 1。
# 这称为增强赋值，适用于所有标准运算符，如*、/、%等。
x = 2
x +=1
x *=2
print(x)                            #6
# 增强赋值也可用于其他数据类型（只要使用的双目运算符可用于这些数据类型）。
fnord = 'foo'
fnord +='bar'
fnord *=2
print(fnord)                        #foobarfoobar