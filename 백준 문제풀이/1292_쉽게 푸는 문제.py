a, b = map(int,input().split())
c = []
n = 1
while 1:
    for i in range(n):
        c.append(n)
        if len(c) >= b:
            break
    if len(c) >= b:
            break
    n += 1
print(sum(c[a-1:b]))