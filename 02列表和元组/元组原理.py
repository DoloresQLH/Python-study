#python的元组与列表雷士，不通支出在于元组的元素不能修改
# 元组使用小括号（），列表使用方括号[]
# 元组创建很简单，只需要在括号中添加元素，并使用都好隔开即可
tup1 = ('a','b','c','d')
tup2 = (1 , 2 , 3 , 4)
tup3 = 'a','b','c','d'
print("type(tup1)",type(tup1))              #type(tup1) <class 'tuple'>
print("type(tup1)",type(tup2))              #type(tup1) <class 'tuple'>
print("type(tup1)",type(tup3))              #type(tup1) <class 'tuple'>

#元组中只包含一个元素时，需要在元素后面添加都好，否则括号会被当做运算符使用：
tup1 = (50)
print("typy(tup1)", type(tup1))             #不加逗号，类型为整型typy(tup1) <class 'int'>
tup2 = (50,)
print("type(tup2)", type(tup2))             #加上逗号，类型为元组type(tup2) <class 'tuple'>

