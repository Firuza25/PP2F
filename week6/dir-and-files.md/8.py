import os
path='/Users/firuza/Desktop/2 2.txt'

if os.path.exists(path):
    os.remove(path)
    print("File deleted successfully")
else:
    print("We dont have this file")