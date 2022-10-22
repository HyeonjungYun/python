a = []
while True:
    try:
        b = input().split()
        for x in b: a.append(int(x[::-1]))
    except EOFError:
        break
print(*sorted(a[1:]))