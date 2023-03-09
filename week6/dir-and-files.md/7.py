# from shutil import copyfile
# copyfile('/Users/firuza/Desktop/happy.txt', '/Users/firuza/Desktop/2.txt')
# # ???

with open('/Users/firuza/Desktop/happy.txt', 'r') as f1:
    s = f1.read()

with open('/Users/firuza/Desktop/2.txt','w') as f2:
    f2.write(s)