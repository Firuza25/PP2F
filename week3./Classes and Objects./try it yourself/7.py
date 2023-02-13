#Вы можете изменить свойства таких объектов:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def myfunc(sd):
        print("Hello my name is "+sd.name)

p1=Person("Firuza",17)
p1.myfunc()
p1.age=19
print(p1.age)