'''a = input()

print(a[::-1])


#if input string
print(a.replace('s', 'e'))

def del_remove_pop():
    thislist = ["apple", "banana", "cherry"]
    thislist.pop(1)
    print(thislist)
    #["apple", "cherry"]

    thislist = ["apple", "banana", "cherry"]
    del thislist[0]
    print(thislist)
    #["banana", "cherry"]

    thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
    thislist.remove("banana")
    print(thislist)
    #["apple", "cherry", "banana", "kiwi"]



def filter_prime(n):
    count=0
    for i in range (1, n+1):
        if n % i == 0:
            count = count + 1
    return count == 2

result = [x for x in map(int, input().split()) if filter_prime(x)]

print(result)



import math
def square_lambda():
    x = lambda a, b, c : a*x**2 + b*x + c 
    
    D = b**2 - 4 * a * c
    if D == 0:
        print((-b)/2*a)
    
    else:
        print((-b + math.sqrt(D) /2 * a))
        print((-b - math.sqrt(D) /2 * a))
a = int(input())
b = int(input())
c = int(input())
square_lambda()





class person():
    def __init__(self, id, name, lastname, age):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age

    def dannye(self):
        print("Your id : " + self.id + "; Your name : " + self.name + " " + self.lastname)




class kidperson(person):
    def __init__(self, kidname, kidage, name):
        super().__init__(self, name)
        self.kidname = kidname
        self.kidage = kidage
    
    def kiddannye(self):
        print(" your name : " + self.kidname)

q = person("23B030476", "Alikhan", "Abdikalyk", "17")
w = kidperson("suslik", "2","Alikhan")
print(q.w.kidname)


'''
n =int(input())
i = 1
for i in range(n+1):
    print(i**2)