#Write a Python program to split a string at uppercase letters.
import re
file=open("/Users/firuza/Desktop/PP2/week5/Regex/text.txt","r")
result=re.split("[A-Z]",file.read())
print(result)
