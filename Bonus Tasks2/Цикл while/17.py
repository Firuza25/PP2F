s1 = k = s = 0
n = int(input())
while n != 0:
    k += 1
    s += n
    s1 += n ** 2
    n = int(input())
print(((s1 - s ** 2 / k)/(k - 1))**0.5)