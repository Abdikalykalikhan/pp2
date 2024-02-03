def histogram(n):
    for i in n:
        print('*' * i)
histogram(list(map(int, input().split())))