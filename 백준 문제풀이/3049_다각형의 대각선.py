N = int(input())
if N == 3: print(0)
elif N == 4: print(1)
elif N >= 5: 
    print((N*(N-1)*(N-2)*(N-3))//24)