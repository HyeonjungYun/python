N = list(map(int, input().split(maxsplit = 3)))
max1 = []
min1 = []

for i in range(0, 3):
    if max(N) == N[i]:
        max1.append(N[i])
    if min(N) == N[i]:
        min1.append(N[i])

if len(max1) == 3:
    prise = max1[0] * 1000 + 10000
elif len(max1) == 2:
    prise = max1[0] * 100 + 1000
elif len(min1) == 2:
    prise = min1[0] * 100 + 1000
else:
    prise = max1[0] * 100
    
print(prise)