from itertools import permutations 
def permutati(a):
    p = permutations(a)
    for i in p:
        print(i)

permutati(input())