from math import*
a = int(input())
b = list(map(int, input().split()))
co = 0
for i in range(a):
    c = floor(sqrt(b[i])) + 1
    for j in range(2, c):
        if b[i] % j == 0:
            b[i] = 0
    if b[i] == 1: b[i] = 0
    if b[i] != 0:
        co += 1
print(co)
