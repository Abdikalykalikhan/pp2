def filter_prime(n):
    count=0
    for i in range (1, n+1):
        if n % i == 0:
            count = count + 1
    return count == 2

result = [x for x in map(int, input().split()) if filter_prime(x)]

print(result)