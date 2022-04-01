#08集合（set）是一个无需的不重复元素序列。
#可以使用大括号｛｝或者set()函数创建集合，空集合必须用set()而不是｛｝，因为｛｝是用来创建一个空字典。
#创建格式：
# parame = {value01,value02}
# # 或者
# set(value)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                       # 这里演示的是去重功能 {'banana', 'pear', 'apple', 'orange'}

print('orange' in basket)           #True
print('asdfasdf' in basket)         #false

#下面展示两个集合间的运算
a = set('abracadabra')
b = set('alacazam')
print(a - b)                    #{'r', 'd', 'b'}
print(a | b)                    #{'z', 'm', 'c', 'a', 'd', 'l', 'b', 'r'}
print(a & b)                    #{'c', 'a'}
print(a ^ b )                   #{'l', 'z', 'm', 'b', 'r', 'd'}

#类似列表推导式，同样集合支持集合推导式(Set comprehension):
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)                        #{'d', 'r'}

