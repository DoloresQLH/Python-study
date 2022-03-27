permissions = 'rw'
print('w' in permissions) #使用运算符in 判断是否满足，返回true/false
user = ['mlh','foo','users']
print(input("user是否在user中：") in user)

#成员资格示例
database = [['zhangsan','12'],['lisi','23'],['wangwu','15'],['zhaoliu','22']] #序列中包含序列
usernam = input("姓名：")
ages = input("年龄：")
if[usernam, ages] in database:  #如果序列在实例database中返回ture 或者false
    print("名字：%s,年龄：%s" % (usernam, ages))
    print('Access granted')
