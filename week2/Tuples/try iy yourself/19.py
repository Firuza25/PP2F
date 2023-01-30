'''
Если количество переменных меньше количества значений, вы можете добавить 
* к имени переменной, и значения будут присвоены переменной в виде списка
'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

