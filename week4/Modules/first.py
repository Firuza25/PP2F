import module
print(module.sum(4,6))


import module as mod
print(mod.sum(7,9))

from module import sum
print(sum(15,3))

from module import *
print(sum(34,654))