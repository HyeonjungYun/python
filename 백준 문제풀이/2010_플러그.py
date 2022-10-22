import sys
N = int(input())
a = []
for i in range(N):
    a.append(int(sys.stdin.readline()))
print(sum(a)-(N-1))