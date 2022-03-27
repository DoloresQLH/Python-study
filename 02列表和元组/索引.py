aa = 'hello'
#序列中的所有元素都有编号——从0开始递增。这称为索引（indexing）。
print(aa[0])
#。你可使用索引来获取元素。这种索引方式适用于所有序列。当你使
#用负数索引时，Python将从右（即从最后一个元素）开始往左数，因此1是最后一个元素的位置。
print(aa[-1])
# 对于字符串字面量（以及其他的序列字面量），可直接对其执行索引操作，无需先将其赋给
# 变量。这与先赋给变量再对变量执行索引操作的效果是一样的。
print('hlleo'[0])

#直接对返回的序列进行索引操作
xiaoming  = input("名字叫什么:")[0] #索引为0的值赋值给xiaoming
print(xiaoming)


# 将以数指定年、月、日的日期打印出来
#设置英文月份名称，使用序列存起来赋值给months
months = ['January',  'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#1-31使用序列存起来赋值给endings
endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
#手工输入年月日
year = input("year:")
month = input("month(1-12):")
day = input("day(1-31):")
#类型转换
month_number = int(month)
days = int(day)
#将月、日减1，得到正确的索引，把索引放入月和日的序列中赋值
month_name = months[month_number-1]
day_number = day + endings[days-1]

#输出正确的年月日
print(year+'.'+month_name+'.'+day_number)

# C:\Users\guohui\testDemo\Scripts\python.exe D:/python文件存放/testDemo/06列表和元组/索引.py
# h
# o
# h
# 名字叫什么:adfsdf
# a
# year:2020
# month(1-12):12
# day(1-31):12
# 2020.December.12th



