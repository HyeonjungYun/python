ans = []
for i in range(10):
    a, b = map(int,input().split())
    if i == 0:
        ans.append(b)
    else:
        ans.append(ans[i-1]-a); ans[i] += b
print(max(ans))
