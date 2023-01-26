#Есть способы сделать копию, один из способов - использовать встроенный метод списка copy().
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Другой способ сделать копию - использовать встроенный метод list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)