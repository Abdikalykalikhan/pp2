import re 

def test(pattern, testinput, testoutput):
    result = re.sub(pattern, r'\1_\2', testinput)
    print(result)
    if result == testoutput:
        print("true")
    else:
        print("false")

pattern = r'([a-z])([A-Z])'

test(pattern, "MyNameIs", "My_Name_Is")
test(pattern, "aaMyNameIsNot", "aa_My_Name_Is_Not")