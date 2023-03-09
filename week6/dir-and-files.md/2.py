'''
Write a Python program to check for access to a specified path. 
Test the existence, readability, writability and executability of
 the specified path
'''

import os
print('Exist:', os.access('/Users/firuza/Desktop/PP2', os.F_OK))
print('Readable:', os.access('/Users/firuza/Desktop/PP2', os.R_OK))
print('Writable:', os.access('/Users/firuza/Desktop/PP2', os.W_OK))
print('Executable:',os.access('/Users/firuza/Desktop/PP2', os.X_OK))