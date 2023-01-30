'''
Объект в методе update() не обязательно должен быть набором,
 это может быть любой итеративный объект (кортежи, списки, словари и т.д.).
 '''
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

