x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

''''
После создания кортежа вы не можете изменить его значения. 
Кортежи неизменны или неизменны, как их также называют.

Но есть обходной путь. Вы можете преобразовать кортеж в список,
 изменить список и преобразовать список обратно в кортеж.



'''