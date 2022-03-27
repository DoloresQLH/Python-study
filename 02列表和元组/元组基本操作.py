#访问元组
#元组可以使用下表索引来访问元组中的值，如下示例：
tup1 =('a','b','c','d')
tup2 =(1,2,3,4,5,6,7,8)
print("tup1[0]", tup1[0])               #tup1[0] a
print("tup2[1:5]", tup2[1:5])           #tup2[1:5] (2, 3, 4, 5)

#修改元组
#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下示例：
tup1 =(12 , 23.45)
tup2 =('abc','xyz')
#以下操作元组元素操作是非法的
# tup1[0] = 100
# print(tup1)             #TypeError: 'tuple' object does not support item assignment
#创建一个新的元组
tup3 = tup1+tup2
print(tup3)             #(12, 23.45, 'abc', 'xyz')

#删除元组
#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下示例：
tup =('a','b','c','d')
print(tup)                                  #('a', 'b', 'c', 'd')
del tup
# print("删除后的元组tup", tup)             #NameError: name 'tup' is not defined


#元组运算符
#与字符串一样，元组之间可以使用+号*号进行运算。这就意味着他们可以组合和赋值，运算后会生成一个新的元组。
#计算元素个数 len()
# print(len(tup))
#连接()+() tup+tup
tup1 =(12 , 23.45)
tup2 =('abc','xyz')
tup3 = tup1+tup2
print(tup3)
print((12 , 23.45)+('abc','xyz'))
#复制
print(('hi')*4)
#元素是否存在
print(3 in (1,2,3))
#迭代
x = 3
for x in (1,2,3):print(x)

#元组的内置函数
#计算元组元素个数len(tuple)

#返回元组元素最大值
print(max((1,2,3)))
#返回元组元素最小值
print(min(5,2,1,3,2,5))
#将可迭代序列转为元组
list1 =['a','b','c','d']
tuple1 = tuple(list1)
print(tuple1)

################################关于元组是不可变的
#所谓元组的不可变是指元组所指向的内存中的内容不可变。
tup =('a','b','c','b','d')

print(''.join(tup))


# 将可迭代系列转换为元组。
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1)
tuple1
('Google', 'Taobao', 'Runoob', 'Baidu')