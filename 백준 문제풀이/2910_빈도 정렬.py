def z(x): return a.index(x[1])
def y(x): return x[0]
input()
a = list(map(int, input().split()))
b = list(set(a))
c = []
for x in b:
    c.append([a.count(x),x])
c = sorted(c, key = z)
c = sorted(c,reverse = True, key = y)
for i in c:
    print((str(i[1])+" ")*i[0], end = '')