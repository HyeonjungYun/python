from sys import*

N = int(input())
a = []
sum = 0
for i in range(N):
    a.append(int(stdin.readline()))
a.sort()
for i in range(N):
    sum += abs((i+1) - a[i])
print(sum)