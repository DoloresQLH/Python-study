d = dict(name = 'guohui',age =30)
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
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
# 4.2.4 字典方法
# 1. clear
# 方法clear删除所有的字典项，这种操作是就地执行的（就像list.sort一样），因此什么都不
# 返回（或者说返回None）。
phonebook.clear()           #{}
print(phonebook)

# 2. copy
# 方法copy返回一个新字典，其包含的键值对与原来的字典相同（这个方法执行的是浅复制，
# 因为值本身是原件，而非副本）。
x =  {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y=x.copy()          #{'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y['usernam'] = 'mlh'
y['machines'].remove('bar')
print(y)            #{'username': 'admin', 'machines': ['foo', 'baz'], 'usernam': 'mlh'}
print(x)            #{'username': 'admin', 'machines': ['foo', 'baz']}

# 3. fromkeys
# 方法fromkeys创建一个新字典，其中包含指定的键，且每个键对应的值都是None。
print({}.fromkeys(['name','age']))                           #{'name': None, 'age': None}
# 如果你不想使用默认值None，可提供特定的值。
print(dict.fromkeys(['name','age'],'(unkown)'))             #{'name': '(unkown)', 'age': '(unkown)'}

# 4. get
# 方法get为访问字典项提供了宽松的环境。通常，如果你试图访问字典中没有的项，将引发
# 错误。
d = {}
# print(d['name'])        #KeyError: 'name'
#而使用get不会这样：
print(d.get('names'))           #None
#可以指定默认值
print(d.get('names','N/A'))     #N/A
print(d.get('name'))           #guohui

# 代码清单4-2 字典方法示例
# 一个使用get()的简单数据库
# 在这里插入代码清单4-1中的数据库（字典people）
labels = {
 'phone': 'phone number',
 'addr': 'address'
}
# name = input('Name: ')
# 要查找电话号码还是地址？
# request = input('Phone number (p) or address (a)? ')
# 使用正确的键：
# key = request # 如果request既不是'p'也不是'a'
# if request == 'a': key = 'addr'
# 使用get提供默认值
# person = people.get(name, {})
# label = labels.get(key, key)
# result = person.get(key, 'not available')
# print("{}'s {} is {}.".format(name, label, result))

# 5. items
# 方法items返回一个包含所有字典项的列表，其中每个元素都为(key, value)的形式。字典项
# 在列表中的排列顺序不确定。
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())            #返回值属于一种名为字典视图的特殊类型。
# 字典视图可用于迭代（迭代将在第5章详细介绍）。
# 另外，你还可确定其长度以及对其执行成员资格检查。
it = d.items()
print(len(it))                          #3
print(('spam',0) in it)                 #True

# 将字典项复制到列表中
print(list(d.items()))                  #[('title', 'Python Web Site'), ('url', 'http://www.python.org'), ('spam', 0)]

# 6. keys方法keys返回一个字典视图，其中包含指定字典中的键。

# 7. pop
# 方法pop可用于获取与指定键相关联的值，并将该键值对从字典中删除。
d =  {'x': 1, 'y': 2}
print(d.pop('x'))           #1
print(d)                    #{'y': 2}

# 8.popitem
# 方法popitem类似于list.pop，但list.pop弹出列表中的最后一个元素，而popitem随机地弹
# 出一个字典项，因为字典项的顺序是不确定的，没有“最后一个元素”的概念。如果你要以高效
# 地方式逐个删除并处理所有字典项，这可能很有用，因为这样无需先获取键列表。
d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
print(d.popitem())              #('title', 'Python Web Site')
print(d)
print(d.popitem())              #('spam', 0)
print(d)
print(d.popitem())              #('url', 'http://www.python.org')
print(d)
# print(d.popitem())              #{}
# print(d)                        #KeyError: 'popitem(): dictionary is empty'

# 9. setdefault
# 方法setdefault有点像get，因为它也获取与指定键相关联的值，但除此之外，setdefault
# 还在字典不包含指定的键时，在字典中添加指定的键值对。
d = {}
d.setdefault('name','N/A')
print(d)                            #{'name': 'N/A'}
d['name'] = 'gumby'
d.setdefault('name','N/A')
print(d)                            #{'name': 'gumby'}
# 如果指定的键
# 存在，就返回其值，并保持字典不变。与get一样，值是可选的；如果没有指定，默认为None。
d = {}
print(d.setdefault('name'))
print(d)                            #{'name': None}
d['name'] = 'guohui'
d.setdefault('name')
print(d)                            #{'name': 'guohui'}

# 10. update
# 方法update使用一个字典中的项来更新另一个字典。
d = {1:'a',2:'b',3:'c'}
c = {'a':"a",'b':"b"}
d.update(c)
print(d)                #{1: 'a', 2: 'b', 3: 'c', 'a': 'a', 'b': 'b'}
b = {1:'A'}             #如果当前字典包含键相同的项，就替换它。
d.update(b)
print(d)                #{1: 'A', 2: 'b', 3: 'c', 'a': 'a', 'b': 'b'}

# 11. values
# 方法values返回一个由字典中的值组成的字典视图。不同于方法keys，方法values返回的视
# 图可能包含重复的值。
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 4
print(d)                    #{1: 1, 2: 2, 3: 3, 4: 4}
print(d.values())           #dict_values([1, 2, 3, 4])

# 小结
# 本章介绍了如下内容。
#  映射：映射让你能够使用任何不可变的对象（最常用的是字符串和元组）来标识其元素。
# Python只有一种内置的映射类型，那就是字典。
#  将字符串格式设置功能用于字典：要对字典执行字符串格式设置操作，不能使用format
# 和命名参数，而必须使用format_map。  字典方法：字典有很多方法，这些方法的调用方式与列表和字符串的方法相同。