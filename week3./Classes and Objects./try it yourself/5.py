class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def mfunc(self):
        print("Hello my name is "+ self.name)

p1=Person("Firuza",17)
p1.mfunc()
