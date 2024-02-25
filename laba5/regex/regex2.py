import re

def test(pattern, testData, expectedResult):
    if re.search(pattern, testData) == expectedResult:
        print("test is passed!")
    elif re.search(pattern, testData) != None:
        print("test is passed!")
    else: 
        print("test is not passed!")

pattern = 'ab{2,3}'

test(pattern, "123ab452", None)
test(pattern, "123abb452", True)
test(pattern, "abbb452", True)
test(pattern, "123ab45", None)
test(pattern, "123ab45as", None)
