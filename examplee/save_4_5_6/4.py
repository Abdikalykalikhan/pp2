def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input("Enter the number of Fibonacci numbers to generate: "))
for num in fibo(n):
    print(num)

'''def fib(n):
    a=[0,1]
    for i in range(2,n):
        a.append(a[i-2]+a[i-1])
    yield a
n=int(input())
print(*fib(n))'''