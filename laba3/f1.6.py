def reversed(s):
    for i in range(len(s)):
        print(s[len(s)-i-1])


reversed(list(map(str, input().split())))