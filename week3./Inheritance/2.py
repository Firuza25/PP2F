#Создать дочерний класс
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    pass

x=Student("Mike", "Olsen")
y=Person("Mira","Kaimodina")
x.printname()
y.printname()

#Теперь класс Student имеет те же свойства и методы, что и класс Person.

