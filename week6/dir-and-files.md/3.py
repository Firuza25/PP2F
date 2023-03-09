'''
Write a Python program to test whether a given path exists or not. 
If the path exist find the filename and directory portion of the given path.
'''
import os
path = '/Users/firuza/Desktop/PP2/week5/Regex/text.txt'

if os.path.exists(path):
    print("Path exists: ", os.path.exists(path))
    print("The filename:",os.path.basename(path))
    print("Directory:",os.path.dirname(path))
else:
    print("False")
 