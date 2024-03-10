import re

f = open('example_10.txt', 'r')
strinput = f.read()

pattern = r'(?P<mail>.+@.+\.com)\n(?P<num>[0-9]+\.)(?P<name>.+)'
#\n(?P<passnum>[1-9]+\.)\s(?P<pass>[1-9].+)'
result = re.finditer(pattern , strinput)

for x in result:
    print(x.group('mail') +"\n"+ x.group('num')+"\n"+ x.group('name'))
#+" "+ x.group('passnum') +" "+ x.group('pass'))
'''
import json
import re
file = open("db.json")
db = json.load(file)
pattern = r".+@.+\.com"

def correct_mail(pattern, db):
    for i in db:
        if re.search(pattern, i["email"]):
            print(f"{i["name"]} has correct email:{i["email"]}")
        else:
            print(f"{i["name"]} has uncorrect email:{i["email"]}")
            
correct_mail(pattern, db)'''