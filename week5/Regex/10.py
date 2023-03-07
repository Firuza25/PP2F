#Write a Python program to convert a given camel case string to snake case.

import re

file =open("/Users/firuza/Desktop/PP2/week5/Regex/text.txt","r")

l = re.findall(r"[A-Z][a-z]*", file.read())
s1 = ''
for i in l:
    s1 += (i[0].lower() + i[1:] + '_')

print(s1[:-1])




