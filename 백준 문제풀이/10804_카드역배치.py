import sys

a = [x for x in range(1,21)]
for i in range(10):
    x,y = map(int, sys.stdin.readline().split())
    a[x-1:y] = a[x-1:y][::-1]
print(*a)