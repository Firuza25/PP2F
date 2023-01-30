#Метод intersection_update() сохранит только те элементы, которые присутствуют в обоих наборах.


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#Метод intersection() вернет новый набор, который содержит только те элементы,
#  которые присутствуют в обоих наборах.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
