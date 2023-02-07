w= input()
a = w[:w.find('h') + 1] 
b = w[w.find('h') + 1:w.rfind('h')]
c = w[w.rfind('h'):]
w = a + b.replace('h', 'H') + c
print(w)