import sys
N = []
n = int(sys.stdin.readline())
for i in range(n):
    N.append(int(sys.stdin.readline()))
N.sort()
ans = []
for i in range(1,n+1):
    ans.append(N[-i] * i )
print(max(ans))