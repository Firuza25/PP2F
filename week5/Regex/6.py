import re

file=open("/Users/firuza/Desktop/PP2/week5/Regex/text.txt","r")
result=re.sub("[ ,.]",":",file.read())
print(result)
