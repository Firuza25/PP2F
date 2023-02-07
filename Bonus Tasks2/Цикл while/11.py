p = int(input())
ans = 0
while p != 0:
    next = int(input())
    if next != 0 and p < next:
        ans += 1
    p = next
print(ans)