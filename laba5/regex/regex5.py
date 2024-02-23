import re

inpa = input("")

result = re.search('^a*b*$', inpa)

if result:
    print("ok")
else:
    print("no")