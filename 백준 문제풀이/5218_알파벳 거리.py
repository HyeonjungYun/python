for i in range(int(input())):
    c = []
    a, b = map(list,input().split())
    for j in range(len(a)):
        if ord(b[j]) >= ord(a[j]):
            c.append(ord(b[j]) - ord(a[j]))
        else: 
            c.append(ord(b[j])+26 - ord(a[j]))
    print("Distances:",*c)