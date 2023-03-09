'''Write a Python program to count the number of lines in a text file.'''

file="/Users/firuza/Desktop/happy.txt"

with open(file, 'r') as file:
    x = len(file.readlines())
    print('Lines:', x) 



