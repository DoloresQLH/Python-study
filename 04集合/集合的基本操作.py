#1、添加元素
# 语法格式如下：
s = set()
# s.add(x)
# 将元素x添加到集合S中，如果元素已存在，则不进行任何操作
thisset = set(('google', 'runoob', 'taobao'))
thisset.add('facebook')
print(thisset)                          #{'runoob', 'google', 'taobao', 'facebook'}
#还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等。语法格式如下：

#修改元素
# s.update(x)
thisset.update({1,3})
print(thisset)                          #集合是无序的添加，和修改。{'runoob', 1, 'google', 3, 'facebook', 'taobao'}

thisset.update([1,4],[5,6])
print(thisset)                          #{1, 'facebook', 3, 4, 5, 6, 'google', 'taobao', 'runoob'}

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

#计算集合元素个数：len(s)
print(len(thisset))                     #6
#清空集合   s.clear()
# print(thisset.clear())                  #None
print(thisset)                          #set()

#判断元素是否在集合中存在
print('asfd' in thisset)                #False
print('runoob' in thisset)              #True

#拷贝一个集合 copy()
sss = thisset
print(sss)                              #{4, 5, 6, 'runoob', 'taobao', 'google'}
st = thisset.copy()
print(st)                               #{4, 5, 6, 'runoob', 'google', 'taobao'}
rrr = set(['g','i'])
print(rrr)
#判断两个元素两个集合是否包含相同的元素，如果没有返回True 否则返回False
print(rrr.isdisjoint(thisset))         #没有 sss.isdisjoint(thisset)    True
print("st.isdisjoint(thisset) ", st.isdisjoint(thisset))        #有False

#返回集合的并集
print(rrr.union(thisset))               #{4, 5, 6, 'runoob', 'i', 'taobao', 'google', 'g'}

#判断该方法的参数集合是否为指定集合的子集
print(rrr.issuperset(thisset))          #False
print(st.issuperset(thisset))           #True
#判断指定集合是否为该方法参数集合的子集
print(rrr.issubset(thisset))            #False
print(st.issubset(thisset))             #True