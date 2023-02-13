def zzs(l):
    for i in range(len(l)-1):
        if l[i]==0 and l[i+1]==0 and l[i+2]:
            return True
    return False

l=list(map(int,input().split()))
print(zzs(l))
#1,2,4,0,0,7,5
#1,0,2,4,0,5,7
#1,7,2,0,4,5,0