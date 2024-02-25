import re

def test(pattern, testData, expectedResult):
    result = re.split(pattern, testData)
    print(result)
    if result == expectedResult:
        print("test is passed!")
    else: 
        print("test is not passed!")

pattern = r'([A-Z][a-z]*)'

test(pattern, "MySuperTest", "['', 'My', '', 'Super', '', 'Test', '']")
test(pattern, " MySuperTest IAmRobot", "[' ', 'My', '', 'Super', '', 'Test', ' ', 'I', '', 'Am', '', 'Robot', '']")