'''
列表由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0~9或
所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。
鉴于列表通常包含多个元素，给列表指定一个表示复数的名称（如letters、 digits或names）是
个不错的主意。
在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素。
'''
#定义列表
names=['张三','李四','王五','小强']
names2=['jackson','michael','jerry']
#访问列表元素
#列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉Python即可。
#要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内。
print(names[0])
print(names2[0].title())
#返回最后一个列表元素
print(names2[-1])
#以此类推，返回倒数第2个
print(names2[-2])
message="my name is\t"+names[0]
print(message)

#输出所有的元素
print(names);
names[0]="小张"
print(names)
#添加元素
names.append('小0')
print(names)
#在列表中插入元素
names.insert(3,'小二')
print(names)
#删除元素
del names[2]
print(names)

#将元素从列表中删除，并接着使用它的值,取到的是加入到列表末尾的值
name=names.pop()
print(names)
print(name)

#弹出任何位置处的元素
print(names.pop(2))
print(names)

#根据值删除元素
names.remove("小强")
print(names)



