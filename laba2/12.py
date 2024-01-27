thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#['apple', 'banana', 'watermelon', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#['apple', 'banana', 'cherry', 'orange']


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']