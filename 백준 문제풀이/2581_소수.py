from math import*

a = [i for i in range(int(input()),int(input())+1)]
b = []

for i in range(len(a)):
    if a[0] == 1:
        a[0] = 0
    ii = floor(sqrt(a[i]))+1
    for j in range(2, ii):
        if a[i] % j == 0:
            a[i] = 0
            break
    if a[i] != 0:
        b.append(a[i])
if len(b) > 0:
    print(sum(b));print(b[0])
else:
    print(-1)