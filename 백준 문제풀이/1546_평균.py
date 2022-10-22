N = int(input())
a = sorted(map(int, input().split()))
b = max(a)
for i in range(N):
    a[i] = (a[i] / b) * 100
print((sum(a)/N))