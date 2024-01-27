fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]

print(newlist)
#['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

###

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]

print(newlist)
#['hello', 'hello', 'hello', 'hello', 'hello']