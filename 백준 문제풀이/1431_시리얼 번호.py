def sumint (n):
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = [int(x) for x in n if x not in a]
    return sum(n)
a = []
for i in range(int(input())):
    a.append(input())
a = sorted(sorted(sorted(a), key = sumint), key = len)
print(*a)
