def power(n):
    for i in range(1, n):
        if i % 2 == 0:
            yield pow(i, 2)

n = int(input())
at = power(n)
for sum in power(n):
    print(next(at))