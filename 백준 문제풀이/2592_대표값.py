a= []; c = []
for i in range(10):
    a.append(int(input()))
b = sorted(list(set(a)))
for j in range(len(b)):
    c.append(a.count(b[j]))
print((int(sum(a)/10)), b[c.index(max(c))])