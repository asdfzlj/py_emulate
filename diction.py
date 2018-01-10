'''字典 key - value'''
alien_0={'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])
#添加
alien_0['x_position']=0
alien_0['y_position']=25

print(alien_0)
#修改
alien_0['color']='yellow'
print(alien_0)
#删除 删除的键—值对永远消失了。
del alien_0['points']
print(alien_0)

#由类似对象组成 的字典
student={
    'name':'Michael',
    'goods':'backetball',
    'age':30
}
print(student['name']+' age is '+str(student['age']))

#遍历字典 for k, v in user_0.items()
for key,value in student.items():
    print("\nKey:"+key)
    if str(value).isdigit():
        print("Value:"+str(value))
    else:
        print("Value:"+str(value.title()))

for k,v in student.items():
    print(k)
    if str(v).isdigit():
        print(str(v))
    else:
        print(v)

#遍历所有的key
for k in student.keys():
    print(k)

#嵌套
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)


aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
    print(alien['color'])
print("...")
print(len("Total number of alien:"+str(len(aliens))))

#在字典里存储列表

pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}
print(pizza['crust'])
print(pizza['toppings'])
for topping in pizza['toppings']:
    print(topping)