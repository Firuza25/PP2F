'''
You are given list of numbers separated by spaces.
 Write a function filter_prime which will take list 
 of numbers as an agrument and returns only prime numbers 
 from the list.
 '''
def filter_prime(n):
    a=[]
    for i in n:
        count=0
        for j in range(1,i+1):
            if i%j==0 and i!=2:
                count+=1
        if count==2:
            a.append(i)
    print(a)
n=list(map(int,input().split()))
filter_prime(n)

