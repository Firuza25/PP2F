#Вы можете удалить объекты с помощью ключевого слова del:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def mfunc(bbc):
        print("Hello my name is "+bbc.name)

p1=Person("Firuza",17)
del p1
print(p1)