'''
    类的相关
'''
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        #给属性指定默认值
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(str(self.year)+' '+self.make+' '+self.model)
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    #通过方法修改属性值 封装
    def update_odometer(self,mileage):
        #self.odometer_reading=mileage
        #封装
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer")
    #通过方法对属性的值进行递增
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

    def fill_gas_tank(self):
        print('tast car!')
my_new_car=Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
#修改属性的值
#my_new_car.odometer_reading=25
#通过方法修改属性值
my_new_car.update_odometer(1000)
#通过方法实现属性值 的递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
#将实例用做属性
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-KWH battery")
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message="This Car can go approximately "+str(range)
        message+=" miles on a full charge."
        print(message)
#继承--
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        #self.battery_size=70
        self.battery=Battery(85) #将实例用做属性
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-KWH battery")

my_tesla=ElectricCar('tesla','model S',2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
