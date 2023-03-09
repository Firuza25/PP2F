W=input()
ul=0
ll=0
for i in W:
    if i>='A' and i<='Z':
        ul+=1
for i in W:
    if i>='a' and i<='z':
        ll+=1
print(ul,ll)