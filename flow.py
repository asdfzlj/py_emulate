cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

age=18
print(age==18)

#检查是否在 列表 中
requested_toppings=['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('mmmm' in requested_toppings)

#检查是否不包含在列表中
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(user.title()+",you can post a response if you wish.")

#布尔表达式
game_active=True
can_edit=False
print(game_active)
print(can_edit)

#if...else
age=19
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age=17
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#if...elsif ....else
age=12
if age<4:
    price=0
    #print("Your admission cost is $0.")
elif age<18:
    price=5
    #print("Your admission cost is $5.")
else:
    price=10
    #print("Your admission cost is $10.")
print("Your admission cost is $"+str(price)+".")