from sys import*
from datetime import*

n = int(stdin.readline())
N = []
for i in range(n):
    a,b,c,d = map(int, stdin.readline().split())
    N.append([(date(2022, a, b)- date(2022,1,1)).days, (date(2022, c, d)- date(2022,1,1)).days])
ans = []
N1 = [a[1] for a in N if a[0] <= 59]
if N1 == []: print(0)
else:
    ans.append(max(N1))
    t = 0
    for i in range(n):
        try:
            if ans[-1] > 333: break
            N1 = [a[1] for a in N if a[0] <= ans[-1]]
            if max(N1) == ans[-1]: t += 1; break
            else: ans.append(max(N1))
        except:
            t += 1
            break
    if t > 0: print(0)
    else: print(len(ans))