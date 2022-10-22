def fac(n):
    if n <= 1: return 1
    return n * fac(n-1)
a = list(str(fac(int(input()))))
b = 0
while 1:
    if a.pop() != '0': break
    else: b += 1
print(b)