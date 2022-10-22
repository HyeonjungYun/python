'''a = input().upper()
b = list(set(a))
c = []
for i in range(len(b)):
    c.append(a.count(b[i]))
if c.count(max(c)) > 1: print('?')
else: print(b[c.index(max(c))])
'''
s = input()
v = sorted({'a','d','r','x','b', '?'}, key = s.count)
print(v)