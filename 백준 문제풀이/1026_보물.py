N = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))[::-1]
c = 0
for i in range(N):
    c += a[i]*b[i]
print(c)
