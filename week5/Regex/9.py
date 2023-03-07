import re
file=open("/Users/firuza/Desktop/PP2/week5/Regex/text.txt","r")
result=re.findall("[A-Z]{1}[a-z]\w*",file.read())
print(result)

