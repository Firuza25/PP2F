#Когда мы создаем кортеж, мы обычно присваиваем ему значения. Это называется "packing" кортежа:
fruits = ("apple", "banana", "cherry")

print(fruits)
 #Но в Python нам также разрешено извлекать значения обратно в переменные. Это называется "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

