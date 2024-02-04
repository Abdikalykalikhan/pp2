class Myclasses:
    def __init__(self):
        self.string = ""

    def Getstring(self):
        self.string = input()

    def Printstring(self):  
        print(self.string.upper()) 

p1 = Myclasses()

p1.Getstring()
p1.Printstring()

