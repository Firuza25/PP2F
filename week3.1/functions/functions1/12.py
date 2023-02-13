def histogram(a):
    for i in a:
        for j in range(i):
            print("*",end="")
        print()


a=list(map(int,input().split()))
histogram(a)