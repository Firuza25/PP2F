#4

import re

file=open("/Users/firuza/Desktop/PP2/week5/Regex/text.txt","r")
result=re.findall("[A-Z][a-z]+",file.read())
print(result)
