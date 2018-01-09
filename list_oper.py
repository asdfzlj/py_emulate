'''
操作列表
'''
#遍历列表
citys=['泉州','厦门','福州','上海','北京']
for city in citys:
    print(city)
    print("这是循环里面的")
print("程序结束")
##for item in items:


####创建数值列表  不包括后面的值
for value in range(0,6):
    print(value+1)

####创建数值列表
#使用函数list()将range()的结果转化为列表
numbers=list(range(0,5))
print(numbers)

#使用range()，可找定步长   每一个值开始，第二个值结束 ，第三个值步长
even_numbers=list(range(2,11,2))
print(even_numbers)

#定义列表，保存数值,将数值遍历出来，一个个放入列表中
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)

    print(squares)
print(squares)

#对数字列表执行简单的统计计算
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
print(sum(digits)/len(digits))


#列表解析 表达式
squares=[value**2 for value in range(1,11)]
print(squares)

##使用列表的一部分
#切片 指定要使用的第一个元素和最后一个元素的索引 与range()一样
players=['姚明','James','Michael','张三','李四','王五','李世民','汉武帝']
print(players[0:3])#不包括3的索引
print(players[1:4])
print(players[:4]) #如果没有指定第一个元素，则自动从列表开头读取
print(players[2:]) #如果没有指定最后一个元素的索引 ，则自动读取到最后一个元素
print(players[-3:]) #输出最后三名

#遍历列表
for player in players[2:]:
    print(player)


#复制列表
your_players=players[3:]; #切片复制，如果没有指定索引，则复制所有的元素
print(your_players)

players.append("小白")
your_players.append("重耳")

print(players)
print(your_players)

#以下不是两个列表，为一个列表，其实是关联包含到另一个变量中
your_players=players
players.append('荆柯')
your_players.append('Jackson')

print(players)
print(your_players)