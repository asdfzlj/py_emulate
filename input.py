'''
函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后， Python将其存储在
一个变量中，以方便你使用
'''
message=input("Tell me something,and I will repeat it back to you: ")
print(message)

name=input("Please enter your name:")
print("Hello,"+name+"!")

prompt="If you tell us who you are,we can personalize the messages you see."
prompt+="\nWhat is your first name?"
name=input(prompt)
print("\nHello,"+name+"!")

age=input("How old are you?")
print(age)
if int(age)>=18:
    print("ok")
else:
    print("nook")