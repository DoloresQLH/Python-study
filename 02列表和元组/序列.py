# 列表和元组的主要不同在于，列表是可以修改的，而元组不可以。
# 注意
#     Python支持一种数据结构的基本概念，名为容器（container）。
#     两种主要的容器是序列（如列表和元组）和映射（如字典）。
#     在序列中，每个元素都有编号，而在映射中，每个元素都有名称（也叫键）。
#     有一种既不是序列也不是映射的容器，它就是集合（set）

edward = ['Edward Gumby' , 42]
john = ['eaaa' , 50]

database = [edward ,john]
print(database)                # [['Edward Gumby', 42], ['eaaa', 50]]
