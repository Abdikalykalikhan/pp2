def trapezoid(h, a, b):
    area = (a + b)/2 * h
    print(area)

h = int(input("height : "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
trapezoid(h, a, b)