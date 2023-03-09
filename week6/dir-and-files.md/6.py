import string, os

if not os.path.exists("aripter"):
   os.makedirs("aripter")#Функция makedirs() модуля os рекурсивно создает все промежуточные каталоги, если они не существуют. 

for let in string.ascii_uppercase:
   with open(let + ".txt", "w") as f:
       f.writelines("Done!")
