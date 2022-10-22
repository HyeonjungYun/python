from math import*

N, N1 = map(int,input().split())

ans = [1]
n = floor(sqrt(N)) + 1
for i in range(1,n):
    if N % i == 0:
        ans.append(i)
        ans.append(N//i)
ans = sorted(list(set(ans)))
if len(ans) < N1:
    print(0)
else:
    print(ans[N1-1])