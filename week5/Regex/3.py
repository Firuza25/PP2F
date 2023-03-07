#3
import re

file=open("/Users/firuza/Desktop/PP2/week5/Regex/text.txt","r")
result=re.findall("[a-z]+_[a-z]+",file.read())
print(result)
