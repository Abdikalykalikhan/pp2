def unque(q):
    q.sort()
    for i in range(len(q)-1,0,-1):
        if q[i] == q[i-1]:
            q.remove(q[i])
    print(q)
unque(list(input().split()))