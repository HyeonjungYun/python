import sys
a,b = map(int,input().split())
c = []; ans = 0
for i in range(a):
    c.append(int(sys.stdin.readline()))
c = sorted(c)[::-1]
for i in range(a):
    if b >= c[i]:
        ans += b//c[i]
        b = b%c[i]
print(ans)