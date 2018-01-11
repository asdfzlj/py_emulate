'''
函数
'''
#传递列表
def greet_users(names):
    for name in names:
        msg="hello,"+name.title()+"!"
        print(msg)

usernames=['Michael','tom','jackson']
greet_users(usernames)

#在函数中修改列表
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

#模拟打印每个设计，直到没有未打印的设计 为止
#打印每个设计 后，都 将其移到列表completed_models
while unprinted_designs:
    current_design=unprinted_designs.pop()

    #模拟
    print("Printing model:"+current_design)
    completed_models.append(current_design)

for completed_model in completed_models:
    print(completed_model)


def print_models(unprint_designs,completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print("Printing model:"+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#禁止函数修改列表
#传递任意数量 的实参
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperono')
make_pizza('mushrooms','green peppers','extra cheese')

def make_pizza(*toppings):
    for topping in toppings:
        print("-"+topping)

make_pizza('pepperono')
make_pizza('mushrooms','green peppers','extra cheese')

#结合使用位置实参和任意数量实参 *空元组
def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-"+topping)

make_pizza(16,'pepperono')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#使用任意数量的关键字实参 **创建空字典
def build_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)