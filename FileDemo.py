with open('pi_digits.txt') as file_object:
    #contents=file_object.read()
    #print(contents.rstrip()) #删除字符串末尾 的空白
    for line in file_object:
        print(line.rstrip()) #一行一行读取


with open('pi_digits.txt') as file_object:
    lines=file_object.readline() #读取一行
for line in lines: #遍历每个字符
    print(line.rstrip())


with open('pi_digits.txt') as file_object:
    lines=file_object.readlines()

pi_string=''
for line in lines:
    pi_string+=line.strip() #去掉两端 的空白
print(pi_string)
print(len(pi_string))


with open('pi_digits.txt') as file_object:
    lines=file_object.readlines()

pi_string=''
for line in lines:
    pi_string+=line.strip() #去掉两端 的空白
print(pi_string[:16]+"...")
print(len(pi_string))
#圆周率是否包含你的生日
with open('pi_digits.txt') as file_object:
    lines=file_object.readlines()

pi_string=''
for line in lines:
    pi_string+=line.rstrip() #去掉两端 的空白
birthday=input("请输入您的生日:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
#创建文件


