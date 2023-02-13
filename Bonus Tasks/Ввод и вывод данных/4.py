n = int(input())
x = 0
if n >= 1440:
    x = n//1440
    n = n - 1440 * x
h = n // 60
m = n % 60

print (h, m)