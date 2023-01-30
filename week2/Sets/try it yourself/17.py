#Метод symmetric_difference_update() сохранит только те элементы, которых нет в обоих наборах.x = {"apple", "banana", "cherry"}
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#Возвращает набор, содержащий все элементы из обоих наборов, за исключением элементов, присутствующих в обоих:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)