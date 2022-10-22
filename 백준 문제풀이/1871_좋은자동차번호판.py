a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for j in range(int(input())):
    b,c = input().split('-')
    b = b[::-1]
    d = 0
    for i in range(3):
        d += a.index(b[i])*(26**i)
    if abs(d-int(c)) <= 100: print("nice")
    else: print("not nice")