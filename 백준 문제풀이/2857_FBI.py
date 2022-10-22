N = []; ans = []
for i in range(5):
    N.append(input())
    if N[i].count("FBI") > 0:
        ans.append(i+1)
if len(ans) > 0: print(*ans)
else: print("HE GOT AWAY!")