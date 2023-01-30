a1 = int(input())
b1 = int(input())
a2 = int(input()) 
b2 = int(input()) 
q = abs(a1 - a2) 
w = abs(b1 - b2) 
if q == 1 and w == 2 or q== 2 and w == 1: 
    print('YES') 
else: print('NO')