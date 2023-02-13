#Используем слова mysillyobject и abc вместо self:
class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age
    
    def myfunc(abc):
        print("Hello my name is "+ abc.name)

p1=Person("Firuza",17)
p1.myfunc()