import sys
N = []
n = int(sys.stdin.readline())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    N.append([a,b])
N.sort()
N.sort(key = lambda x: x[1])
ans = [[0,0]]
ans[0] = N[0]; N.pop(0)
for j in range(len(N)):
    if ans[-1][1] <= N[j][0]:
        ans.append(N[j])
        N[j] = [0,0]
print(len(ans))