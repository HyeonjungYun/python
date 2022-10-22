N = int(input())
ans = 0
a = list(map(int, input().split()))
for i in range(5):
    if a[i] == N: ans += 1
print(ans)
