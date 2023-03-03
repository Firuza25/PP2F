#Верните год и название дня недели:
import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))