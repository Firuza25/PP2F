def threes(l):
    for i in range(len(l)-1):
        if l[i]==3 and l[i+1]==3:
            return True
    return False

l=list(map(int,input().split()))
print(threes(l))
