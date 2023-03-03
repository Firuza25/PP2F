x=350
def myfunc():
    global x
    x=200

myfunc()
print(x)

'''
To change the value of a global variable 
inside a function, refer to the 
variable by using the global keyword:
'''