'''
    定义函数
'''


def greet_user():
    """显示简单的问候"""
    print("Hello!")

greet_user()

def greet_user(username):
    print("Hello," + username.title() + "!")

greet_user("zhangsan")

#1位置实参 顺序很重要
#你调用函数时， Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。 为此，
#最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参
def describe_pet(animal_type,pet_name):
    print("\n I hava a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name)

describe_pet("hamster","harry")
describe_pet("dog",'willie  ')

#2关键字实参
#明确地指出了各个实参对应的形参
def describe_pet(animal_type,pet_name):
    print("\n I hava a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name)
describe_pet(animal_type='hamster',pet_name='harry')

#3默认值
def describe_pet(animal_type,pet_name='dog'):
    print("\n I hava a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name)
describe_pet(animal_type='hamster')


#4返回值
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name

musician=get_formatted_name('jimi','handrix')
print(musician)

#5,让实参变成可选的
def get_formatted_name(first_name,middle_name,last_name):
    full_name=first_name+' '+middle_name+' '+last_name
    return full_name
musician=get_formatted_name('jimi','lee','hooker')
print(musician)

def get_formatted_name(first_name,last_name,middle_name=''):
    full_name=first_name+' '+middle_name+' '+last_name
    return full_name
musician=get_formatted_name('jimi','lee')
print(musician)
musician=get_formatted_name('jimi','lee','hooker')
print(musician)


#6返回字典
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('jimi','hendix')
print(musician)

def build_person(first_name,last_name,age=''):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age #字典追加数据
    return person
musician=build_person('jimi','hendix',11)
print(musician)

#7结果使用 函数和while循环
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name=input("First name:")
    l_name=input("Last name:")

    if f_name=='q':
        break
    if l_name=='q':
        break

    formatted_name=get_formatted_name(f_name,l_name)
    print('\nHello ,'+formatted_name+"!")

