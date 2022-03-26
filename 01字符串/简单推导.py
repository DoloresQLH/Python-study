# 列表推导是一种从其他列表创建列表的方式，类似于数学中的集合推导。列表推导的工作原
# 理非常简单，有点类似于for循环。
print([x * x for x in range(10)])                               #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 打印那些能被3整除的平方值，该如何办呢？
print([x * x for x in range(10) if x % 3 ==0])                  #[0, 9, 36, 81]
#还可添加更多的for部分。
print([(x,y) for x in range(3) for y in range(3)])
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 作为对比，下面的两个for循环创建同样的列表：
result = []
for x in range(1):
    for y in range(9):
        result.append((x,y))
        print(result)

# 与以前一样，使用多个for部分时，也可添加if子句。
girls = ['alice','bernice','clarice']
boys = ['chris','arnold','bob']
# print([b + '+'+ g for b in boys for g in girls if b[0] == g[0]])     #['chris+clarice', 'arnold+alice', 'bob+bernice']
letterGirls ={}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print([b + '+' +g for b in boys for g in letterGirls[b[0]]])       #['chris+clarice', 'arnold+alice', 'bob+bernice']