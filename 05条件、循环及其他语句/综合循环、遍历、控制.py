#使用enumerate 函数进行遍历：
#语法：
# for index,item in enumerate(sequence):
#         process(index,item)

# seq = [1,2,34,5,6,7,8,3,23,2,3]
# for j,i in enumerate(seq):
    # print(j,i)

#for循环1-100所有整数的和
# n = 0
# sum = 0
# for n in range(0,101):
#     # print(n)
#     sum +=n
# print(sum)

#使用循环嵌套来实现99乘法表
x = 1
y = 1
z = 0
for x in range(1,10):
    for y in range(1,x+1):
        z = x * y
        print("%d*%d=%d"%(x,y,z),end='   ')
    print('\r')
# 1*1=1
# 2*1=2   2*2=4
# 3*1=3   3*2=6   3*3=9
# 4*1=4   4*2=8   4*3=12   4*4=16
# 5*1=5   5*2=10   5*3=15   5*4=20   5*5=25
# 6*1=6   6*2=12   6*3=18   6*4=24   6*5=30   6*6=36
# 7*1=7   7*2=14   7*3=21   7*4=28   7*5=35   7*6=42   7*7=49
# 8*1=8   8*2=16   8*3=24   8*4=32   8*5=40   8*6=48   8*7=56   8*8=64
# 9*1=9   9*2=18   9*3=27   9*4=36   9*5=45   9*6=54   9*7=63   9*8=72   9*9=81
#九九乘法表逆时针输出
for i in range(10,1,-1):
    print('\r')
    # print("x",x, end='     ')
    for j in range(1,i):
        # print("y",y,end=' ')
        n = i * j
        print("%d*%d=%d" % (i, j, n), end='   ')

#1-100的和
print(sum(range(101)))          #5050

#while循环算出1-100的和
n = 100
sum = 0
number = 1
while number <= n:
    sum = sum + number
    number += 1
print("1 到 %d 之和为: %d" % (n,sum))


#while循环语句和for循环语句使用else的区别：
# 1、如果else语句和while循环语句一起使用，则当条件变为False时，则执行else语句。
# 2、如果else语句和for循环语句一起使用时，else语句块只在for循环正常终止时执行！

#十进制转化
# while True:
#     number = input('请输入一个整数（输入Q退出程序）:' )
#     if number in ['q','Q']:
#         break
#     elif not number.isdigit():
#         print('您的输入有误！只能输入整数（输入Q退出程序）！请重新输入')
#         continue
#     else:
#         number = int(number)
#         print('十进制 --> 十六进制 : %d -> 0x%x' %(number,number))
#         print('十进制 --> 八进制 : %d -> 0o%o' % (number, number))
#         print('十进制 --> 二进制 : %d ->' %number,bin( number))

#冒泡排序
def paixu(li):
    max = 0
    for ad in range(len(li) -1):
        for x in range(len(li) - 1- ad):
            if li[x] >li[x+1]:
                max = li[x]
                li[x] = li[x+1]
                li[x+1] = max
            else:
                max = li[x+1]
    print(li)

#猜拳小游戏
import random
while 1:
    s = int(random.randint(1,3))
    if s == 1:
        ind = "石头"
    elif s ==2:
        ind = "剪刀"
    elif s == 3:
        ind = "布"
m = input("请输入石头，剪刀，布，输入end结束游戏：")
blist = ['石头','剪刀','布']

if (m not in blist) and (m!='end'):
    print("输入入错误，请重试：")
elif (m == 'end') and (m not in blist):
    print(ind)
    print("\n游戏退出")
    break




if __name__ == '__main__':
 paixu([41,23344,9353,5554,44,7557,6434,500,2000])
