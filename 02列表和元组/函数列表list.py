#=======================使用字符串创建列表
print(list('hello'))            #可将任何序列（而不仅仅是字符串）作为list的参数
numlist = list('hello')
print(''.join(numlist))             #''.join(列表) 讲列表转换成字符串


#修改列表，给元素赋值
x = [1,1,1]
x[1]=2 #给列表元素赋值
print(x)
num = [None] *10
# num[21] = 1 #给不存在的元素赋值，报错IndexError: list assignment index out of range
print(num)

#删除列表
del num[2]
print(num)

#示例一，给切片赋值
user = list('username')
user[4:] = list('ages')
print(''.join(user))
#示例二
a = list('per')
a[1:] = list('ython')
print(a)
#示例三
b = [1,2,3,4,5,6,7,8,9]
b[1:8] = []
print(b)

#==============================================列表list的各种方法
#给列表添加元素 .append()对象末尾单一添加、.extend(list)对象末尾添加多个元素，相当于一个列表扩充到另一个列表中
ls = [1,2,3]
ls.append(4)            #.append()对象末尾添加单一元素 [1, 2, 3, 4]
print(ls)
ls.extend([4,5,6])      #.extend(list)对象末尾添加一个序列 ls [1, 2, 3, 4, 4, 5, 6]
print("ls %s" % ls)
ls.extend(list('hello'))    #.extend()添加一个列表 ls = [1, 2, 3, 4, 4, 5, 6, 'h', 'e', 'l', 'l', 'o']
print("ls hello %s" % ls)
ls = ls+list('list')        #这种拼接相加[1, 2, 3, 4, 4, 5, 6, 'h', 'e', 'l', 'l', 'o', 'l', 'i', 's', 't']
print(ls)
a1 = [1,2,3]
b1 = [4,5,6]
print("a1+b1 %s" % (a1+b1))         #生成一个新的列表 [1, 2, 3, 4, 5, 6]
print("a1%s " % a1)                 #a1对象并未改变 [1, 2, 3]
a1 = a1+b1                          #a1对象虽改变，但是这种拼接没有extend效率高 [1, 2, 3, 4, 5, 6]
print("a1= a1+b1 %s" % a1)
# a1[len(a1):] =b1
# print("a1[len(a1):] =b1  %s"  % a1)     #a1与extend效果一致，但是可读性不高 [1, 2, 3, 4, 5, 6]


#给列表清空.clear()
ls.clear()
print(ls)

#复制.copy()列表
aa = [1,2,3,4,5]
bb = aa.copy()
print(id(bb))           #打印bb对象地址2167568319240
print("bb %s " % bb)    #[1, 2, 3, 4, 5]
print(id(aa))           #打印aa对象地址2167569114696
print("aa %s " % aa)    #[1, 2, 3, 4, 5]
#修改bb对象中元素值
bb[2] = 44
print("bb %s " % bb)    #查看bb是否修改成功 [1, 2, 44, 4, 5]
print("aa %s " % aa)    #查看是否影响aa对象[1, 2, 3, 4, 5]

#=方法count计算指定的元素在列表中出现了多少次
num1 = list('asdfasdfksdflsjdflsdjfoiwejflwejqwieqweqfdsdfsedaaSADASDWE')
print(num1)
n1 = num1.count('f')            #查看‘f’在num1对象中出现多少次
print(n1)                       #打印 出现8次

#方法index在列表中查找指定值第一次出现的索引。
a2 = [1,2,3,4,5,6,7,8,9]
print(a2.index(6))      #.index()获取值得索引

#方法insert用于将一个对象插入列表。
a2.insert(6, 'zhangsan')    #给指定索引添加值，也可使用切片赋值来获得与insert一样的效果。
print(a2)                   #[1, 2, 3, 4, 5, 6, 'zhangsan', 7, 8, 9]
a2[1:1] = list('he')        #通过切片的方式
print(a2)

