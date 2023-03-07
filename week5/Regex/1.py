
import re

file=open("/Users/firuza/Desktop/PP2/week5/Regex/text.txt","r")
result=re.findall(".*a.*b*",file.read())
print(result)

#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
