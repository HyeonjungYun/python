a = []; b = []
for i in range(20):
    x = int(input())
    if i < 10: a.append(x)
    else: b.append(x)
print(sum(sorted(a)[7:]),sum(sorted(b)[7:]))