def palindrome(s):
    return s == s[::-1]


s=input()
a=palindrome(s)
if a:
        print("Yes")
else:
        print("No")
