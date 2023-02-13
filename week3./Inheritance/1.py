# Создать родительский класс
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

p=Person("Firuza","Sagatkyzy")
p.printname()