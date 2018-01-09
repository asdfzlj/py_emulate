'''
组织列表
'''
#使用sort()对列表进行永久性排序
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
#倒序排序 reverse=True 永久性修改
cars.sort(reverse=True)
print(cars)

print(cars[0].title())

#使用函数sorted()对列表进行临时排序
cars=['bmw','audi','toyota','subaru']
print(cars)
print(sorted(cars))
#又变回来了
print(cars)

#倒着打印列表
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

#确定列表的长度
print(len(cars))

