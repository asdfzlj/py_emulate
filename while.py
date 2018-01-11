'''prompt="\ntell me something,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."
message=""
while message!='quit':
    message=input(prompt)
    if message!='quit':
        print(message)
'''
#使用标志

# prompt="\ntell me something,and I will repeat it back to you:"
# prompt+="\nEnter 'quit' to end the program."
# active=True
# message=""
# while message!='quit':
#     message=input(prompt)
#     if message!='quit':
#         active=False
#         break
#     else:
#         print(message)


#continue 跳过本次循环，继续下一次循环
current_number=0
while current_number<10 :
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)


#用while循环处理列表
uncommited_users=['alice','brian','candace']
commited_users=[]
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while uncommited_users:
    current_user=uncommited_users.pop()
    print("Verifying user:"+current_user.title())
    commited_users.append(current_user)

#while commited_users:
#    print(commited_users.pop())

for user in commited_users:
    print(user.title())


#删除特定值的所有列表元素
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


#使用用户输入来填充字典
responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name?")
    response=input("Which mountain would you like to climb someday?")
    #将答案存储在字典中
    responses[name]=response;
    #看看是否还有人参与
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=='no':
        polling_active=False
#结果
print("\n ----Poll Results----")
for key,value in responses.items():
    print(name+" would like to climb "+value+".")