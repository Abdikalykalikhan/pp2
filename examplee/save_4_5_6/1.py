import re

def test(pattern, testinput, testoutput):
    result = re.search(pattern, testinput)
    print(result)
    if result:
        print("ok")
    else:
        print("nop")


pattern = r'^8[1-9]{10}'
#phone number
test(pattern, "87771233455", True)
test(pattern, "877712334556", False)
test(pattern, "8777123345", False)
test(pattern, "8f555555555", False)