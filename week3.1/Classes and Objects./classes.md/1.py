class upstr():
    def __init__(self):
        self.string=""
    
    def getString(self):
        self.string=input()

    def printString(self):
        print(self.string.upper())
    
string=upstr()
string.getString()
string.printString()
#