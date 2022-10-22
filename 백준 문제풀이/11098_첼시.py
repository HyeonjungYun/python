for i in range(int(input())):
    max = 0; maxp = ""
    for j in range(int(input())):
        N = list(input().split())
        if max < int(N[0]):
            max = int(N[0]); maxp = N[1]
    
    print(maxp)