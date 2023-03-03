import math
n=int(input("Number of sides: "))
s=int(input("Length of the side: "))
A=int((n*pow(s,2)/(4*math.tan(math.pi/n))))
print(A)#area of the polygon



