def rev(s):
    s = reversed(s)
    print(*s)

s = list(input().split())
rev(s)