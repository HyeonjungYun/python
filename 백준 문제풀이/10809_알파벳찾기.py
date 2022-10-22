a = input()
abc = list('abcdefghijklmnopqrstuvwxyz')
c=[-1 for i in range(26)]
for i in range(len(a)):
    if c[abc.index(a[i])] == -1:
        c[abc.index(a[i])] = i
    else: continue
print(*c)