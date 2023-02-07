A=int(input())
f1=1
i=f0=fn=0
while i<A:
    fn=f0+f1
    f0,f1=f1,fn
    i+=1
    if fn==A:
        print(i+1)
        break
    if fn>A:
        print(-1)
        break