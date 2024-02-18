def square(a, b):
    for i in range(a, b):
        yield pow(i, 2)

a = int(input())
b = int(input())

q = square(a, b)

for j in square(a, b):
    print(next(q), end = " ")