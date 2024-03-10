def even(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

n = int(input())
a = even(n)

for j in even(n):
    print(next(a), end = ", ")
    