n=input()
if n.count('f')==1:
    print(n.find('f'))
elif n.count('f')>=2:
    print(n.find('f'),n.rfind('f'))