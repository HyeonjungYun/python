a = []
N = int(input())
for i in range(N):
    a.append(list(map(int, input().split())))
b = sorted(a)
for i in range(N):
    ans = 0
    for j in range(i+1, N):
        if b[i][0] < b[j][0]:
            if b[i][1] < b[j][1]: ans += 1
    a[a.index(b[i])] = ans + 1
print(*a)