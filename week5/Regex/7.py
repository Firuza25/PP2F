#snake case -> red_mad_robot
#camel case -> redMadRobo

# import re
# file=open("/Users/firuza/Desktop/PP2/week5/Regex/text.txt","r")
# result= re.sub("_","",file.read().title())




# print(result)

 

import re

s = open("/Users/firuza/Desktop/PP2/week5/Regex/text.txt","r")
l = re.split(r"_", s.read())
s2 = ''
for i in l:
    s2 += (i[0].upper() + i[1:])
print(s2)