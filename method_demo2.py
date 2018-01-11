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