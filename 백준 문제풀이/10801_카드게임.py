a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in range(10):
    if (a[i] - b[i]) == 0: c.append(0)
    elif (a[i] - b[i]) > 0: c.append(1)
    elif (a[i] - b[i]) < 0: c.append(-1)
if sum(c) > 0: print('A')
elif sum(c) < 0: print('B')
elif sum(c) == 0: print('D')