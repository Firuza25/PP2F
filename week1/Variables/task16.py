#Чтобы создать глобальную переменную внутри функции, вы можете использовать ключевое слово global.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
'''
Чтобы изменить значение глобальной 
переменной внутри функции,мы обратимься
 к переменной с помощью ключевого слова global

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
'''