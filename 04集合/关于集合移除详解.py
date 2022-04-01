thisset = set(('google', 'runoob', 'taobao','facebook'))
#移除元素，语法格式如下：
# s.remove(x)

#1、将元素X从集x中移除，如果元素不存在，则会发生错误。
thisset.remove('facebook')
print(thisset)                          #移除'facebook' {'runoob', 1, 3, 4, 'taobao', 5, 6, 'google'}
#移除不存在元素
# thisset.remove('asf')
# print(thisset)                          #KeyError: 'asf'
#2、可以使用另外一种方法也是移除集合中的元素，且如果元素不存在，不会发生错误。
#格式如下：
# s.discard(x)
thisset.discard("adfsdf")               #集合中不存在“adfsdf”
print(thisset)                          #{1, 3, 4, 5, 6, 'runoob', 'taobao', 'google'}
# 3、也可以 s.pop()
thisset.pop()                           #集合中随机移除一个元素
print(thisset)                          #{3, 4, 5, 6, 'runoob', 'taobao', 'google'}
thisset.pop()
print(thisset)                          #{3, 4, 5, 6, 'runoob', 'taobao'}
    #1、对于python中列表list、tuple类型中的元素，转换集合是会去掉重复的元素如下：
list = [1,1,1,2,3,42,3,2,4,2,5,67,8]
print(set(list))                   #列表list转换为set()08集合，去重复{1, 2, 3, 4, 5, 67, 8, 42}
tuple = (2,3,2,1,4,5,6,4,3,2,1)
print(set(tuple))                  #tuple类型转换set()08集合，也是去重复{1, 2, 3, 4, 5, 6}
    # 2、集合对 list 和 tuple 具有排序(升序)，举例如上:

    # 3、当集合是字典或者字符串,列表和元组组成时的set.pop()是随机从左边删除元素
# 列表示例：
set1 = set(["as","as","sd","ax","re"])
print("set1", set1)                 #{1, 2, 34, 4, 5, 6, 8, 9}
print("set1.pop()", set1.pop())     #1
print("set1", set1)                 #{2, 34, 4, 5, 6, 8, 9}

#元组示例：
set2 = set(("as","as","sd","ax","re"))
print("set2", set2)                 #{0, 1, 2, 6, 7, 8, 9, 23}
print("set2.pop()", set2.pop())     #0
print(set2)                         #{1, 2, 6, 7, 8, 9, 23}

#字典转换删除示例：
set3 = set({"1":'2',"2":"4","5":"6"})
print("set3", set3)
print("set(set3)", set3.pop())
print(set3)                         #{'2', '1'}

#字符串转换集合删除.pop()示例：
# print(''.join(["as","as","sd","ax","re"]))
set5 = set('asassdaxre')
print("set5", set5)
print("set5.pop()", set5.pop())
print(set5)                         #{'f', 'd', 's'}

