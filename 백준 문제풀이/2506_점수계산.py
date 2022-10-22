N = int(input())
a = list(map(int, input().split()))

for i in range(1,N):
    if a[i] == 0:
        continue
    if a[i] == 1:
        if a[i-1] > 0:
            a[i] += a[i-1]
        elif a[i-1] == 0:
            a[i] = 1
print(sum(a))