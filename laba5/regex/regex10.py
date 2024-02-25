import re 

def test(pattern, testinput, testoutput):
    result = re.sub(pattern, r'\1_\2', testinput)
    if result == testoutput:
        print("test is passed!")
    else:
        print("tet is not passed!")

pattern = r'([a-z])([A-Z])'

test(pattern, "MyNameIs", "My_Name_Is")
test(pattern, "aaMyNameIsNot", "aa_My_Name_Is_Not")