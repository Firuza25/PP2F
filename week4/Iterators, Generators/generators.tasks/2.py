# n = int(input())

# for i in range(0, n+1, 2):
#   if i < n - 1:
#     print(i, end = ',' )
#   else:
#     print(i) 

'''
def evennum(n):
  for i in range(0,n+1):
    if i%2==0:
      yield i
n=int(input())
for i in evennum(n):
   v=",".join(i)
   print(i,v)
   ????????
'''

n2 = int(input())
b = [i for i in range(n2) if i % 2 == 0]
print(b,sep=",")

  
  