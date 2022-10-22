from math import*

No1 = int(input())
N1 = floor(sqrt(No1)) + 1
N2 = floor(sqrt(int(input()))) + 1
ans = []

if No1 == 1:
    ans.append(1)

for i in range(N1, N2):
    ans.append(i**2)

if len(ans) > 0:
    print(sum(ans))
    print(ans[0])
else: print(-1)
