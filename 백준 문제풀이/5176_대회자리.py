for i in range(int(input())):
    a, b = map(int, input().split()); c = []
    for i in range(a):
        c.append(int(input()))
    c = list(set(c))
    print(a-len(c))