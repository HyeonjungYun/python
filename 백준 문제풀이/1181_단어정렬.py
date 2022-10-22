'''
시간초과
import sys
b = {}
for i in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().strip()
    if b.get(len(a), 1) == 1:
        b[len(a)] = [a]
    else: 
        b[len(a)].append(a)
        b[len(a)] = sorted(set(b[len(a)]))
for i in range(len(b)):
    print(*b[sorted(b)[i]], end = " ")    
'''
'''
a = []
for i in range(int(input())):
    x = input()
    if not [len(x), x] in a:
        a.append([len(x), x])
a.sort()
a = [y for [x,y] in a]
print(*a)
'''
import sys
input()
print(*sorted(sorted(set(sys.stdin)), key = len))