'''если вам нужна функция сортировки без учета регистра,
 используйте str.lower в качестве ключевой функции:
 '''
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)

