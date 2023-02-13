def myfunc(n):
    return lambda a:a*n

mult1=myfunc(2)
mult2=myfunc(3)

print(mult1(11))
print(mult2(22))