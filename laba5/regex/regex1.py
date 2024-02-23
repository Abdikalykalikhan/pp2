import re

inpa = input()

x = re.search('^a(b*)$ ' ,inpa )

if x:
    print("Match found!")
else:
    print("Not found!")