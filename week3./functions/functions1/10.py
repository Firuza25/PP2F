list1 = list(map(int, input().split()))

def set(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2 

print(*set(list1))