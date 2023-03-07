import re

file=open("/Users/firuza/Desktop/PP2/week5/Regex/text.txt","r")
result=re.findall(".*a.*b.*b.*b?.*",file.read())
print(result)