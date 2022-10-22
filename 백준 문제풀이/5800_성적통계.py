for i in range(int(input())):
    a = list(map(int, input().split()))
    c = sorted(a[1:])
    for j in range(len(c)-1):
        c[j] = c[j+1] - c[j]
    c.pop()
    print("Class",i+1); print(f"Max {max(a[1:])}, Min {min(a[1:])}, Largest gap {max(c)}")