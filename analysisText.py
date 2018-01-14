title="Alice in Wonderland"
print(title.split())

file_name="test.txt"
words=''
try:
    with open(file_name) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg="Sorry,the file"+file_name+" does not exist."
    print(msg)
else:
    try:
        words=contents.split()
    except AttributeError:
        print('没有属性')
    num_words = len(words)
    print("the file "+file_name+" has about "+str(num_words)+" words.")


def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents=f_obj.read()
    except FileNotFoundError:
        msg="Sorry,the file "+filename+"does not exist."
        print(msg)
        #pass 失败时不提示
    else:
        words=contents.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+"words.")

file_name='test.txt'
count_words(file_name)

file_name=['test1.txt','test.txt','teee.txt']
for filename in file_name:
    count_words(filename)