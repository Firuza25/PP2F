#С помощью оператора break мы можем остановить цикл до того, как он пройдет через все элементы:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
