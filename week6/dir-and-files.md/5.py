'''Write a Python program to write a list to a fi
'''
name="/Users/firuza/Desktop/happy.txt"

with open(name,"a") as file:
    file.write(input()+"\n")

with open(name,"r") as file:
    print(file.read())

