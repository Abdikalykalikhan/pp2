def pallindrome(s):
    if s == s[::-1]:
        print("it is pallindrome")
    else:
        print("it is not pallindromme")
pallindrome(str(input()))