a,b = map(int, input().split())
c = list(map(int, input().split()))
x = 0
d = [c[0]]
for i in range(1,b):
    if len(d) < a: 
        if (c[i] in d) == True: continue
        else: d.append(c[i])
    e = []
    if (c[i] in d) == True: pass
    else:
        for j in d:
            if (j in c[i:]) == True: e.append(c[i:].index(j))
            else: e.append(101)
        d[e.index(max(e))] = c[i]
        x += 1
print(x)