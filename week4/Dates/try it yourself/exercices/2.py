from datetime import datetime,timedelta
x=datetime.now()-timedelta(1)
y=datetime.now()
z=datetime.now()+timedelta(1)
print(x,y,z,sep="  ")