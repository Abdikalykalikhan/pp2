import re

inpa = input()

for i in len(inpa):
    if inpa[i] == '_':
        inpa[i+1].upper()
print(inpa)
#pattern = r'[_]'

#result = re.sub(pattern, )