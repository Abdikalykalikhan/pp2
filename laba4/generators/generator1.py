#generator for list
# a = [ i**2 for i in range(1, n)]
# print(a)


def generate(n):
    for i in range(n+1):
        yield pow(i, 2)

n = int(input())        
at = generate(n)

for j in generate(n):
    print(next(at))

