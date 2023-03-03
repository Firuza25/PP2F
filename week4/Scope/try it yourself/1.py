#Local Scope
def myfunc():
    x=300
    print(x)

myfunc()
'''variable created inside a function is available inside that function'''

def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

'''The local variable can be accessed from a function within the function:'''