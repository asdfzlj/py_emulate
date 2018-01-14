# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you can't divide by zero!")
# print('程序运行结束')
#
#
# print("Give me tow numbers,and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number=input("\nfirst number:")
#     if first_number=='q':
#         break
#     second_number=input("\nSecond number:")
#     if(second_number=='q'):
#         break
#     try:
#         answer=int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print("You Can't divide by 0!")
#     else:
#         print(answer)

#处理文件异常
file_name='alice.txt'
try:
    with open(file_name) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg="Sorry,the file"+file_name+" does not exist."
    print(msg)

