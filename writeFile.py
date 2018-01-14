file_name='programming.txt'

with open(file_name,'w') as file_object:
    file_object.write("I Love programming.\n")
    #写入多行
    file_object.write("I Love creating new games.\n")


