import math
class myclass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        D = b**2 -4 * a * c
        if(D > 0):
            print((-b + math.sqrt(D) )/ 2*a)
            print((-b + math.sqrt(D) )/ 2*a)
        elif(D==0):
            print((-b)/2*a)
        else:
            print(complex((-b +(D))/ 2*a))
            print(complex((-b -(D))/ 2*a))

myclass(1,2, 2)