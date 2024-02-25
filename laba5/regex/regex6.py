import re 

def test(pattern, testinput, testoutput):
    result = re.sub(pattern, ':', testinput)
    if result == testoutput:
        print("test is passed!")
    else:
        print("test is not passed!")

pattern = '[,]|[" "]|[@]'

test(pattern, "hi salam,privet", "hi:salam:privet")
test(pattern, " fibo itis me", ":fibo:itis:me")
test(pattern, "hi salam,privet", "hi:salam:privet")
test(pattern, ":,,,:", ":::::")
test(pattern, "hey , My name", "hey:::My:name")