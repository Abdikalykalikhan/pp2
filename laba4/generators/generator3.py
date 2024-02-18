def divided_3_4(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
a = divided_3_4(n)

for j in divided_3_4(n):
    print(next(a), end = " ")