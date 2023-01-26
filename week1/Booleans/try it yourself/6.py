class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
'''Еще одно значение, или объект в данном случае, оценивается как False,
 и это если у вас есть объект, созданный из класса с функцией __len__, 
 которая возвращает 0 или False:'''