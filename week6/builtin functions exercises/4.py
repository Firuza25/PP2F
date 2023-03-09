'''
Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
'''
import math
import time
a=int(input())
t=int(input())
t=t/1000#milli=10^-3
answ=math.sqrt(a)
print(f"Square root of {a} after {t} miliseconds is {answ}")