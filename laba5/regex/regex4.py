import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern, testData) == expectedResult:
        print(testNumber + " is passed!")
    elif re.search(pattern, testData) != None:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")

pattern = '[A-Z][a-z]'

test(pattern, "AsAssscbns", "test1", True)
test(pattern, "AAAAAAAAAAAAAAA", "test2", None)
test(pattern, "aaaaAAa", "test3", True)
test(pattern, "123452", "test4", None)
test(pattern, "AYHAah", "test5", True)