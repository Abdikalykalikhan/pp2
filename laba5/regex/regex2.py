import re

inpa = input("")

result = re.search('^a(b{2,3})' , inpa)
if result:
    print('ok')
else:
    print('mo')