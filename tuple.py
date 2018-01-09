"""
    tuple 元组
    列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网
站的用户列表或游戏中的角色列表至关重要。然而，有时候你需要创建一系列不可修改的元素，
元组可以满足这种需求。 Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
元组看起来犹如列表，但使用圆括号而不是方括号来标识。
"""
#定义元组
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#print(dimensions[2])
#python不能给元组的元素赋值
#dimensions[0]=250
for dimension in dimensions:
    print(dimension)
#修改元组变量
dimensions=(400,100)
for dimension in dimensions:
    print(dimension)

