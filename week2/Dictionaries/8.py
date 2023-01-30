thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#Вы можете получить доступ к элементам словаря, обратившись к его ключевому названию в квадратных скобках

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)

#Существует также метод под названием get(), который даст вам тот же результат
