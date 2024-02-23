import re

inpa = input("")

result = re.findall('[a-z]_[a-z]', inpa)

if result:
    print("yep")
else:
    print("nop")