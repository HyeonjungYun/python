c = []
for i in range(int(input())):
    a = list(map(int, input().split()))
    b = list(set(a))
    if len(b) == 1:
        c.append(50000+(b[0]*5000))
    elif len(b) == 2:
        if a.count(b[0]) == 1:
            c.append(10000+(b[1]*1000))
        elif a.count(b[0]) == 3:
            c.append(10000+(b[0]*1000))
        elif a.count(b[0]) == 2:
            c.append(2000+(b[0]*500)+(b[1]*500))
    elif len(b) == 3:
        for j in range(3):
            if a.count(b[j]) == 2:
                c.append(1000+(b[j]*100))
    elif len(b) == 4:
        c.append(max(b)*100)
print(max(c))