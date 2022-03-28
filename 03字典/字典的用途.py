#字典以类似于下面的方式表示：竟字典是Python中唯一的内置映射类型
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# 12函数 dict
# 可使用函数dict①从其他映射（如其他字典）或键值对序列创建字典。
items = [('name','gumby'),('age',42)]
d = dict(items)
print(d)                    #         {'name': 'gumby', 'age': 42}
print(d['name'])            #gumby
#还可使用关键字实参来调用这个函数，如下所示：
d = dict(name = 'guohui',age =30)
print(d)                    #{'name': 'guohui', 'age': 30}
print(len(d))
# 基本的字典操作           ① 与list、tuple和str一样，dict其实根本就不是函数，而是一个类。
# 字典的基本行为在很多方面都类似于序列。
#  len(d)返回字典d包含的项（键值对）数。
#  d[k]返回与键k相关联的值。
#  d[k] = v将值v关联到键k。  del d[k]删除键为k的项。
#  k in d检查字典d是否包含键为k的项。
# 虽然字典和列表有多个相同之处，但也有一些重要的不同之处。
#  键的类型：字典中的键可以是整数，但并非必须是整数。字典中的键可以是任何不可变
# 的类型，如浮点数（实数）、字符串或元组。
#  自动添加：即便是字典中原本没有的键，也可以给它赋值，这将在字典中创建一个新项。
# 然而，如果不使用append或其他类似的方法，就不能给列表中没有的元素赋值。
#  成员资格：表达式k in d（其中d是一个字典）查找的是键而不是值，而表达式v in l（其
# 中l是一个列表）查找的是值而不是索引。这看似不太一致，但你习惯后就会觉得相当自
# 然。毕竟如果字典包含指定的键，检查相应的值就很容易。

# 前述第一点（键可以是任何不可变的类型）是字典的主要优点。第二点也很重要，下面的示
# 例说明了这种差别：
# x = []
# x[42] = 'foobar'
# print(x)                  #IndexError: list assignment index out of range
x = {}
x[42] = 'guohui'             #{42: 'guohui'}
print(x)

# 一个简单的数据库
# 一个将人名用作键的字典。每个人都用一个字典表示，
# 字典包含键'phone'和'addr'，它们分别与电话号码和地址相关联

people = {
    'Alice':{
        'phone':'2341',
        'addr':'foo drive 23'
    },
    'beth':{
        'phone':'9120',
        'addr':'bar street 42'
    },
    "Cecil": {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
#电话号码和地址的描述性标签，供打印输出时使用
labels = {
 'phone': 'phone number',
 'addr': 'address'
}

# name = input('Name: ')
#要查找电话号码还是地址？
# request = input('Phone number (p) of address (a)?')
#使用正确的键
# if request == 'p':key = 'phone'
# if request == 'a':key = 'addr'
#晋档名字是字典包含的键时才打印信息
# if name in people:
#    print("{}'s {}is {}.".format(name,labels[key],people[name][key]))


# =============4.2.3 将字符串格式设置功能用于字典
phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
print("Cecil`s pyhone number is {Cecil}.".format_map(phonebook))        #Cecil`s pyhone number is 3258.
