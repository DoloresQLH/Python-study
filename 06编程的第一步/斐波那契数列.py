#写一个斐波纳契数列
#两个元素的总和确定下一个数
a , b = 0,1
while b < 1000:
    print(b, end= '  ')
    a,b = b,a+b
    print("a ,b",a ,b )

n=b
m=a+b
a=n
b=m

