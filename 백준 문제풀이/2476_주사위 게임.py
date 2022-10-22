num = int(input())
prise = []
for k in range(0, num):
    N = list(map(int, input().split(maxsplit = 3)))
    max1 = []
    min1 = []

    for i in range(0, 3):
        if max(N) == N[i]:
            max1.append(N[i])
        if min(N) == N[i]:
            min1.append(N[i])

    if len(max1) == 3:
        prise.append(max1[0] * 1000 + 10000)
    elif len(max1) == 2:
        prise.append(max1[0] * 100 + 1000)
    elif len(min1) == 2:
        prise.append(min1[0] * 100 + 1000)
    else:
        prise.append(max1[0] * 100)
    
print(max(prise))