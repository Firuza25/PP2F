#Global Scope
#Global variables are available from within any scope, global and local.
x=300
def myfunc():
    print(x)
myfunc()
print(x)