import math
def polygon(n, l):
    area = (n * l ** 2) / (4 * math.tan(math.pi / n))
    print(area)

n = int(input("sides: "))
l = int(input("Input the length of a side: "))
polygon(n, l)