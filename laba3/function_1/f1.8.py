def spy_game(n):
    s = ""
    for i in range(len(n)):
        s += str(n[i])
        if s.count("007")>=1:
            return "True"
    return "False"
print(spy_game(list(map(int, input().split()))))