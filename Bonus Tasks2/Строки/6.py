n=input()
if n.count('f')==1:
    print(-1)
elif n.count('f')<1:
    print(-2)
else:
    print(n.find('f', n.find('f')+1))