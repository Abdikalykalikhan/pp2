def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime(n):
    for j in range(2, n):
        if isPrime(j):
            yield j

n = int(input())
at = prime(n)

for j in prime(n):
    print(next(at))