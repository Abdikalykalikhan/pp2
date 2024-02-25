import re

def test(pattern, testinput, testoutput):
    if re.search(pattern, testinput) == testoutput:
        print("test is not passed")
    elif re.search(pattern, testinput) != None:
        print("test is passed!")
    else:
        print("test is not passed")

pattern = '^a(b*).'

test(pattern, "123ab45", None)
test(pattern, "123ab45as", None)
test(pattern, "123ab452", None)
test(pattern, "abb", True)
test(pattern, "abbb452", True)