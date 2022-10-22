a = input()
n = len(a)
d = 10
for i in range(0, n-1):
    b = a[i] + a[i+1]
    if b == '()' or b == ')(':
        d += 10
    if b == '((' or b == '))':
        d += 5
print(d)