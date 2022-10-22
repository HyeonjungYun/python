import sys
def min(n):
    return n[1]
def max(n):
    return n[0]
a = {}; b = []
N = int(sys.stdin.readline())
for i in range(N):
    n = int(input())
    b.append(n)
for i in set(b):
    a[i] = 0
for i in b:
    a[i] += 1
a = sorted(zip(a.values(), a.keys()), reverse = True, key = min)
a = sorted(a, key = max)
print(a[-1][1])