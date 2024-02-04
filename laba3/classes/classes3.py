class Shape:
    def area(self) -> None:
        self.a = 0

class Rectangle:
    def __init__(self,length,width):
        self.length = length 
        self.width = width

    def area(self):
        self.a = self.length * self.width
        print(self.a)

x = Rectangle(int(input()),int(input()))

x.area()