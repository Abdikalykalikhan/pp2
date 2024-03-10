import os
list=list(input().split())

with open('fibo', 'w') as file:
    for i in list:
        file.write(str(i))