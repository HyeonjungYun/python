c = []
for i in range(int(input())):
    a,b = map(int, input().split())
    c.append([b,a])
c = sorted(c)
for i in range(len(c)):
    print(f"{c[i][1]} {c[i][0]}")