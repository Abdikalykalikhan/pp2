def has_3_3(n):
    s = ""
    for i in range(len(n)):
        s += str(n[i])
        print(s)
        if s.count("33")>=1:
            return "True"
    return "False"

print(has_3_3(list(map(int, input().split()))))