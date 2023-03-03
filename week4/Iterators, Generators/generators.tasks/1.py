
#1var
n=int(input())
a=(i**2 for i in range(1,n+1))
for i in a:
 print(i)

'''
#2var
def sq(n):
    for i in range(1,n+1):
        yield i**2

n=int(input())
for i in sq(n):
    print(i,end=" ")

    
'''