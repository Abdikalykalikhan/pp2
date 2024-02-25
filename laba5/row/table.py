import re

f = open("row.txt", "r", encoding = "utf8")
text = f.read()

pattern = r"\n(?P<order>[0-9]+)\.\n(?P<name>.+)\n(?P<count>.+)x(?P<price>.+)\n"

results = re.finditer(pattern, text)

for x in results:
    print(x.group('order') + " " + x.group('name') + " " + x.group('count') + " " + x.group('price'))