fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#['apple', 'banana', 'mango']

#########

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]

print(newlist)
#[ "banana", "cherry", "kiwi", "mango"]

#########

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]

print(newlist)
#["apple", "banana", "cherry", "kiwi", "mango"]