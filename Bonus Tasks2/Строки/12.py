w = input()
t = ''
for i in range(len(w)):
    if i % 3 != 0:
        t +=w[i]
print(t)