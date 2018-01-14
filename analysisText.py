title="Alice in Wonderland"
print(title.split())

file_name="alice.txt"
try:
    with open(file_name) as f_obj:
        contents=f_obj.readlines()
except FileNotFoundError:
    msg="Sorry,the file"+file_name+" does not exist."
    print(msg)
else:
    words=contents.split()
    num_words=len(words)
    print("the file "+file_name+" has about "+str(num_words)+" words.")