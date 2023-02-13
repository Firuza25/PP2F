from itertools import permutations
def perm(s):
    for i in permutations(s):
        print(i)

s=input()
perm(s)
