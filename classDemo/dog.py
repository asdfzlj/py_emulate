class Dog():
    '''
        __init__特殊的方法，创建实例时调用
        形参self必不可少，还必须位于其它形参的前面 。
        因为python调用init创建实例时，将自动传入实参self.
        每个与类相关联的方法
调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法
self会自动传递，因此我们不需要传递它。
以self为前缀的变量都可供类中的所有方法使用，我们
还可以通过类的任何实例来访问这些变量。 self.name = name获取存储在形参name中的值，并将
其存储到变量name中，然后该变量被关联到当前创建的实例
    '''
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title()+" is now sitting")

    def roll_over(self):
        print(self.name.title()+" rolled over!")