import re

def test(pattern, testData, expectedResult):
    result = re.sub(pattern, r"\1 \2", testData)
    print(result)
    if result == expectedResult:
        print("test is passed!")
    else: 
        print("test is not passed!")

pattern = r'([a-zA-Z])([A-Z])'

test(pattern, "MySuperTest", "My Super Test")
test(pattern, " MySuperTest IAmRobot", " My Super Test I Am Robot")