#Метод format() принимает переданные аргументы, 
# форматирует их и помещает в строку, где находятся заполнители {}
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

'''
ошибка!
age = 36
txt = "My name is John, I am " + age
print(txt)
'''






quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#Метод format() принимает неограниченное количество аргументов и помещается в соответствующие заполнители




quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

'''мы можем использовать индексные номера {0}, 
чтобы убедиться, что аргументы помещены в правильные заполнители'''
