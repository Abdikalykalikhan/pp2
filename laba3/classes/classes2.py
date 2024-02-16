class Shape:
    def area(self) -> None:
        self.a = 0
        
class Square:
    def __init__(self):
        self.length = int(input())

    def area(self):
        self.a = self.length * self.length

        print(self.a)

p = Square()
p.area()