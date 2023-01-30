#Преобразуйте кортеж в список, удалите "apple" и преобразуйте его обратно в кортеж:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

