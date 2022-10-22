p0 = 100; p1 = 100

for i in range(int(input())):
    sc = list(map(int, input().split()))
    if sc[0] > sc[1]:
        p1 -= sc[0]
    elif sc[0] < sc[1]:
        p0 -= sc[1]
print(p0); print(p1)
