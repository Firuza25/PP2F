g=int(input())
k=int(input())
l=int(input())
if (g*k>l) and (l%g==0) or (l%k==0):
    print("YES")
else:
    print("NO")