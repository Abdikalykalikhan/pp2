def pallindrome(q):
    if q == q[::-1]:
        print("true")
    else:
        print("false")

q = input("")
pallindrome(q)