def affin(n,a,b):
    c = (a*(ord(n)-65) + b)
    if c > 25: c %= 26
    return chr(c+65)
for i in range(int(input())):
    a,b = map(int, input().split())
    c = input()
    for i in c:
        print(affin(i,a,b), end="")
    print()