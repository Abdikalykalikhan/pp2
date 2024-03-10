import re

def test(pattern, inputstring, outputstring):
    result = re.sub(pattern, r'\1 \2', inputstring)
    print(result)
    if result == outputstring:
        print("true")
    else:
        print("false")

pattern = r'([a-zA-Z])([A-Z])'

test(pattern, "MySuperTest", "My Super Test")
test(pattern, " MySuperTest IAmRobot", " My Super Test I Am Robot")