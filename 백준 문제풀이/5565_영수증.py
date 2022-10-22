import sys
a = []
for i in range(10): a.append(int(sys.stdin.readline()))
print(a[0] - sum(a[1:]))