i = 1
while i < 6:
  print(i)
  i += 1


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# Note that number 3 is missing in the result
  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 