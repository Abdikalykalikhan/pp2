import re

inpa = input("")

result = re.findall('[A-Z][a-z]', inpa)

if result:
    print("ok")
else:
    print("no")