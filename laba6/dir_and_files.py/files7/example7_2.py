with open('files7.py', 'r') as file:
    data = file.read()

with open(r'example7_2.py', 'w') as file:
    file.write(data)