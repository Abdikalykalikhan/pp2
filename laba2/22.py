thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print(thisset)
#{'cherry', 'apple', 'orange', 'banana'}

###

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset)
#{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}