#方法pop从列表中删除一个元素（末尾为最后一个元素），并返回这一元素。
# 使用pop可实现一种常见的数据结构——栈（stack）。栈就像一叠盘子，你可在上面添加盘子，
# 还可从上面取走盘子。最后加入的盘子最先取走，这被为后进先出（LIFO）。
#示例1
a2.pop()                    #默认删除末尾一个元素
print(a2)                   #[1, 'h', 'e', 2, 3, 4, 5, 6, 'zhangsan', 7, 8]
#示例2
a2.pop(5)                   #可指定索引，删除该索引值
print(a2)                   #[1, 'h', 'e', 2, 3, 5, 6, 'zhangsan', 7, 8]
#示例3
a3 = []                     #******pop是唯一既修改列表又返回一个非None值的列表方法
# a3.pop()
# print(a3)                   #当对象为None时，报错IndexError: pop from empty list
#示例4
# 方法pop和append的效果相反，因此将刚弹出的值压入（或附加）后，得到的
# 栈将与原来相同。使用pop可实现一种常见的数据结构——栈（stack）。
#后进先出（LIFO），x.append(x.pop())
x= [1,2,3]
x.append(x.pop())           #其中x.pop()删除列表末尾一个元素，x.append()给列表末尾添加一个元素
print(x)                    #[1, 2, 3]
#创建先进先出（FIFO）的队列，可使用insert(0, ...)代替append。一种更佳的解决方案是，使用模块collections中的
#deque。有关这方面的详细信息，请参阅第10章。
x.insert(3,x.pop())
print(x)                    #[1, 2, 3]
#也可继续使用append，但用pop(0)替代pop()。
x.append(x.pop(2))
print(x)                    #[1, 2, 3]

#方法remove用于删除第一个为指定值的元素。
x = ['aa','bb','cc']
print(id(x))        #删除前查看x对象的内存地址值2361127200840
x.remove('aa')      #remove是就地修改且不返回值的方法之一。不同于pop的是，它修改列表，但不返# 回任何值。
print(id(x))        #删除后查看x对象的内存地址值2361127200840
print(x)            #['bb', 'cc']

#方法reverse按相反的顺序排列列表中的元素（我想你对此应该不会感到惊讶）。
lst = [1,2,3]
print(id(lst))
print(lst)              #翻转前[1, 2, 3]
lst.reverse()           #注意到reverse修改列表，但不返回任何值（与remove和sort等方法一样）。
print(id(lst.reverse()))
print(lst)              #翻转后[3, 2, 1]

lst = [1,2,3,4,5]
sa = list(reversed(lst))        #.reverse倒序不返回列表，只是一个迭代。使用list蒋返回的对象转换为列表
print(sa)

#方法sort用于对列表就地排序①。就地排序意味着对原来的列表进行修改，使其元素按顺序
#排列，而不是返回排序后的列表的副本。
so = [4,52,1,21,36,7892,21,2]
so.sort()                       #就地排序序列，对原来的列表进行修改，按顺序排序
print(so)                       #[1, 2, 4, 21, 21, 36, 52, 7892]执行结果
y = so.sort()                 #由于.sort()不返回结果，是x是经过排序的，而y包含None
print(id(so))                   #2963901748104
# print(y)
# print(id(y))#None

#y与so进行关联
so1 = [4,52,1,21,36,7892,21,2]
print("id(so1) %s" % id(so1))                  #2786505650120
y = so1.copy()                  #与y与so进行关联，然后在进行排序
print(id(y))                    #2963901837384
y.sort()                        #y.sort()排序
print(id(y))                    #2963901837384
print(y)                        #[1, 2, 4, 21, 21, 36, 52, 7892]
#如果要将元素按相反的顺序排列，可先使用sort（或sorted），再调用方法reverse，也可使
#用参数reverse，这将在下一小节介绍。
print("sorted(y)%s" % sorted(y))

# 小结
# 下面来回顾一下本章介绍的一些最重要的概念。
#  序列：序列是一种数据结构，其中的元素带编号（编号从0开始）。列表、字符串和元组
# 都属于序列，其中列表是可变的（你可修改其内容），而元组和字符串是不可变的（一旦
# 创建，内容就是固定的）。要访问序列的一部分，可使用切片操作：提供两个指定切片起
# 始和结束位置的索引。要修改列表，可给其元素赋值，也可使用赋值语句给切片赋值。
# 函 数 描 述
# len(seq) 返回序列的长度
# list(seq) 将序列转换为列表
# max(args) 返回序列或一组参数中的最大值
# min(args) 返回序列和一组参数中的最小值
# reversed(seq) 让你能够反向迭代序列
# sorted(seq) 返回一个有序列表，其中包含指定序列中的所有元素
# tuple(seq) 将序列转换为





