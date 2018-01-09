name="I Love You"
#以首字母大写的方式显示字符串
print(name.title());
#字符串的操作
print(name.upper());
print(name.lower());

#合并和拼接字符串
first_name="Jackson";
last_name="Michael";
full_name=first_name+" "+last_name;

print(full_name.title());

#使用制表符和换行符
print("\tPython");
print("lanuages:\nPython\nC\nJavascript");

print("lanuages:\n\tPython\n\tC\n\tJavascript");

#删除空白
goods="python ";
print(goods);
goods.rstrip(); #去掉右空格 lstrip() strip()
print(goods);

#python 2.7
#print "hello world"