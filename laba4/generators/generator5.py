def numbers(n):
    i = n
    while i >=0:
        yield i
        i = i-1
    
n = int(input())
a = numbers(n)

for j in numbers(n):
    print(next(a), end = " ")