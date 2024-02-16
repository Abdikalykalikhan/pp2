#generator for list
# a = [ i**2 for i in range(1, n)]
# print(a)

n = int(input())


def generate(n):
    for i in range(1, n+1):
        yield next(a)
        
a = ( i**2 for i in range(1, n))

generate(n)

