def myfunc(n):
    return lambda a:a*n

mult=myfunc(3)
print(mult(11))