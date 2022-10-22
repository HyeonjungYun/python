a,b = map(int, input().split())
c = []
if a > b: a,b = b,a
for i in range(a+1,b):
    c.append(i)
print(len(c))
print(*c)