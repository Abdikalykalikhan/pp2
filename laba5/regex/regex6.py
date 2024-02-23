import re 

inpa = input("")

pattern = r'[,]|[" "]|[.]|[;]'
result = re.sub(pattern, ':', inpa)
print(result)
if result:
    print("ok")
else:
    print("no")